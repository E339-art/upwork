# Setup Guide

This guide walks through the complete setup process for local development.

## Prerequisites

Before getting started, ensure the following tools are installed on your system:

| Tool | Minimum Version | Installation |
|---|---|---|
| Python | 3.10+ | [python.org/downloads](https://python.org/downloads/) |
| Git | 2.30+ | [git-scm.com/downloads](https://git-scm.com/downloads) |
| Make | Any | Pre-installed on macOS/Linux; [GnuWin32](http://gnuwin32.sourceforge.net/packages/make.htm) on Windows |

## Step 1: Clone the Repository

```bash
git clone https://github.com/E339-art/upwork.git
cd upwork
```

## Step 2: Create a Virtual Environment

It is strongly recommended to use a virtual environment to isolate project dependencies.

```bash
python -m venv .venv
```

Activate the virtual environment:

| Platform | Command |
|---|---|
| macOS / Linux | `source .venv/bin/activate` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, use the Makefile shortcut:

```bash
make install
```

## Step 4: Verify the Installation

Run the test suite to confirm everything is working:

```bash
make test
```

You should see all tests passing with output similar to:

```
tests/test_utils.py::TestSlugify::test_basic_string PASSED
tests/test_utils.py::TestSlugify::test_special_characters PASSED
...
```

## Step 5: Run Linters

Check that the code meets quality standards:

```bash
make lint
```

## Development Workflow

A typical development session follows this pattern:

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes to the code
3. Format the code: `make format`
4. Run linters: `make lint`
5. Run tests: `make test`
6. Commit and push: `git commit -m "feat: description" && git push`
7. Open a pull request on GitHub

## Troubleshooting

**Python version mismatch:** Ensure you are using Python 3.10 or later. Check with `python --version`.

**Permission errors on install:** If you encounter permission errors, ensure you are working inside the virtual environment (you should see `(.venv)` in your terminal prompt).

**Make not found on Windows:** Install Make via [Chocolatey](https://chocolatey.org/) (`choco install make`) or use the underlying commands directly (see the Makefile for the full commands).
