# 002: Frontend Markdown Renderer

## Goal
Render user-provided Markdown with word and line identifiers for highlighting.

## Tasks
- Implement `MarkdownInput.vue` with a textarea and Render button.
- Use `markdown-it` with custom rules to wrap each line with `data-line-id` and each word with `data-word-id` spans.
- Create `ContentViewer.vue` to display the rendered HTML and emit a `read-from-word` event when a word is clicked.
- Store the rendered structure in the `usePlaybackStore.js` composable.

## Completion
The task is complete when Markdown can be entered, rendered, and clicking a word emits the correct word identifier.
