# Issue 013: Marked Word Out of Sync with Spoken Audio

## Job Description

Resolve timing mismatch between spoken audio and highlighted words during playback. Update the frontend playback logic to wait for the `playing` event and cancel existing timeouts when stopping playback. Update docs to mention the synchronization improvement.

## Prompts

- User: "fix a new issue"

## Summary of Changes

- Added highlight timeout management and start delay in `usePlaybackStore.js`.
- Updated README to document playback highlighting synchronization.
- Added inline comment explaining sanitized error handling in `app.py`.

## Relevant Paths

- `frontend/src/composables/usePlaybackStore.js`
- `backend/app.py`
- `README.md`
