# 开发时间：2023/3/21 22:51

import aircv as ac
from common.tools import get_project_path, sep


class FindImg:
    def ing_imread(self, img_path):
        '''
        读取图片
        :param img_path:
        :return:
        '''
        # return ac.imread(img_path)
        return "D:/code/trading_system_autotest/img/assert_img/head_img.png"
    def get_confidence(self, source_path, search_path):
        '''
        查找图片
        :param source_path:原图路径
        :param search_path:需要查找的图片路径
        :return:
        '''
        img_src = self.ing_imread(source_path)
        img_sch = self.ing_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        return result["confidence"]
