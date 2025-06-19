# Installing Piper TTS

This project expects the `piper` executable to be available on your system.
The following steps show one way to install Piper and an example voice.

## 1. Download Piper

Grab a binary release for your platform from the
[Piper releases page](https://github.com/rhasspy/piper/releases).
Extract the archive and place the `piper` binary somewhere on your `PATH`
(e.g. `/usr/local/bin`).

## 2. Download a Voice Model

Download a voice from the same releases page or from
[Hugging Face](https://huggingface.co/rhasspy/piper-voices).
A voice consists of a `.onnx` model file and a matching `.onnx.json` config file.
Place both files in a directory of your choice.

Example using `curl`:

```bash
curl -L -o en_US-amy-medium.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx
curl -L -o en_US-amy-medium.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json
```

## 3. Verify Piper

Run Piper directly to confirm it works:

```bash
echo "Hello from Piper" | \
  piper --model en_US-amy-medium.onnx --output_file test.wav
```

Play the resulting `test.wav` to ensure audio was generated.

## 4. Configure `PiperWrapper`

`PiperWrapper` looks for the `piper` executable in your `PATH`. If it is located
elsewhere, pass the full path when constructing the wrapper in `app.py`:

```python
from piper_wrapper import PiperWrapper

# tts = PiperWrapper('/opt/piper/piper', 'en_US-amy-medium')
```

You can also specify the `--voice` argument to set a default voice.

## Troubleshooting

- **piper: command not found** — ensure the binary directory is in your `PATH`.
- **No such file or directory for voice** — check the paths to your `.onnx` and `.onnx.json` files.
- **Silent output** — verify that the voice files are compatible with your
  Piper version.
