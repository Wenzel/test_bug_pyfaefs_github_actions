from pathlib import Path
import pytest

@pytest.fixture
def fake_fs_01(fs):
    path = '/toto'
    p = Path(path)
    p.mkdir(parents=True)
    yield path
    p.rmdir()

def test_01(fake_fs_01):
    pass
