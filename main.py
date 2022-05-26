import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from bs4 import BeautifulSoup
import requests

formClass = uic.loadUiType("./MainUI.ui")[0]

class MyApp(QMainWindow,formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.crawlBtn.clicked.connect(self.crawlStart)

    def crawlStart(self):
        url = self.webSiteName.toPlainText()
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')

        tag1 = self.tag1.toPlainText()
        att1 = self.att1.toPlainText()
        value1 = self.value1.toPlainText()

        st = "{},{{}:{}}".format(tag1, att1, value1)
        items = soup.find_all(st)
        print(items.text)

        # for item in items:
        #     para2 = self.att2.toPlainText()
        #     res = item.find(para2).text
        #     self.crawlResult.appendPlainText(res)
        #     print(res)

        # self.crawlResult.appendPlainText(items.text)
        # for page in range(1,30):
        #     response = requests.get(url+str(page), verify=False)
        #     soup = BeautifulSoup(response.content, 'html.parser')
        #
        #     para1 = self.att1.toPlainText()
        #     items = soup.find_all(para1)
        #
        #     self.crawlResult.appendPlainText("========="+str(page)+"==========")
        #
        #     for item in items:
        #         para2 = self.att2.toPlainText()
        #         res = item.find(para2).text
        #         self.crawlResult.appendPlainText(res)
        #         print(res)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()