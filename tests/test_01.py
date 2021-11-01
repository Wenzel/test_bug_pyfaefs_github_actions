from pathlib import Path

import pytest
from libcloud.storage.providers import get_driver
from contextlib import contextmanager
from tempfile import TemporaryDirectory

@pytest.fixture
def tmp_dir():
    with TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@contextmanager
def libcloud_driver(tmp_dir: Path):
    """Initializes libcloud with the local provider (filesystem) creates a container and yield"""
    cls = get_driver('local')
    driver = cls(key=str(tmp_dir))
    container_name = 'cont_01'
    driver.create_container(container_name)
    try:
        yield driver
    finally:
        for cont in driver.iterate_containers():
            driver.delete_container(cont)


@pytest.fixture
def libcloud_driver_fake_fs(fs, tmp_dir):
    """Initializes libcloud based on the fake filesystem PyFakeFS"""
    with libcloud_driver(tmp_dir) as driver:
        yield driver


@pytest.fixture
def libcloud_driver_normal_fs(tmp_dir):
    with libcloud_driver(tmp_dir) as driver:
        yield driver


def test_fake_fs(libcloud_driver_fake_fs):
    pass


def test_no_fake_fs(libcloud_driver_normal_fs):
    pass