# 开发时间：2023/3/27 22:34

import ddddocr


class OcrIdentify:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    # 打开要识别的图片
    def identify(self, pic_path):
        with open(pic_path, "rb") as f:
            image = f.read()
        # 识别图片
        res = self.ocr.classification(image)
        return res


if __name__ == '__main__':
    print(OcrIdentify().identify("test11.png"))