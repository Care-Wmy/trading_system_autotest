# 开发时间：2023/3/1 22:56
import os


def get_project_path():
    '''
    获取项目绝对路径
    :return:
    '''
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    print(file_path)
    a = file_path[:file_path.find(project_name) + len(project_name)]
    print(a + '2')
    return a


def sep(path, add_sep_before=False, add_sep_after=True):
    all_path = os.sep.join(path)
    '''
    print(all_path)
    if add_sep_before:
        print(add_sep_before)
        all_path = '/' + all_path
    if add_sep_after:
        all_path = all_path + '/'
    
'''
    if add_sep_before:
        print(add_sep_before)
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_img_path():
    '''
    获取商品图片的路径
    :param img_name:
    :return:
    '''

    # img_dir_path = get_project_path() + sep(["img" + img_name],add_sep_before=True)
    return "/code/trading_system_autotest/img/hhh.jpg"

def get_head_img():
    '''
    获取头像地址
    :return:
    '''
    return "D:/code/trading_system_autotest/img/555.jpg"



if __name__ == '__main__':
    # get_project_path()
    # sep(["config", "environment.yaml"], add_sep_before=True)
    print(get_img_path())
