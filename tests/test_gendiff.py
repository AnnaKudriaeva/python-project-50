import pytest
from gendiff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.gendiff import find_differences
from gendiff.parser import load_data

@pytest.fixture
def file1_data_json():
    return load_data('tests/fixtures/file1.json')

@pytest.fixture
def file2_data_json():
    return load_data('tests/fixtures/file2.json')

@pytest.fixture
def file1_data_yml():
    return load_data('tests/fixtures/file1.yml')

@pytest.fixture
def file2_data_yml():
    return load_data('tests/fixtures/file2.yml')

def test_generate_diff_yaml(file1_data_yml, file2_data_yml):
    diff = generate_diff(file1_data_yml, file2_data_yml)
    assert diff == find_differences(file1_data_yml, file2_data_yml)

def test_generate_diff(file1_data_json, file2_data_json):
    diff = generate_diff(file1_data_json, file2_data_json)
    assert diff == find_differences(file1_data_json, file2_data_json)

def test_format_stylish(file1_data_json, file2_data_json):
    diff = find_differences(file1_data_json, file2_data_json)
    with open('tests/fixtures/expected_stylish.txt') as f:
        expected_output = f.read().strip()
    assert format_stylish(diff).strip() == expected_output

def test_format_stylish_yml(file1_data_yml, file2_data_yml):
    diff = find_differences(file1_data_yml, file2_data_yml)
    with open('tests/fixtures/expected_stylish.txt') as f:
        expected_output = f.read().strip()
    assert format_stylish(diff).strip() == expected_output

def test_format_plain(file1_data_json, file2_data_json):
    diff = find_differences(file1_data_json, file2_data_json)
    with open('tests/fixtures/expected_plain.txt') as f:
        expected_output = f.read().strip()
    assert '\n'.join(format_plain(diff)).strip() == expected_output

def test_format_plain_yml(file1_data_yml, file2_data_yml):
    diff = find_differences(file1_data_yml, file2_data_yml)
    with open('tests/fixtures/expected_plain.txt') as f:
        expected_output = f.read().strip()
    assert '\n'.join(format_plain(diff)).strip() == expected_output

def test_format_json(file1_data_json, file2_data_json):
    diff = find_differences(file1_data_json, file2_data_json)
    with open('tests/fixtures/expected_json.json') as f:
        expected_output = f.read().strip()
    assert format_json(diff) == expected_output

def test_format_json_yml(file1_data_yml, file2_data_yml):
    diff = find_differences(file1_data_yml, file2_data_yml)
    with open('tests/fixtures/expected_yml.json') as f:
        expected_output = f.read().strip()
    assert format_json(diff) == expected_output