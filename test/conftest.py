import pytest

from lotterydraft.model import load_from_yaml


@pytest.fixture
def test_data():
    return load_from_yaml("test/test_data.yaml")
