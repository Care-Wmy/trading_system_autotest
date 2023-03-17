# 开发时间：2023/3/17 20:34

class AccountBase:
    def basic_info_avatar_input(self):
        '''
        基本资料-个人头像
        :return:
        '''
        return "//input[@type='file']"

    def basic_info_save_button(self):
        '''
        基本资料-保存按钮
        :return:
        '''
        return "//span[text()='保存']/parent::button"