# 004: Audio Playback and Highlighting

## Goal
Synchronize audio playback with dynamic line and word highlighting.

## Tasks
- Implement playback controls in `PlaybackControls.vue` and connect them to the state store.
- Use the timings returned by the backend to update `currentLineId` and `currentWordId` during playback.
- Apply CSS classes `highlight-line` and `highlight-word` in `ContentViewer.vue` based on the state.
- Ensure highlighting resets when playback stops.

## Completion
The task is complete when the user can hear audio and see synchronized highlighting for a sample text.
