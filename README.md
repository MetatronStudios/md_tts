# Markdown Text-to-Speech Reader

This project provides a basic setup for a Vue.js frontend and Flask backend.

## Development Setup

### Frontend

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

### Backend

1. Create and activate a Python virtual environment:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```bash
   flask --app app run
   ```
   The backend uses `flask-cors` to allow requests from the frontend during development.

Both servers will run locally and communicate via HTTP APIs.

When Piper is unavailable, the backend returns a `503` status from `/api/tts`
and includes an `X-Piper-Error` header describing the problem.

Playback highlighting now waits for the audio element's `playing` event,
ensuring that the marked word stays in sync with spoken audio.

### Environment Variables

The frontend expects an environment variable `VITE_API_URL` pointing to the back-end API.
Create the following files under `frontend/`:

```bash
echo "VITE_API_URL=http://localhost:5000/api" > frontend/.env.development
echo "VITE_API_URL=/api" > frontend/.env.production
```

Vite will use the appropriate file based on the build mode.

### Installing Piper TTS

The backend requires the `piper` executable along with a model file and its
matching `.onnx.json` config. See `backend/INSTALL.md` for setup instructions.

## Testing

### Frontend

Run unit tests with Vitest:

```bash
cd frontend
npm test
```

### Backend

Execute Python tests with pytest:

```bash
cd backend
pytest
```
