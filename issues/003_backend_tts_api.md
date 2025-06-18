# 003: Backend TTS API

## Goal
Provide an HTTP endpoint that converts text to audio using Piper.

## Tasks
- Implement a Flask endpoint `POST /api/tts` accepting `{ "text": "..." }`.
- Create `piper_wrapper.py` using `subprocess.Popen` to manage the Piper engine.
- Return base64 encoded audio and word timing information as described in the ADD.
- Add error handling and input validation.

## Completion
The task is complete when sending a text snippet returns audio data and timings in JSON.
