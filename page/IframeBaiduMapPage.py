# 开发时间：2023/3/17 21:51

from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IfameBaiduMapPage(ObjectMap, IframeBaiduMapBase):
    def get_baidu_map_search_button(self, driver):
        '''
        获取百度地区搜索按钮
        :param driver:
        :return:
        '''
        button_xpath = self.search_button()
        return self.element_get(driver, By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self,driver):
        '''
        切换百度地图的iframe
        :param driver:
        :return:
        '''
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_info_iframe(driver,By.XPATH,iframe_xpath)

    def iframe_out(self,driver):
        '''
        从百度地图iframe切回校园二手交易系统
        :param driver:
        :return:
        '''
        return self.switch_from_iframe_to_content(driver)