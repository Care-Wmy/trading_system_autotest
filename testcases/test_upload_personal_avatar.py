# 开发时间：2023/3/17 20:59
from time import sleep

from config.driver_config import DriverConfig
from page.AccountPage import  AccountPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LonginPage

class TestPersonalInfo:

    def test_upload_personal_avatar(self):
        driver = DriverConfig().driver_config()
        LonginPage().login(driver,"william")
        LeftMenuPage().click_level_one_menu(driver,"账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver)
        sleep(3)
        AccountPage().click_save(driver)
        sleep(3)
        driver.quit()

