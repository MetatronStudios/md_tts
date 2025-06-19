import base64
import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # noqa: E402

from app import app, tts  # noqa: E402


def test_tts_endpoint(monkeypatch):
    def fake_synthesize(text: str):
        return {"audioContent": "", "mimeType": "audio/wav", "timings": []}

    monkeypatch.setattr(tts, "synthesize", fake_synthesize)

    client = app.test_client()
    resp = client.post("/api/tts", json={"text": "hello world"})
    assert resp.status_code == 200
    assert resp.headers.get("Access-Control-Allow-Origin") == "*"
    data = resp.get_json()
    assert "audioContent" in data
    assert "mimeType" in data and data["mimeType"] == "audio/wav"
    assert "timings" in data
    assert isinstance(data["timings"], list)
    base64.b64decode(data["audioContent"])


def test_tts_piper_unavailable(monkeypatch):
    monkeypatch.setattr(
        tts,
        "synthesize",
        lambda text: (_ for _ in ()).throw(RuntimeError("piper missing")),
    )

    client = app.test_client()
    resp = client.post("/api/tts", json={"text": "hi"})
    assert resp.status_code == 503
    assert resp.headers.get("X-Piper-Error") == "piper missing"
