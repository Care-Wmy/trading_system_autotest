# 开发时间：2023/3/17 20:43

from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_head_img


class AccountPage(AccountBase, ObjectMap):

    def upload_avatar(self, driver):
        '''
        上传个人图像
        :param driver:
        :return:
        '''
        img_path = get_head_img()
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        '''
        个人资料-点击保存
        :return:
        '''
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)
