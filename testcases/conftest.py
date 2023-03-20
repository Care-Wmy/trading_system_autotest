# 开发时间：2023/3/20 21:45

import pytest

from config.driver_config import DriverConfig

@pytest.fixture()
def driver():
    getdriver = DriverConfig().driver_config()
    yield getdriver
    getdriver.quit()