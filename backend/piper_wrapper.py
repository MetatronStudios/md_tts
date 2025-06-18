import base64
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List


class PiperWrapper:
    """Manage a Piper TTS subprocess."""

    def __init__(self, executable: str = "piper", voice: str | None = None) -> None:
        cmd = [executable]
        if voice:
            cmd.extend(["--voice", voice])

        if shutil.which(executable):
            self.process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        else:
            # Fallback stub when Piper is not installed
            self.process = None

    def synthesize(self, text: str) -> Dict[str, object]:
        if self.process is None:
            # Generate silent placeholder audio when Piper is unavailable
            return self._fake_response(text)
        if not self.process.stdin or not self.process.stdout:
            raise RuntimeError("Piper process not started correctly")

        # Piper expects a JSON line with text and a temporary output path
        with tempfile.TemporaryDirectory() as tmpdir:
            out_wav = Path(tmpdir) / "output.wav"
            timings_path = Path(tmpdir) / "timings.json"

            request = json.dumps({"text": text, "output_path": str(out_wav)})
            self.process.stdin.write(request + "\n")
            self.process.stdin.flush()

            # Read response JSON from Piper
            response_line = self.process.stdout.readline()
            if not response_line:
                stderr = self.process.stderr.read() if self.process.stderr else ""
                raise RuntimeError(f"Piper failed: {stderr}")
            resp = json.loads(response_line)

            if resp.get("status") != "ok":
                raise RuntimeError(f"Piper error: {resp}")

            if timings_path.exists():
                timings = json.loads(timings_path.read_text())
            else:
                # Fallback: basic timings assuming 0.2s per word
                timings = []
                start = 0.0
                for word in text.split():
                    timings.append(
                        {"word": word, "startTime": start, "endTime": start + 0.2}
                    )
                    start += 0.2

            audio_b64 = base64.b64encode(out_wav.read_bytes()).decode("ascii")

        return {
            "audioContent": audio_b64,
            "mimeType": "audio/wav",
            "timings": timings,
        }

    def _fake_response(self, text: str) -> Dict[str, object]:
        """Return dummy audio and timings when Piper is unavailable."""
        words = text.split()
        timings: List[Dict[str, float]] = []
        start = 0.0
        for word in words:
            timings.append({"word": word, "startTime": start, "endTime": start + 0.2})
            start += 0.2
        # create 1 second of silence as WAV
        with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
            tmp.write(
                b"\x52\x49\x46\x46\x24\x00\x00\x00\x57\x41\x56\x45"
                b"\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00"
                b"\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00"
                b"\x64\x61\x74\x61\x00\x00\x00\x00"
            )
            tmp.flush()
            audio = base64.b64encode(Path(tmp.name).read_bytes()).decode("ascii")
        return {"audioContent": audio, "mimeType": "audio/wav", "timings": timings}

    def terminate(self) -> None:
        if self.process.poll() is None:
            self.process.terminate()
            self.process.wait(timeout=5)
