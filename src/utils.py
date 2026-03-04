"""Shared utility functions for common operations across projects."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug.

    Args:
        text: The input string to convert.

    Returns:
        A lowercase, hyphen-separated slug string.

    Example:
        >>> slugify("Hello World! This is a Test")
        'hello-world-this-is-a-test'
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def read_json(filepath: str | Path) -> dict[str, Any]:
    """Read and parse a JSON file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        Parsed JSON content as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    path = Path(filepath)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filepath: str | Path, data: dict[str, Any], indent: int = 2) -> None:
    """Write data to a JSON file.

    Args:
        filepath: Path to the output JSON file.
        data: Dictionary to serialize as JSON.
        indent: Number of spaces for indentation (default: 2).
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
        f.write("\n")


def timestamp_now() -> str:
    """Return the current UTC timestamp in ISO 8601 format.

    Returns:
        A string like '2026-03-03T12:00:00+00:00'.
    """
    return datetime.now(timezone.utc).isoformat()


def file_checksum(filepath: str | Path, algorithm: str = "sha256") -> str:
    """Calculate the checksum of a file.

    Args:
        filepath: Path to the file.
        algorithm: Hash algorithm to use (default: 'sha256').

    Returns:
        Hexadecimal checksum string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the algorithm is not supported.
    """
    if algorithm not in hashlib.algorithms_available:
        msg = f"Unsupported hash algorithm: {algorithm}"
        raise ValueError(msg)

    h = hashlib.new(algorithm)
    path = Path(filepath)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate a string to a maximum length with a suffix.

    Args:
        text: The input string.
        max_length: Maximum allowed length including suffix.
        suffix: String to append when truncating.

    Returns:
        The truncated string, or the original if within limits.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def flatten_dict(
    data: dict[str, Any], parent_key: str = "", separator: str = "."
) -> dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary.

    Args:
        data: The nested dictionary to flatten.
        parent_key: Prefix for keys (used in recursion).
        separator: Separator between nested keys.

    Returns:
        A flattened dictionary with dot-separated keys.

    Example:
        >>> flatten_dict({"a": {"b": 1, "c": {"d": 2}}})
        {'a.b': 1, 'a.c.d': 2}
    """
    items: list[tuple[str, Any]] = []
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, separator).items())
        else:
            items.append((new_key, value))
    return dict(items)
