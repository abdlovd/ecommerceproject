from unittest.mock import patch, mock_open

from src.read_file import read_file


def test_read_file(category):
    with patch("builtins.open", mock_open(read_data="[]")):
        assert read_file("data") == []