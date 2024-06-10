import json
import pytest
from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.gendiff import find_differences
from gendiff.parser import parse_yaml

@pytest.fixture
def file1_data():
    with open('tests/fixtures/file1.json') as f:
        return json.load(f)

@pytest.fixture
def file2_data():
    with open('tests/fixtures/file2.json') as f:
        return json.load(f)

@pytest.fixture
def file1_data_yaml():
    return parse_yaml('tests/fixtures/file1.yml')

@pytest.fixture
def file2_data_yaml():
    return parse_yaml('tests/fixtures/file2.yml')


def test_generate_diff_yaml(file1_data_yaml, file2_data_yaml):
    diff = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    expected_diff = find_differences(file1_data_yaml, file2_data_yaml)
    assert diff == expected_diff


def test_generate_diff(file1_data, file2_data):
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == find_differences(file1_data, file2_data)

def test_format_stylish(file1_data, file2_data):
    diff = find_differences(file1_data, file2_data)
    with open('tests/fixtures/expected_stylish.txt') as f:
        expected_output = f.read().strip()
    assert format_stylish(diff).strip() == expected_output

def test_format_plain(file1_data, file2_data):
    diff = find_differences(file1_data, file2_data)
    with open('tests/fixtures/expected_plain.txt') as f:
        expected_output = f.read().strip()
    assert '\n'.join(format_plain(diff)).strip() == expected_output

def test_format_json(file1_data, file2_data):
    diff = find_differences(file1_data, file2_data)
    with open('tests/fixtures/expected_json.json') as f:
        expected_output = f.read().strip()
    assert format_json(diff) == expected_output
