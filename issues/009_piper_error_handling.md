# Issue: Improve Error Handling for Piper Unavailability

## Description
When Piper is not available or there is an error executing the Piper command, the current implementation in `PiperWrapper` returns a fake response with silent placeholder audio. This approach does not provide sufficient feedback about the error.

## Proposed Solution
1. **Error Message Retrieval**:
   - If Piper is unavailable or fails to execute, attempt to retrieve the error message from the executable command.
   - Use the `stderr` output from the Piper subprocess to extract the error message.

2. **HTTP Error Header**:
   - Instead of returning a fake response, return an HTTP error header.
   - Include the error message (if available) as part of the error response.

3. **Implementation Details**:
   - Modify the `synthesize` method in `PiperWrapper` to:
     - Check for errors in the Piper subprocess.
     - Extract the error message from `stderr`.
     - Return an HTTP error header with the error message.

## Acceptance Criteria
- When Piper is unavailable, the `synthesize` method should return an HTTP error header.
- The error response should include the error message from the Piper executable, if available.
- Ensure backward compatibility for cases where no error message is available.

## Tasks
- Update the `synthesize` method in `PiperWrapper`.
- Add unit tests to verify the new error handling behavior.
- Update documentation to reflect the changes.

## References
- File: `backend/piper_wrapper.py`
- Current behavior: Returns fake response with silent placeholder audio.
- Proposed behavior: Return HTTP error header with error message.
