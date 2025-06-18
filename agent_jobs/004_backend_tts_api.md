# Job 004: Backend TTS API

- **Issue**: [issues/003_backend_tts_api.md](../issues/003_backend_tts_api.md)
- **Description**: Implement Flask endpoint to convert text to audio using a Piper wrapper and return base64 audio with timings.

## Summary of Changes
- Added `piper_wrapper.py` with a fallback stub when Piper is missing.
- Updated `backend/app.py` with `/api/tts` endpoint using the wrapper.
- Created pytest `backend/tests/test_tts.py` to verify API response structure.

## Commands Used
- `pip install -r backend/requirements.txt`
- `black backend`
- `flake8 backend`
- `pytest`
- `npm install` (frontend)
- `npx eslint .`
- `npx prettier --write frontend`

## Output
- Test log: `/tmp/pytest.log`
- ESLint log: `/tmp/eslint.log`
- Prettier log: `/tmp/prettier.log`
- npm test log: `/tmp/npm_test.log`
