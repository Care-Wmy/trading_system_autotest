# 开发时间：2023/3/16 22:28

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        '''
        切换窗口
        :param driver:
        :return:
        '''
        self.switch_window_2_latest_handle(driver)
        return driver.title
