from unittest.mock import patch, mock_open

from src.read_file import read_file, create_object_from_json


def test_read_file(category):
    with patch("builtins.open", mock_open(read_data="[]")):
        assert read_file("data") == []

def test_create_object_from_json(read_json_file):
    assert create_object_from_json(read_json_file)[0].name == 'Смартфоны'
