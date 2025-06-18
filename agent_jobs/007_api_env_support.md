# Job 007: API Environment Support

- **Issue**: [issues/007_api_env_support.md](../issues/007_api_env_support.md)
- **Description**: Configure environment variables for API URL and update frontend code to use it.

## Summary of Changes
- Added `.env.development` and `.env.production` files with `VITE_API_URL`.
- Updated `usePlaybackStore.js` to fetch the API using `import.meta.env.VITE_API_URL`.
- Documented setup in `README.md`.
- Fixed flake8 line-length errors in `piper_wrapper.py`.

## Commands Used
- `npm install`
- `npx prettier --write .`
- `npx eslint .`
- `black backend`
- `flake8 backend`
- `pytest`
- `npm test -- --run`

## Output
- ESLint log: `/tmp/eslint.log`
- Prettier log: `/tmp/prettier.log`
- Pytest log: `/tmp/pytest.log`
- Vitest log: `/tmp/npm_test.log`
