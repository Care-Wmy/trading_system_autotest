# 开发时间：2023/3/30 22:42

from time import sleep

import allure

from common.mysql_operate import MysqlOperate
from page.LoginPage import LonginPage
from page.HomePage import HomePage
from logs import log


class TestMysqlConn:
    def test_mysql(self, driver):
        with allure.step("登录"):
            LonginPage().login(driver, "jay")
            sleep(3)

        with allure.step("获取账户余额"):
            balance = HomePage().get_balance(driver)
            log.info(balance)

        with allure.step("从MySQL中读取账户余额"):
            sql = "select balance from wallet where user_id=13;"
            db_balance = MysqlOperate().query(sql)[0][0]
            log.info(db_balance)

        with allure.step("断言数据库中的数据是否与页面数据一致"):
            assert str(balance) == str(db_balance)
