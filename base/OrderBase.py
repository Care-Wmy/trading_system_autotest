# 开发时间：2023/3/16 22:49


class OrderBase:
    def order_tab(self, tab_name):
        '''
        已买到宝贝tab按钮
        :param tab_name:全部、待付款、待发货、运输中、待确认、待评价
        :return:
        '''
        return "//div[@role='tab' and text()='" + tab_name + "']"
