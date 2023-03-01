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
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=True):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    sep(["config", "environment.yaml"], add_sep_before=True)
