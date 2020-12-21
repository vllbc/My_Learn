import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import yaml
config = {
    '算法相关':'sf',
    'Python':'python',
    'Cookbook':'Cookbook',
    '爬虫':'spider',
    'Pandas':'pandas',
    'Pytorch':'pytorch',
    'AI学习':'AI_learn',
    'flask':"flask",
    '其他':'others'
}
with open(r"config.yml",'r',encoding='utf-8') as fp:
    res = fp.read()
    data = yaml.load(res,Loader=yaml.FullLoader)
    mkdocs_yaml = data['mkdocs_yaml']
    mkdocs_work = data['mkdocs_work_folder']
    githubpage = data['githubpage_folder']
    

# def copyFiles(sourceDir,targetDir):
#     if sourceDir.find("exceptionfolder")>0:
#         return
#     for file in os.listdir(sourceDir):
#         sourceFile = os.path.join(sourceDir,file)
#         targetFile = os.path.join(targetDir,file)
#         if os.path.isfile(sourceFile):
#             if not os.path.exists(targetDir):
#                 os.makedirs(targetDir)
#             if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) !=
#  os.path.getsize(sourceFile))):
#                 open(targetFile, "wb").write(open(sourceFile, "rb").read())
#                 print(targetFile+ " copy succeeded")
#         if os.path.isdir(sourceFile):
#             copyFiles(sourceFile, targetFile)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):  #控件函数
        self.cb=QComboBox()
        self.cb.addItem("请选择类型")
        self.cb.addItem("算法相关")
        self.cb.addItem("Python")
        self.cb.addItem("Cookbook")
        self.cb.addItem("爬虫")
        self.cb.addItem("Pandas")
        self.cb.addItem("AI学习")
        self.cb.addItem("flask")
        self.cb.addItem("其他")
        self.cb.activated.connect(self.showfolder)
        #标签
        self.is_new = QLabel('是否为新文件')
        self.types = QLabel('类型')
        self.name = QLabel('名字')
        self.folder = QLabel('路径')
        self.message = QLabel('提交信息') 
        #文本框
        self.isnewEdit = QLineEdit()
        self.nameEdit = QLineEdit()
        # self.folderEdit = QLineEdit()
        self.cbfolder = QComboBox()
        self.messageEdit = QTextEdit()
        #按钮
        self.commit_but = QPushButton('确认提交')
        self.commit_but.clicked.connect(self.mains)
        #布局
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.is_new, 1, 0)
        grid.addWidget(self.isnewEdit, 1, 1)


        grid.addWidget(self.types, 2, 0)
        grid.addWidget(self.cb,2,1)
        # grid.addWidget(typeEdit, 2, 1)
    
        grid.addWidget(self.name, 3, 0)
        grid.addWidget(self.nameEdit, 3, 1)
        
        grid.addWidget(self.folder,4,0)
        grid.addWidget(self.cbfolder,4,1)

        grid.addWidget(self.message,5,0)
        grid.addWidget(self.messageEdit,5,1)

        grid.addWidget(self.commit_but)

        self.setLayout(grid) 
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('MY_BLOG_SERVER')
        self.show()
        
    def mains(self):
        is_new = self.isnewEdit.text()
        types = self.cb.currentText()
        name = self.nameEdit.text()
        folder = self.cbfolder.currentText()  
        message = self.messageEdit.toPlainText()
        print(type(name),type(folder))
        # with open(mkdocs_yaml,'r',encoding='utf-8') as fp:
        #     result = fp.read()
        #     data = yaml.load(result,Loader=yaml.FullLoader)
        #     if is_new != 'yes':
        #         os.system(f"cd {mkdocs_work} && mkdocs build --clean")
        #         copyFiles(f"{mkdocs_work}\site",githubpage)
        #         if message != "":
        #             os.system(f'cd {githubpage} && git add . && git commit -m "{message}" && git push origin master')
        #             QMessageBox.information("所有工作完成!")
        #             sys.exit()
        #     if is_new == 'yes':
        #         for index,name in enumerate(data['nav']):
        #             if name.get(types):
        #                 data['nav'][index][types].append({name:folder})
        # with open(mkdocs_yaml,'w',encoding='utf-8') as fp:
        #     yaml.dump(data,fp,allow_unicode=True)
        # os.system(f"cd {mkdocs_work} && mkdocs build --clean")
        # copyFiles(f"{mkdocs_work}\site",githubpage)
        # if message != "":
        #     os.system(f'cd {githubpage} && git add . && git commit -m "{message}" && git push origin master')
        # QMessageBox.information("所有工作完成!")

    def showfolder(self):
        self.cbfolder.addItem("请选择文件")
        docs_folder = mkdocs_yaml.strip('mkdocs.yml')+f'docs/{config[self.cb.currentText()]}'
        for file in os.listdir(docs_folder):
            self.cbfolder.addItem(file)
if  __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())