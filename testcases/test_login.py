# 开发时间：2023/3/2 23:06

from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LonginPage

class TestLogin:

    def test_login(self):
        driver = DriverConfig().driver_config()
        # 登录系统
        driver.get("http://www.tcpjwtester.top")
        sleep(3)
        # 输入用户名
        LonginPage().login_input_value(driver,"用户名","周杰伦")
        sleep(3)
        # 输入密码
        LonginPage().login_input_value(driver, "密码", "123456")
        sleep(3)
        # 点击登录
        LonginPage().click_login(driver,"登录")
        sleep(3)
        # 退出浏览器
        driver.quit()