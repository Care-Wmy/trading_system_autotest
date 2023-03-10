# 开发时间：2023/3/2 22:51

from base.loginBase import LoginBase

class LonginPage(LoginBase):
    def login_input_value(self, driver,input_placeholder,input_value):
        '''
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        '''
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self,driver,button_name):
        '''
        点击登录
        :param driver:
        :param button_name:
        :return:
        '''
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()
