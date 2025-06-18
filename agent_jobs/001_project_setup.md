# Job 001: Project Setup

- **Issue**: [issues/001_project_setup.md](../issues/001_project_setup.md)
- **Description**: Initialize base project structure with Vue frontend and Flask backend. Configure formatting tools and basic instructions.

## Commands Used
- `npm init vite@latest frontend -- --template vue`
- Installed ESLint and Prettier
- `python3 -m venv venv` and installed Flask, flake8, black

## Summary of Changes
- Added `frontend/` Vue project with ESLint and Prettier config
- Added `backend/` Flask skeleton with virtualenv and requirements
- Created `pyproject.toml` for black and flake8
- Added root `.gitignore` and project `README.md`

## Output
- Build logs: `frontend/dist/`
- Flask run log: `/tmp/flask.log`
