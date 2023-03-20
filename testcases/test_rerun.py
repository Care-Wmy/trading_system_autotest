# 开发时间：2023/3/20 23:36
import random


class TestRerun:
    def test_terun(self):
        num = random.randint(1,3)
        print("num",num)
        if num !=1:
            print("失败")
            raise Exception("出错了")
        else:
            return True