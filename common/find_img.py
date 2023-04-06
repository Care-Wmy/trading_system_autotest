# 开发时间：2023/3/21 22:51

import aircv as ac
from common.tools import get_project_path, sep, get_now_date_time_str
from common.report_add_img import add_img_path_2_report

import cv2


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
        # 对原图画框
        cv2.rectangle(
            img_src,
            result["rectangle"][0],
            result["rectangle"][3],
            (255, 0, 0), 2
        )
        # 保存图片
        diff_img_path = get_project_path() + sep(
            ["img", "diff_img",
             get_now_date_time_str() + "-对比的图.png"]
            , add_sep_before=True)
        cv2.imencode(".png", img_src)[1].tofile(diff_img_path)
        add_img_path_2_report(diff_img_path, "查找到的图")
        return result["confidence"]
