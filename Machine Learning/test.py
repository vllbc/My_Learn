import yaml

with open(r"C:\Users\vllbc\Desktop\my_projects\mkdocs.yml",'r',encoding='utf-8') as fp:
    result = fp.read()
    x = yaml.load(result,Loader=yaml.FullLoader)
    print(x)
    x['nav'][0]['首页'] = 'index.md'
    with open(r'C:\Users\vllbc\Desktop\my_projects\mkdocs.yml','w',encoding='utf-8') as fp:
        yaml.dump(x,fp,allow_unicode=True)
    print(x)
