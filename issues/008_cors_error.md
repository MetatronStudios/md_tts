# Issue 008: CORS Error

## Description
Accessing the API from the frontend results in a CORS error. The application currently attempts to make a POST request to `http://localhost:5000/api/tts`, but the backend does not include the required `Access-Control-Allow-Origin` header in its response.

## Steps to Reproduce
1. Run the backend server on `http://localhost:5000`.
2. Run the frontend server on `http://127.0.0.1:5173`.
3. Attempt to use the text-to-speech functionality.
4. Observe the console error:
   ```
   Access to fetch at 'http://localhost:5000/api/tts' from origin 'http://127.0.0.1:5173' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.
   ```

## Expected Behavior
The backend should include the `Access-Control-Allow-Origin` header in its response to allow cross-origin requests from the frontend.

## Proposed Solution
- Update the Flask backend to include CORS headers in its responses.
- Use the `flask-cors` library to configure CORS support for the API endpoints.

## Completion Criteria
The task is complete when the frontend can successfully make requests to the backend without encountering CORS errors.
