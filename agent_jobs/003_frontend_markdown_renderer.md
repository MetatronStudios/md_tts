# Job 003: Frontend Markdown Renderer

- **Issue**: [issues/002_frontend_markdown_renderer.md](../issues/002_frontend_markdown_renderer.md)
- **Description**: Implement components to input Markdown, render it with line and word IDs, and emit events when words are clicked.

## Summary of Changes
- Added `markdown-it` dependency and configured ESLint for Vue flat config.
- Created `MarkdownInput.vue` and `ContentViewer.vue` with custom markdown-it rules that wrap lines and words with data attributes.
- Added `usePlaybackStore.js` composable to hold Markdown and rendered HTML.
- Updated `App.vue` to use new components and removed the default `HelloWorld` example.

## Commands Used
- `npm install markdown-it@^14.0.0`
- `npx prettier --write .`
- `npx eslint .`
- `black backend`
- `flake8 backend`
- `pytest`

## Output
- Prettier output: `/tmp/prettier.log`
- ESLint log: `/tmp/eslint.log`
- Backend test log: `/tmp/pytest.log`
