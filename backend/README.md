# Backend

This directory contains the Flask application that provides the `/api/tts` endpoint.
It relies on a local installation of [Piper TTS](https://github.com/rhasspy/piper).

## Installing Piper

1. Download a Piper release for your platform and place the `piper` binary on
   your `PATH`.
2. Download a voice model (`.onnx` and `.onnx.json`) and keep both files
   together in a directory.
3. Test the installation:

   ```bash
   echo "test" | piper --model en_US-amy-medium.onnx --output_file test.wav
   ```

4. If `piper` is not on your `PATH`, pass the full path when constructing
   `PiperWrapper` in `app.py`.

See [INSTALL.md](INSTALL.md) for detailed instructions and troubleshooting tips.
