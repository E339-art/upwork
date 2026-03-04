#!/usr/bin/env bash
# setup.sh — Automated environment setup for the upwork-portfolio project.
#
# Usage:
#   chmod +x scripts/setup.sh
#   ./scripts/setup.sh

set -euo pipefail

PYTHON_MIN_VERSION="3.10"
VENV_DIR=".venv"

echo "================================================"
echo "  Upwork Portfolio — Environment Setup"
echo "================================================"
echo ""

# Check Python version
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo "ERROR: Python 3 is not installed."
        echo "Please install Python ${PYTHON_MIN_VERSION}+ from https://python.org/downloads/"
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo "Found Python ${PYTHON_VERSION}"

    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"; then
        echo "  ✓ Python version meets minimum requirement (${PYTHON_MIN_VERSION}+)"
    else
        echo "  ✗ Python ${PYTHON_MIN_VERSION}+ is required, but found ${PYTHON_VERSION}"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    if [ -d "${VENV_DIR}" ]; then
        echo ""
        echo "Virtual environment already exists at ${VENV_DIR}/"
        echo "  → To recreate, delete it first: rm -rf ${VENV_DIR}"
    else
        echo ""
        echo "Creating virtual environment..."
        python3 -m venv "${VENV_DIR}"
        echo "  ✓ Virtual environment created at ${VENV_DIR}/"
    fi
}

# Install dependencies
install_deps() {
    echo ""
    echo "Installing dependencies..."
    "${VENV_DIR}/bin/pip" install --upgrade pip --quiet
    "${VENV_DIR}/bin/pip" install -r requirements.txt --quiet
    echo "  ✓ Dependencies installed"
}

# Run tests
run_tests() {
    echo ""
    echo "Running test suite..."
    "${VENV_DIR}/bin/python" -m pytest tests/ -v --tb=short
}

# Main
check_python
create_venv
install_deps
run_tests

echo ""
echo "================================================"
echo "  Setup complete!"
echo ""
echo "  Activate the environment:"
echo "    source ${VENV_DIR}/bin/activate"
echo ""
echo "  Available commands:"
echo "    make help     — Show all available commands"
echo "    make lint     — Run linters"
echo "    make test     — Run tests"
echo "    make format   — Auto-format code"
echo "================================================"
