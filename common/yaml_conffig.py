# 开发时间：2023/3/1 22:25
# 打开文件
import yaml
from common.tools import get_project_path, sep

'''
file = open("/code/trading_system_autotest/config/environment.yaml",encoding="utf-8")
try:
    a = file.read()
    print(a)
except Exception as e:
    print(e)
finally:
    file.close()

with open("/code/trading_system_autotest/config/environment.yaml","r",encoding="utf-8") as file:
    # 对文件进行读取
    a = file.read()
    print(a)
'''


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True),"r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.env["username"], self.env["password"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
