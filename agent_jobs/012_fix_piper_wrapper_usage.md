# Issue 012: Fix PiperWrapper Usage According to Piper Help

## Job Description

Update PiperWrapper to use the correct command options based on the Piper CLI help.

## Prompts

- User: "fix the new issue piper_wrapper"

## Summary of Changes

- Updated `PiperWrapper` to pass `--model` and `--config` with `--json-input`.
- Adjusted synthesize to send `output_file` field and parse plain responses.
- Updated application instantiation in `app.py` for new parameters.
- Revised documentation for installing and configuring Piper.
- Updated tests to expect HTTP 500 status after error handling change.

## Relevant Paths

- `backend/piper_wrapper.py`
- `backend/app.py`
- `backend/INSTALL.md`
- `backend/README.md`
- `backend/tests/test_tts.py`
- `README.md`
