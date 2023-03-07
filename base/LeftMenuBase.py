# 开发时间：2023/3/7 21:23

class LeftMenuBase:

    def level_one_menu(self, menu_name):
        '''
        定位一级菜单栏
        :param menu_name: 菜单栏名称
        :return:
        '''
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        '''
        定位二级菜单栏
        :param menu_name: 菜单栏名称
        :return:
        '''
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"

if __name__ == '__main__':
    print(LeftMenuBase().level_two_menu("新增二手商品"))