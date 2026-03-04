"""Tests for the shared utility functions."""

from __future__ import annotations

import json

import pytest

from src.utils import (
    file_checksum,
    flatten_dict,
    read_json,
    slugify,
    timestamp_now,
    truncate,
    write_json,
)


class TestSlugify:
    """Tests for the slugify function."""

    def test_basic_string(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self):
        assert slugify("Hello, World! How's it going?") == "hello-world-hows-it-going"

    def test_multiple_spaces(self):
        assert slugify("too   many   spaces") == "too-many-spaces"

    def test_leading_trailing_whitespace(self):
        assert slugify("  padded  ") == "padded"

    def test_underscores(self):
        assert slugify("snake_case_string") == "snake-case-string"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_already_slugified(self):
        assert slugify("already-a-slug") == "already-a-slug"


class TestReadWriteJson:
    """Tests for JSON read/write functions."""

    def test_write_and_read(self, tmp_path):
        filepath = tmp_path / "test.json"
        data = {"key": "value", "number": 42}
        write_json(filepath, data)
        result = read_json(filepath)
        assert result == data

    def test_write_creates_parent_dirs(self, tmp_path):
        filepath = tmp_path / "nested" / "dir" / "test.json"
        write_json(filepath, {"test": True})
        assert filepath.exists()

    def test_read_nonexistent_file(self):
        with pytest.raises(FileNotFoundError):
            read_json("/nonexistent/path/file.json")

    def test_read_invalid_json(self, tmp_path):
        filepath = tmp_path / "invalid.json"
        filepath.write_text("not valid json")
        with pytest.raises(json.JSONDecodeError):
            read_json(filepath)

    def test_unicode_content(self, tmp_path):
        filepath = tmp_path / "unicode.json"
        data = {"greeting": "Hello, World! — 你好世界"}
        write_json(filepath, data)
        result = read_json(filepath)
        assert result == data


class TestTimestampNow:
    """Tests for the timestamp_now function."""

    def test_returns_string(self):
        result = timestamp_now()
        assert isinstance(result, str)

    def test_contains_utc_offset(self):
        result = timestamp_now()
        assert "+00:00" in result

    def test_iso_format(self):
        result = timestamp_now()
        assert "T" in result


class TestFileChecksum:
    """Tests for the file_checksum function."""

    def test_sha256_checksum(self, tmp_path):
        filepath = tmp_path / "test.txt"
        filepath.write_text("hello world")
        checksum = file_checksum(filepath)
        assert isinstance(checksum, str)
        assert len(checksum) == 64  # SHA-256 produces 64 hex characters

    def test_md5_checksum(self, tmp_path):
        filepath = tmp_path / "test.txt"
        filepath.write_text("hello world")
        checksum = file_checksum(filepath, algorithm="md5")
        assert len(checksum) == 32  # MD5 produces 32 hex characters

    def test_nonexistent_file(self):
        with pytest.raises(FileNotFoundError):
            file_checksum("/nonexistent/file.txt")

    def test_unsupported_algorithm(self, tmp_path):
        filepath = tmp_path / "test.txt"
        filepath.write_text("test")
        with pytest.raises(ValueError, match="Unsupported hash algorithm"):
            file_checksum(filepath, algorithm="invalid_algo")


class TestTruncate:
    """Tests for the truncate function."""

    def test_short_string_unchanged(self):
        assert truncate("short", max_length=100) == "short"

    def test_exact_length_unchanged(self):
        assert truncate("exact", max_length=5) == "exact"

    def test_long_string_truncated(self):
        result = truncate("a very long string", max_length=10)
        assert len(result) == 10
        assert result.endswith("...")

    def test_custom_suffix(self):
        result = truncate("a very long string", max_length=10, suffix="~")
        assert result.endswith("~")
        assert len(result) == 10


class TestFlattenDict:
    """Tests for the flatten_dict function."""

    def test_flat_dict_unchanged(self):
        data = {"a": 1, "b": 2}
        assert flatten_dict(data) == {"a": 1, "b": 2}

    def test_nested_dict(self):
        data = {"a": {"b": 1, "c": {"d": 2}}}
        expected = {"a.b": 1, "a.c.d": 2}
        assert flatten_dict(data) == expected

    def test_custom_separator(self):
        data = {"a": {"b": 1}}
        assert flatten_dict(data, separator="/") == {"a/b": 1}

    def test_empty_dict(self):
        assert flatten_dict({}) == {}

    def test_mixed_types(self):
        data = {"a": {"b": [1, 2, 3], "c": "text"}}
        expected = {"a.b": [1, 2, 3], "a.c": "text"}
        assert flatten_dict(data) == expected
