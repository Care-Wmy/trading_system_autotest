# 开发时间：2023/3/21 23:48

import pytest
from time import sleep

from page.LoginPage import LonginPage


class TestLoginAssert:
    @pytest.mark.login
    def test_login_assert(self, driver):
        '''
        登录后断言图片
        :param driver:
        :return:
        '''
        LonginPage().login(driver, "william")
        sleep(3)
        assert LonginPage().login_assert(driver, "head_img.png") > 0.9
