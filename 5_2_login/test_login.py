# 开发时间：2023/2/28 22:48

from time import sleep
# 用来启动浏览器的
from config.driver_config import DriverConfig

# 实例化
driver = DriverConfig().driver_config()
# 打开系统
driver.get("http://www.tcpjwtester.top")
sleep(3)
# 输入用户名
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(3)
# 输入密码
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
sleep(3)
# 点击登录
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(3)
# 成功后退出浏览器
driver.quit()