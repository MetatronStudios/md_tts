# Issue: HTTP 500 Error - Broken Pipe

## Description
When attempting to play audio by posting to `http://localhost:5000/api/tts`, the server returns an HTTP 500 error with the following message:

```json
{"error":"[Errno 32] Broken pipe"}
```

## Proposed Solution
1. **Error Diagnosis**:
   - Investigate the root cause of the broken pipe error.
   - Check if the issue is related to the `PiperWrapper` subprocess or the HTTP server implementation.

2. **Error Handling**:
   - Implement proper error handling to prevent the server from crashing.
   - Return a more descriptive error message to the client.

3. **Testing**:
   - Add unit tests to simulate the broken pipe scenario.
   - Verify that the server handles the error gracefully.

## Acceptance Criteria
- The server should not crash when a broken pipe error occurs.
- A descriptive error message should be returned to the client.
- The issue should be reproducible and resolved.

## Tasks
- Investigate the cause of the broken pipe error.
- Update the error handling logic in the backend.
- Add unit tests to cover the broken pipe scenario.
- Verify the fix by testing the API endpoint.

## References
- Endpoint: `http://localhost:5000/api/tts`
- Error message: `{"error":"[Errno 32] Broken pipe"}`
