# 开发时间：2023/3/17 21:57
from time import sleep

from config.driver_config import DriverConfig
from page.IframeBaiduMapPage import IfameBaiduMapPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LonginPage


class TestIframeBaiduMap:

    def test_iframe_baidu_map(self):
        driver = DriverConfig().driver_config()
        LonginPage().login(driver, "william")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"iframe测试")
        sleep(1)

        IfameBaiduMapPage().switch_2_baidu_map_iframe(driver)

        IfameBaiduMapPage().get_baidu_map_search_button(driver)

        IfameBaiduMapPage().iframe_out(driver)

        LeftMenuPage().click_level_one_menu(driver,"首页")
        sleep(3)
        driver.quit()
