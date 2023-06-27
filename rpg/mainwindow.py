from PyQt5.QtWidgets import QMainWindow
from rpg.util import ADTPATH
from rpg.ui.ui_mainwindow import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.loadCmd()
        self.pushButton_exec.clicked.connect(self.website)
        self.pushButton_create.clicked.connect(self.create)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_save.clicked.connect(self.save)
        self.lineEdit_command.returnPressed.connect(self.create)
        self.listWidget.itemClicked.connect(self.send)
        self.listWidget.itemDoubleClicked.connect(self.delete)
        filePath = os.path.join(ADTPATH, 'tool/information.txt')
        with open(filePath, 'r', encoding='utf-8-sig') as f:
            (self.url, self.channel, self.account, self.pw) = [
                _.split('=')[1].strip() for _ in f]

    def loadCmd(self):
        filePath = os.path.join(ADTPATH, 'tool/commandSet.txt')
        with open(filePath, 'r', encoding='utf-8-sig') as f:
            self.listWidget.addItems([_.rstrip('\n') for _ in f])
        self.driver = None

    def inputPassword(self):
        try:
            self.driver.find_element(
                By.XPATH, "//input[contains(@aria-label, '電子郵件或電話號碼')]").send_keys(self.account)
            time.sleep(0.1)
            self.driver.find_element(
                By.XPATH, "//input[contains(@aria-label, '密碼')]").send_keys(self.pw)
            time.sleep(0.1)
            self.driver.find_element(
                By.XPATH, "//button[contains(@type, 'submit')]").click()
            # self.driver.find_element(
            #     By.XPATH, "//div[contains(@aria-label, '隱藏成員名單')]").click()
        except:
            pass

    def website(self):
        url = self.url
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option(
            "excludeSwitches", ['enable-automation'])
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        service = ["hide_console"]
        self.driver = webdriver.Chrome(ChromeDriverManager().install(
        ), chrome_options=chrome_options, service_args=service)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        self.inputPassword()

    def close(self):
        if self.driver.session_id != None:
            self.driver.quit()
            self.driver.session_id = None

    def create(self):
        if self.lineEdit_command.text() == '':
            return
        else:
            newCmd = self.lineEdit_command.text()
            self.listWidget.addItem(newCmd)
            self.lineEdit_command.setText('')

    def send(self):
        try:
            line = self.driver.find_element(
                By.XPATH, "//div[contains(@aria-label, '傳訊息到 " + self.channel + "')]")
            line.send_keys(Keys.CONTROL, 'a')
            time.sleep(0.1)
            line.send_keys(Keys.DELETE)
            sendCmd = self.listWidget.currentItem().text()
            line.send_keys("<@555955826880413696> "+sendCmd)
            line.send_keys(Keys.ENTER)
        except:
            print("Runtime error")

    def delete(self):
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        item = None

    def save(self):
        try:
            list_widget = self.listWidget
            filePath = os.path.join(ADTPATH, 'tool/commandSet.txt')
            entries = '\n'.join(list_widget.item(ii).text()
                                for ii in range(list_widget.count()))
            with open(filePath, 'w', encoding='utf-8-sig') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file commandSet.txt could not be written")
