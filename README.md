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

Both servers will run locally and communicate via HTTP APIs.

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
