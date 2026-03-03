# Architecture

This document describes the high-level architecture and design decisions for this repository.

## Overview

The repository is organized as a monorepo-style portfolio that serves two primary purposes: showcasing completed freelance projects and maintaining a library of reusable utilities. The structure is designed to be modular, allowing individual projects to be self-contained while sharing common tooling and configuration.

## Directory Layout

| Directory | Purpose |
|---|---|
| `src/` | Shared source code and reusable utility modules |
| `tests/` | Test suite mirroring the `src/` structure |
| `docs/` | Project-level documentation and guides |
| `portfolio/` | Individual project showcases, each with its own README |
| `scripts/` | Automation and setup scripts |
| `.github/` | GitHub-specific configuration (CI, templates, Dependabot) |

## Design Principles

The codebase adheres to several core principles that guide all development decisions.

**Modularity** is the primary organizational principle. Each portfolio project is self-contained within its own directory, with its own README, dependencies (if any), and documentation. Shared code lives in `src/` and is imported as needed.

**Testability** is enforced through a comprehensive test suite. Every utility function includes corresponding tests, and the CI pipeline runs tests across multiple Python versions to ensure compatibility.

**Documentation-first** development means that every module, function, and project includes clear documentation. Public APIs use docstrings following Google-style conventions, and architectural decisions are recorded in this document.

**Automation** reduces manual overhead. The Makefile provides common commands, GitHub Actions handles CI/CD, and Dependabot manages dependency updates automatically.

## Technology Choices

Python was selected as the primary language due to its versatility across the service domains offered (web development, data engineering, automation, and machine learning). The tooling choices reflect the current best practices in the Python ecosystem:

| Tool | Role | Rationale |
|---|---|---|
| Black | Code formatting | Zero-configuration, deterministic formatting |
| Ruff | Linting | Fast, comprehensive, replaces multiple tools (flake8, isort, etc.) |
| Pytest | Testing | Flexible, extensible, industry standard |
| GitHub Actions | CI/CD | Native integration, free for public repos |
| Dependabot | Dependency management | Automated security and version updates |

## Future Considerations

As the portfolio grows, the following enhancements are planned:

1. **Documentation site** — Deploy a MkDocs or Sphinx documentation site via GitHub Pages
2. **Package publishing** — Publish the `src/` utilities as a standalone PyPI package
3. **Docker support** — Add Dockerfiles for containerized development and deployment
4. **Pre-commit hooks** — Integrate pre-commit for local development quality gates
