# Contributing Guidelines

## Git Workflow Standards

### Branch Naming Convention

Use descriptive kebab-case names with optional type prefix:

```
<type>/<description>
```

Examples:
```
feature/astronaut-search-filter
fix/login-redirect-issue
chore/update-dependencies
refactor/mission-models
docs/api-documentation
```

**Branch Types:**
- `feature/` - New features
- `fix/` - Bug fixes
- `chore/` - Maintenance tasks (dependencies, configs, build)
- `refactor/` - Code refactoring (no behavior change)
- `docs/` - Documentation only changes
- `test/` - Adding or updating tests
- `style/` - Code style/formatting (no logic change)

**For simple changes**, descriptive names without type prefix are acceptable:
- `rebrand-to-space-pioneers-api`
- `update-readme`

### Commit Message Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/).

**Format:**
```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Examples:**
```bash
feat(missions): add crew member age calculation
fix(auth): resolve OAuth callback redirect issue
chore(deps): update Django to 5.1.14
docs(readme): add setup instructions for Docker
refactor(astronauts): simplify nationality filter logic
test(missions): add crew assignment validation tests
style(templates): fix indentation in base.html
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `chore` - Maintenance (dependencies, configs, build tools)
- `docs` - Documentation only
- `refactor` - Code change that neither fixes a bug nor adds a feature
- `test` - Adding or updating tests
- `style` - Code formatting, missing semicolons, etc. (no code change)
- `perf` - Performance improvement
- `ci` - CI/CD configuration changes

**Scope (recommended but optional):**
- Use app names: `missions`, `astronauts`, `agencies`, `evas`, `accounts`, `common`
- Or component: `deps`, `docker`, `templates`, `models`, `views`
- Can be omitted for changes that span multiple scopes

**Subject:**
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Keep under 72 characters

**Body (optional):**
- Explain what and why, not how
- Separate from subject with blank line
- Wrap at 72 characters

**Footer (optional):**
- Reference issues: `Closes #123` or `Fixes #456`
- Breaking changes: `BREAKING CHANGE: description`

**Good Examples:**
```
feat(astronauts): add search by nationality

Adds a dropdown filter on the astronauts list page allowing users
to filter by country of origin.

Closes #45
```

```
fix(missions): resolve crew member duplicate entries

When adding crew members, the same astronaut could be added twice
to the same mission. This adds validation to prevent duplicates.
```

```
chore(deps): update Django from 5.1.6 to 5.1.14

Security update fixing 8 CVEs in Django core.
```

**Bad Examples:**
```
# Too vague
fix: bug fix

# Not imperative
feat: Added new feature

# Missing type
update readme

# Unclear scope
chore(): stuff
```

**Consistency Notes:**

Avoid:
- Empty scope parentheses: `chore():` - either use a scope or omit parentheses
- Inconsistent capitalization
- Past tense ("Added", "Fixed")

Prefer:
- Clear scopes when applicable: `chore(deps):`, `feat(missions):`
- No parentheses when scope doesn't apply: `docs:`, `test:`
- Imperative mood: "add", "fix", "update"

## Pull Request Process

1. **Create a feature branch from main**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code standards

3. **Commit your changes** using conventional commits
   ```bash
   git commit -m "feat(scope): add new feature"
   ```

4. **Push to GitHub**
   ```bash
   git push -u origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Use a descriptive title
   - Reference any related issues
   - Describe what changed and why
   - Include testing steps if applicable

6. **Wait for review** before merging

## Code Standards

### Python
- Follow PEP 8 style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter standard)
- Use type hints where applicable

### Django
- Follow Django coding style
- Keep models in `models.py`, views in `views.py`, etc.
- Use Django's class-based views where appropriate
- Write docstrings for complex functions and classes

### Templates
- Use 2 spaces for indentation in HTML
- Keep template logic simple (use template tags/filters)
- Add comments for complex template sections

### Testing
- Write tests for new features
- Maintain or improve test coverage
- Run tests before submitting PR: `python manage.py test`

## Questions?

If you have questions about contributing, feel free to:
- Open an issue
- Reach out at info@spacepioneersapi.com