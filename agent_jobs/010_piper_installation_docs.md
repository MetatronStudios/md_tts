# Job 010: Piper Installation Docs

- **Issue**: [issues/010_piper_installation_docs.md](../issues/010_piper_installation_docs.md)
- **Description**: Provide documentation for installing Piper TTS and configuring it with `PiperWrapper`.

## Summary of Changes
- Added `backend/INSTALL.md` with step-by-step instructions for downloading Piper and a sample voice.
- Created `backend/README.md` summarizing installation steps and linking to the detailed guide.
- Updated root `README.md` to reference the new installation guide.

## Commands Used
- `pip install -r backend/requirements.txt`
- `black backend`
- `flake8 backend`
- `npx prettier --write .`
- `cd frontend && npm install`
- `cd frontend && npx eslint .`
- `cd frontend && npm test -- --run`
- `cd backend && pytest`
