# Job 008: Enable CORS

- **Issue**: [issues/008_cors_error.md](../issues/008_cors_error.md)
- **Description**: Allow cross-origin requests from the frontend by adding CORS headers in the Flask backend.

## Summary of Changes

- Installed `flask-cors` and enabled it in `backend/app.py`.
- Added test to verify the `Access-Control-Allow-Origin` header.
- Updated `requirements.txt` and documentation.

## Commands Used

- `pip install -r backend/requirements.txt`
- `black backend`
- `flake8 backend`
- `npx prettier --write .`
- `cd frontend && npx eslint .`
- `cd frontend && npm test -- --run`
- `cd backend && pytest`

## Output

- Prettier log: `/tmp/prettier.log`
- ESLint log: `/tmp/eslint.log`
- Pytest log: `/tmp/pytest.log`
- Vitest log: `/tmp/npm_test.log`
