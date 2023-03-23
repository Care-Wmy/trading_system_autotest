# 开发时间：2023/3/2 23:06

from time import sleep

import allure
import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LonginPage
from common.report_add_img import add_img_2_report

class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self,driver):
        '''使用错误的账号登录'''

        with allure.step("登录"):
            LonginPage().login(driver,"aaa")
            sleep(3)
            add_img_2_report(driver,"登录")