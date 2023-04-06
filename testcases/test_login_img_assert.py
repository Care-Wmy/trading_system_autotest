# 开发时间：2023/3/21 23:48

import pytest
from time import sleep
import allure

from page.LoginPage import LonginPage
from common.report_add_img import add_img_2_report

class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        '''
        登录后断言图片
        :param driver:
        :return:
        '''
        with allure.step("登录"):
            LonginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver,"登录")
        with allure.step("断言图片"):
            assert LonginPage().login_assert(driver, "head_img.png") > 0.9
