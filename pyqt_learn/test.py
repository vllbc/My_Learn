import os
import sys
import yaml
import shutil
import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger('my_test')


parser = argparse.ArgumentParser()
parser.add_argument('-new', type=str,help='是否为新文件')
parser.add_argument('-type', type=str,help='类型')
parser.add_argument('-name', type=str,help='名字')
parser.add_argument('-folder', type=str,help='路径')
parser.add_argument('-messege', type=str,help='提交信息')
args = parser.parse_args()
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
    clas = args.new
    if clas == "yes":
        types = args.type
        names = args.name
        dirs = args.folder+'.md'
        messge = args.messege
    else:
        messge = args.messege
        os.system(f"cd {mkdocs_work} && mkdocs build --clean")
        copyFiles(f"{mkdocs_work}\site",githubpage)
        if messge != "":
            os.system(f'cd {githubpage} && git add . && git commit -m "{messge}" && git push origin master')
            print("all works OK!!")
            sys.exit()
    for index,name in enumerate(data['nav']):
        if name.get(types):
            print('ok')
            data['nav'][index][types].append({names:dirs})
    with open(mkdocs_yaml,'w',encoding='utf-8') as fp:
        yaml.dump(data,fp,allow_unicode=True)


os.system(f"cd {mkdocs_work} && mkdocs build --clean")
#替换文件


copyFiles(f"{mkdocs_work}\site",githubpage)
if messge != "":
    os.system(f'cd {githubpage} && git add . && git commit -m "{messge}" && git push origin master')
print("all works OK!!")