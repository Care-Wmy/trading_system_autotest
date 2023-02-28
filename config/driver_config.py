# 开发时间：2023/2/28 22:49


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# from common.tools import get_project_path, sep


class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                                      latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                                      cache_valid_range=365).install(),
                                  options=options)
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver