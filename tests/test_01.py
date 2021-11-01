from pathlib import Path
import pytest
from libcloud.storage.providers import get_driver
from tempfile import TemporaryDirectory


@pytest.fixture
def tmp_directory(fs):
    with TemporaryDirectory() as tmp_dir:
        yield tmp_dir

@pytest.fixture
def fake_libcloud_container(fs, tmp_directory):
    path = tmp_directory
    cls = get_driver('local')
    driver = cls(key=path)
    container_name = 'cont_01'
    cont = driver.create_container(container_name)
    yield driver, cont
    for cont in driver.iterate_containers():
        driver.delete_container(cont)


def test_01(fake_libcloud_container):
    pass
