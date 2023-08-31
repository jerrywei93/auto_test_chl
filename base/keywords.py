import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 项目名称
pro_name = 'Auto_Key'

# 项目根路径
root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)).split(pro_name)[0], pro_name)

# Chrome驱动路径
driver_path = os.path.join(root_path, 'chromedriver.exe')
S = Service(executable_path=driver_path)

browser_type = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'ie': webdriver.Ie
}


# 创建指定浏览器对象
def browser(type_):
    try:
        return getattr(webdriver, type_)(service=S)
    except:
        return webdriver.Chrome(service=S)


class UnSupportBrowserTypeError(object):
    pass


class KeyUI:
    """
    关键字驱动类，封装常用的操作方法
    """
    # 初始化浏览器，封装浏览器操作方法
    def __init__(self, type='Chrome'):
        # self._type = type.lower()
        # if self._type in browser_type:
        #     self.browser = browser_type[self._type]
        # else:
        #     raise UnSupportBrowserTypeError
        # # self.driver = self.browser()
        # self.driver = webdriver.Chrome(service=S)

        self.driver = browser(type)

    def open_browser(self, type='Chrome'):
        self._type = type
        return self.driver

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def locate(self, name, value):
        return self.driver.find_element(name, value)

    def click(self, name, value):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located([name, value]))
        self.locate(name, value).click()

    def input(self, name, value, text):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located([name, value]))
        self.locate(name, value).send_keys(text)

    def wait(self, value):
        time.sleep(int(value))

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    key = KeyUI('Chrome')
    # key.open_browser()

    key.open('https://www.baidu.com/')
    key.input('id', 'kw', 'pytest搜索')
    key.click('id', 'su')
    key.wait(5)

    # key.open('http://10.13.4.31:8810/#/login')
    # key.input('xpath', '//*[@id="app"]/div/div[2]/div/form/div[2]/div/div[1]/input', 'guanli')
    # key.input('xpath', '//*[@id="app"]/div/div[2]/div/form/div[3]/div/div/input', 'chl123456')
    # key.click('xpath', '//*[@id="app"]/div/div[2]/div/form/div[4]/div/button')
    # key.wait(5)

