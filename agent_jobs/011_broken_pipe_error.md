# Issue 011: HTTP 500 Error - Broken Pipe

## Job Description
Fix backend to handle BrokenPipeError from Piper process gracefully and add tests for this scenario.

## Prompts
- User: "fix the next issue"

## Summary of Changes
- Updated `PiperWrapper.synthesize` to detect terminated process and handle BrokenPipeError when writing to or reading from Piper.
- Added unit test `test_tts_broken_pipe` simulating a broken pipe by patching Piper process.
- Formatted code and ensured linting passes.

## Relevant Paths
- `backend/piper_wrapper.py`
- `backend/tests/test_tts.py`
