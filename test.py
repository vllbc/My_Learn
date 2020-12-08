import argparse
parser =  argparse.ArgumentParser()
parser.add_argument('-new', type=str,help='是否为新文件')
parser.add_argument('-type', type=str,help='类型')
parser.add_argument('-folder', type=str,help='路径')
parser.add_argument('-messege', type=str,help='提交信息')
args = parser.parse_args()

#打印姓名
if args.new == 'yes':
    print(args.type,args.folder,args.messege)