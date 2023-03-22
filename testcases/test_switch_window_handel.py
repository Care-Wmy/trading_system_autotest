# 开发时间：2023/3/16 22:32

from time import sleep

import allure
from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LonginPage
from common.report_add_img import add_img_2_report

class TestWindowHandel:
    @allure.description("窗口句柄测试")
    # allurl功能菜单中显示
    @allure.epic("窗口句柄一级目录")
    @allure.feature("窗口句柄二级目录")
    @allure.story("窗口句柄三级目录")
    @allure.tag("窗口句柄tag描述")
    def test_switch_window_handles(self, driver):
        # driver = DriverConfig().driver_config()
        with allure.step("登录"):
            LonginPage().login(driver, "jay")
            sleep(3)
            # 对步骤截图操作
            add_img_2_report(driver,"登录")
        # 点击一级菜单外链
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(1)
            add_img_2_report(driver,"点击外链")

        # 切换句柄
        with allure.step("断言title"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("title", title)
            assert title == "慕课网-程序员的梦工厂"
        # driver.quit()
