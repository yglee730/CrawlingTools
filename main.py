import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from bs4 import BeautifulSoup
import requests

import pandas as pd

formClass = uic.loadUiType("./MainUI.ui")[0]

class MyApp(QMainWindow,formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.crawlBtn.clicked.connect(self.crawlStart)
        self.defaultBtn.clicked.connect(self.default)
        self.saveBtn.clicked.connect(self.save)

    def crawlStart(self):
        url = self.webSiteName.toPlainText()
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        tag1 = self.tag1.toPlainText()
        att1 = self.att1.toPlainText()
        value1 = self.value1.toPlainText()

        items = soup.find_all(tag1,{att1:value1})

        for item in items:
            # print(item.text)
            self.crawlResult.appendPlainText(item.text)

    def default(self):
        self.crawlResult.clear()

    def save(self):
        ans = self.crawlResult.toPlainText()
        fileName = self.pathBtn.toPlainText()

        ansPd = pd.Series(ans.split("\n"))
        # print(type(ans))
        # print(ansPd)

        ansPd.to_csv(fileName,encoding='utf-8-sig')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()