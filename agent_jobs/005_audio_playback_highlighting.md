# Job 005: Audio Playback and Highlighting

- **Issue**: [issues/004_audio_playback_highlighting.md](../issues/004_audio_playback_highlighting.md)
- **Description**: Implement playback controls and synchronized highlighting during audio playback.

## Summary of Changes
- Added new state and methods in `usePlaybackStore.js` to handle audio playback and highlighting.
- Created `PlaybackControls.vue` component with play, pause, and stop buttons.
- Updated `ContentViewer.vue` to apply `highlight-line` and `highlight-word` classes based on store state.
- Updated `App.vue` to fetch audio from the backend and start playback when a word is clicked.
- Added highlight styles in `style.css`.

## Commands Used
- `pip install -r backend/requirements.txt`
- `black backend`
- `flake8 backend`
- `npm install` (frontend)
- `npx eslint . --config eslint.config.js`
- `npx prettier --write .`
- `npm test` *(fails: Missing script)*
- `pytest`

## Output
- Flake8 log: `/tmp/flake8.log`
- ESLint log: `/tmp/eslint.log`
- Prettier log: `/tmp/prettier.log`
- npm install log: `/tmp/npm_install.log`
- npm test log: `/tmp/npm_test.log`
- Pytest log: `/tmp/pytest.log`
