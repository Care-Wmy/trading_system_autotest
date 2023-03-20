# 开发时间：2023/3/18 18:07

from time import sleep
import pytest
from config.driver_config import DriverConfig


class TestPytestMClass:

    @pytest.fixture()
    def driver(self):
        getdriver = DriverConfig().driver_config()
        return getdriver

    @pytest.mark.bing
    def test_open_bing(self,driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    # pytest -m baidu 在命令行输入命令 就会运行这个用例
    def test_open_baidu(self,driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self,driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://fanyi.baidu.com")
        sleep(3)
        driver.quit()