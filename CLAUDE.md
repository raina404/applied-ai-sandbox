# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A tiny Flask web application used as the practice playground for the
**Code2College Applied AI Cohort**. It's intentionally incomplete — each
task in `tasks/` walks the student through fixing or adding one piece.

## Stack

- Python 3.10+, Flask 3.x, pytest, Jinja2 templates, vanilla HTML/CSS

## Commands

```bash
python app.py          # Run the app → http://localhost:5000
pytest                 # Run all tests
pytest tests/test_task_01.py          # Run tests for a single task
pytest tests/test_task_01.py::test_empty_title_shows_error  # Single test
```

## Architecture

`app.py` uses a **factory function** (`create_app() -> Flask`) rather than a module-level app instance. Notes live in `app.notes` (a plain Python list on the Flask instance) — they're in-memory only and reset on restart.

`tests/conftest.py` provides two shared fixtures used by all test files:
- `app` — calls `create_app()` with `TESTING=True`
- `client` — wraps the app with Flask's built-in test client

Each task has a stub comment in `app.py` marking exactly where new code belongs (e.g., `# TASK 01 will add validation here.`). The corresponding task description is in `tasks/TASK_NN.md` and the acceptance tests are in `tests/test_task_NN.py`.

## Conventions

- The task is "done" when `pytest tests/test_task_NN.py` passes.
- Never edit `tests/` — change `app.py` / `templates/` instead. Tests are the spec.
- Keep changes scoped to the current task. Don't refactor unrelated files.
- Read the test file first — it tells you exactly what behavior is expected.
- Always read the task file before writing code; plan before implementing.

## Notes Storage
- Notes are stored in-memory as a list of dicts on app.notes — there is no database for notes.
- Do not move notes to SQLite or any other database.
