# 开发时间：2023/3/7 19:23

class HomeBase:
    '''
    contains方法的作用查找属性中包含元素  模糊查询的意思
    '''
    def wallet_switch(self):
        '''
        首页的钱包开关定位
        :return:
        '''
        return "//span[contains(@class,'switch')]"

    def logo(self):
        '''
        进入系统后，首页左上角的logo
        :return:
        '''
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        '''
        定位首页 ‘欢迎您回来’
        :return:
        '''
        return "//span[starts-with(text(),'欢迎您回来')]"