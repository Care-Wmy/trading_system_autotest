# 开发时间：2023/3/16 22:54

from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase

class OrderPage(ObjectMap,OrderBase):

    def click_order_tab(self,driver,tab_name):
        '''
        点击订单tab栏按钮
        :param driver:
        :param tab_nam:
        :return:
        '''
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver,By.XPATH,tab_xpath)
