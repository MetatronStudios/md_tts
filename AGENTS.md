# AGENTS Guide

This repository contains specifications for a Markdown Text-to-Speech Reader.

## Development Workflow

1. Review the specifications in `specs/` before starting work.
2. Select a task from `issues/` and follow its instructions.
3. Keep code modular and documented. Use Python with PEP8 and black style; use Prettier/ESLint for JavaScript.
4. Format and lint code before committing:
   - Python: `black backend` and `flake8 backend`.
   - JavaScript: `npx prettier --write .` and `npx eslint .`.
5. Run available tests with `pytest` for Python and `npm test` for the frontend when applicable.
6. Summaries of completed tasks must be stored in `agent_jobs/` using sequentially numbered Markdown files detailing job description, prompts, code diffs, and relevant output paths.

## Pull Request Requirements

- Reference the task file you worked on.
- Provide a concise summary of changes and test results.
