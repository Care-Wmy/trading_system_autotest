# 开发时间：2023/3/2 23:06

from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LonginPage

class TestLogin:

    def test_login(self,driver):
        # driver = DriverConfig().driver_config()
        LonginPage().login(driver,"jay")
        sleep(3)
        # # 退出浏览器
        # driver.quit()