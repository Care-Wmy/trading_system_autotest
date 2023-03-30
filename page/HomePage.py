# 开发时间：2023/3/30 22:34


from selenium.webdriver.common.by import By
from base.HomeBase import HomeBase
from base.ObjectMap import ObjectMap

class HomePage(HomeBase,ObjectMap):
    def get_balance(self,driver):
        '''
        获取首页的账户余额
        :param driver:
        :return:
        '''
        balance_xpath = self.user_balance()
        # 获取元素的文本信息  .text
        return self.element_get(driver,By.XPATH,balance_xpath).text

