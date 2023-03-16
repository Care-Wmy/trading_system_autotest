# 开发时间：2023/3/16 21:06

from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LonginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods_001(self):
        driver = DriverConfig().driver_config()
        # 登录
        LonginPage().login(driver, "jay")
        # 点击一级菜单
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        # 点击二级菜单
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title="新增商品测试11",
            goods_details="商品详情测试",
            goods_num=1,
            # goods_pic_list=["hhh.jpg"],
            goods_price=123,
            goods_status="上架",
            bottom_button_name="提交"
        )
        sleep(3)
        driver.quit()
