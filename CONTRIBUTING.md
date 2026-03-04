# Contributing

Thank you for your interest in contributing to this project. Contributions of all kinds are welcome, including bug reports, feature requests, documentation improvements, and code changes.

## How to Contribute

### Reporting Issues

If you encounter a bug or have a feature request, please [open an issue](https://github.com/E339-art/upwork/issues/new/choose) using the appropriate template. When reporting bugs, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior versus actual behavior
- Your environment details (OS, Python version, etc.)

### Submitting Changes

1. **Fork the repository** and create a new branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards described below.

3. **Write or update tests** to cover your changes:

   ```bash
   python -m pytest tests/ -v
   ```

4. **Run the linters** to ensure code quality:

   ```bash
   make lint
   ```

5. **Commit your changes** with a clear, descriptive commit message:

   ```bash
   git commit -m "feat: add new utility function for data validation"
   ```

6. **Push to your fork** and [open a pull request](https://github.com/E339-art/upwork/compare).

### Commit Message Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Purpose |
|---|---|
| `feat:` | A new feature |
| `fix:` | A bug fix |
| `docs:` | Documentation changes |
| `style:` | Code style changes (formatting, no logic change) |
| `refactor:` | Code refactoring (no feature or fix) |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks (CI, dependencies, etc.) |

### Coding Standards

- **Formatting:** All Python code must be formatted with [Black](https://github.com/psf/black)
- **Linting:** All code must pass [Ruff](https://github.com/astral-sh/ruff) checks
- **Testing:** All new features must include corresponding tests
- **Documentation:** Public functions and classes must include docstrings
- **Type Hints:** Use Python type hints for function signatures

### Code Review

All submissions require review before merging. Reviewers may request changes, and all CI checks must pass. Please be patient and responsive during the review process.

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this standard.

## Questions?

If you have questions about contributing, feel free to [open a discussion](https://github.com/E339-art/upwork/issues) or reach out directly.

Thank you for helping improve this project.
