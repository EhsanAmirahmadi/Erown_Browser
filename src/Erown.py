import os
import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar('Navigation')
        self.addToolBar(navtb)

        back_btn = QAction('◀️',self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setStatusTip('Back to previos page')
        navtb.addAction(back_btn)

        forward_btn = QAction('▶️', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setStatusTip('Forward to next page')
        navtb.addAction(forward_btn)

        reload_btn = QAction('🔃', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setStatusTip('Reload page')
        navtb.addAction(reload_btn)

        home_btn = QAction('🏠', self)
        home_btn.triggered.connect(self.navigate_home)
        home_btn.setStatusTip('go Home')
        navtb.addAction(home_btn)
        navtb.addSeparator

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction('❌', self)
        stop_btn.triggered.connect(self.browser.stop)
        stop_btn.setStatusTip('stop loading currnet page')
        navtb.addAction(stop_btn)

        self.show()

    def update_title(self):
       title = self.browser.page().title()
       self.setWindowTitle('%s - Erown' % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('https')
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)

QApplication.setApplicationName('browser')
window = MainWindow()
app.exec_()