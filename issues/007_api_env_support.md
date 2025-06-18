# Issue 007: API Environment Support

## Description
Accessing the API without a definition of the server results in a 404 error. The application currently attempts to make a POST request to `http://localhost:5173/api/tts`, which fails because the API server URL is not defined for development or production environments.

## Steps to Reproduce
1. Run the application in development mode.
2. Attempt to use the text-to-speech functionality.
3. Observe the console error:
   ```
   usePlaybackStore.js:43 
   POST http://localhost:5173/api/tts 404 (Not Found)
   ```

## Expected Behavior
The application should use an environment-specific API server URL to make requests.

## Proposed Solution
- Add environment variable support for defining the API server URL.
- Configure separate URLs for development and production environments.
- Update the frontend code to use the environment variable for API requests.

## Tasks
1. Update the project setup to include environment variable support.
2. Define API server URLs for development and production in `.env` files.
3. Modify the frontend code to use the environment variable for API requests.
4. Test the solution in both development and production environments.

## References
- Console error: `usePlaybackStore.js:43 POST http://localhost:5173/api/tts 404 (Not Found)`
