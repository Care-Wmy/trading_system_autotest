# 开发时间：2023/3/7 22:23

import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class ObjectMar:
    def element_get(self, driver, locate_type, locator_expresson, timeout=10, must_be_visible=False):
        '''
        单个元素获取
        :param driver:浏览器驱动法
        :param locate_type:定位方式类型
        :param locator_expresson:定位表达式
        :param timeout:超时时间
        :param must_be_visible:元素是否必须可见 True是必须可见 false是默认值
        :return:返回的元素
        '''
        # 设置开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expresson)
                #     如果元素不是必须可见的就直接返回元素
                if not must_be_visible:
                    return element
                #     如果元素必须是可见的，则需要先判断元素是否可见
                else:
                    # is_displayed() 这个方法是判断元素是否可见
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位表达式：" + locator_expresson)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        '''
        等待页面完全加载完成
        :param driver:浏览器驱动
        :param timeout:超时时间
        :return:
        '''
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("return document.readyState")

            except WebDriverException:
                # 如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            #     如果页面元素全部加载完成返回true
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.tzset(0.1)
        raise Exception("打开网页时，页面元素在%s秒后仍然没有完全加载完成" % timeout)