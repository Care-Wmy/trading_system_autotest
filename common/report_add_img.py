# 开发时间：2023/3/22 21:59

from time import sleep

import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    '''
    截图并插入allure报告
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    '''
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)
