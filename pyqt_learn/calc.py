import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class My_blog_control(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.commit_btn = QPushButton("确定")
        # self.commit_btn.clicked.connect(sys.exit)
        self.cel_btn = QPushButton("退出")

        grid = QGridLayout()
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        position = [(i,j) for i in range(5) for j in range(4)]
        for positi,name in zip(position,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*positi)

        self.setLayout(grid)
        # self.setGeometry(300, 300, 850, 520)
        self.move(300,150)
        self.setWindowTitle("MY_BLOG_CONTROL")
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mbc = My_blog_control()
    sys.exit(app.exec_())