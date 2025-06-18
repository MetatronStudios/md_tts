# Job 006: Testing and Documentation

- **Issue**: [issues/005_testing_and_docs.md](../issues/005_testing_and_docs.md)
- **Description**: Add automated testing setup for frontend and backend and update documentation with testing instructions.

## Commands Used
- `npm install vitest @vue/test-utils jsdom --save-dev`
- `npx prettier --write .`
- `npx eslint frontend --config frontend/eslint.config.js`
- `black backend`
- `flake8 backend --max-line-length 88`
- `pytest`
- `npm test -- --run`

## Summary
- Configured Vitest in `vite.config.js` and added test script to `package.json`.
- Added Markdown parser utility and sample Vitest suite.
- Created pytest configuration and sample API test.
- Updated README with testing steps.
- All tests pass.
