# 开发时间：2023/3/16 21:06

from time import sleep

import pytest

from page.LoginPage import LonginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

goods_info_list = [
    {
        "goods_title": "新增商品测试01",
        "goods_details": "商品详情测试",
        "goods_num": 1,
        # goods_pic_list=["hhh.jpg"],
        "goods_price": 111,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "新增商品测试02",
        "goods_details": "商品详情测试",
        "goods_num": 1,
        # goods_pic_list=["hhh.jpg"],
        "goods_price": 222,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }

]


class TestAddGoods:
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        # driver = DriverConfig().driver_config()
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
            goods_title=goods_info["goods_title"],
            goods_details=goods_info["goods_details"],
            goods_num=goods_info["goods_num"],
            # goods_pic_list=["hhh.jpg"],
            goods_price=goods_info["goods_price"],
            goods_status=goods_info["goods_status"],
            bottom_button_name=goods_info["bottom_button_name"]
        )
        sleep(3)
