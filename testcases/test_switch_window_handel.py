# 开发时间：2023/3/16 22:32

from time import sleep

from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LonginPage


class TestWindowHandel:

    def test_switch_window_handles(self,driver):
        # driver = DriverConfig().driver_config()
        LonginPage().login(driver, "jay")
        sleep(3)
        # 点击一级菜单外链
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(1)
        # 切换句柄
        title = ExternalLinkPage().goto_imooc(driver)
        print("title", title)
        # driver.quit()
