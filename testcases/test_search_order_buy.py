# 开发时间：2023/3/16 23:01


from time import sleep

from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LonginPage
from page.OrderPage import OrderPage


class TestOrderBuy:
    def test_order_buy(self):
        driver = DriverConfig().driver_config()
        LonginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for tab in tab_list:
            OrderPage().click_order_tab(driver, tab)
            sleep(2)
        driver.quit()