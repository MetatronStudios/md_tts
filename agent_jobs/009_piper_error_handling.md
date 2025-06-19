# Job 009: Piper Error Handling

- **Issue**: [issues/009_piper_error_handling.md](../issues/009_piper_error_handling.md)
- **Description**: Improve error reporting when Piper is not available.

## Summary of Changes

- Updated `PiperWrapper.synthesize` to raise `RuntimeError` with stderr output instead of returning a fake response.
- Added `_get_error_message` helper for capturing Piper errors.
- Modified Flask `tts_endpoint` to return HTTP 503 with `X-Piper-Error` header when Piper fails.
- Updated backend tests to cover success and error scenarios.
- Documented new behavior in `README.md`.

## Commands Used

- `pip install -r backend/requirements.txt`
- `black backend`
- `flake8 backend`
- `npx prettier --write .`
- `cd frontend && npx eslint .`
- `cd frontend && npm test -- --run`
- `cd backend && pytest`
