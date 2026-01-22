# Claude Code Guidelines

## Project Overview

This is the Human Spaceflight API - a Django-based API for tracking human spaceflight data including missions, astronauts, agencies, and EVAs.

## Git Conventions

**Follow the standards in [CONTRIBUTING.md](CONTRIBUTING.md):**

- **Branches**: Use `feature/`, `fix/`, `chore/`, `refactor/`, `docs/`, `test/`, `style/` prefixes with kebab-case descriptions
- **Commits**: Use conventional commits format: `type(scope): subject`
  - Types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `style`, `perf`, `ci`
  - Scopes: `missions`, `astronauts`, `agencies`, `evas`, `accounts`, `common`, `deps`, `docker`, `templates`, `models`, `views`
  - Use imperative mood, no capital, no period
- **Do not** use empty scope parentheses like `chore():` - either include a scope or omit parentheses entirely

## Tech Stack

- Python / Django
- Docker for containerization
- PostgreSQL database

## Code Standards

- PEP 8 style guide
- 4 spaces indentation (Python)
- 88 character line length (Black formatter)
- 2 spaces indentation (HTML templates)

## Testing

Run tests before committing: `python manage.py test`