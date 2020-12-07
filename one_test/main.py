import os
import sys
import yaml
import shutil
messge = ''
with open(r"config.yml",'r',encoding='utf-8') as fp:
    res = fp.read()
    data = yaml.load(res,Loader=yaml.FullLoader)
    mkdocs_yaml = data['mkdocs_yaml']
    mkdocs_work = data['mkdocs_work_folder']
    githubpage = data['githubpage_folder']
with open(mkdocs_yaml,'r',encoding='utf-8') as fp:
    result = fp.read()
    data = yaml.load(result,Loader=yaml.FullLoader)
    print("注意在执行前要确保单词拼对，而且有对应文件!!!!!")
    clas = input("是否为新文件?(yes/no>>>")
    if clas == "yes":
        while True:
            types = input("输入要加入的类型>>>")
            names = input("请输入名字>>>")
            dirs = input("输入文件的路径>>>")
            messge = input("提交信息>>>")
            if input("检查是否有错误(yes/no)>>>") == 'yes':
                continue
            else:
                break
        for index,name in enumerate(data['nav']):
            if name.get(types):
                data['nav'][index][types].append({names:dirs})
        with open(mkdocs_yaml,'w',encoding='utf-8') as fp:
            yaml.dump(data,fp,allow_unicode=True)
    else:
        messge = input("输入提交信息>>>")
os.system(f"cd {mkdocs_work} && mkdocs build --clean")
#替换文件
def copyFiles(sourceDir,targetDir):
    if sourceDir.find("exceptionfolder")>0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,file)
        targetFile = os.path.join(targetDir,file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) !=
 os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
                print(targetFile+ " copy succeeded")
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)
copyFiles(f"{mkdocs_work}\site",githubpage)
if messge != "":
    os.system(f'cd {githubpage} && git add . && git commit -m "{messge}" && git push origin master')
print("all works OK!!")




