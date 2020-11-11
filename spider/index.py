import requests
import json
import time

params={
    'account':"18265090197",
    'password':"xwh5201314",
    "phoneVersion":19,
    "platform":1,
    "deviceCode":355757010701395,
    "versionNumber":"9.4.0",
    "channel":"ppMarket",
    "phoneBrand":"samsung",
    "phoneModel":"SM-G955F"
}
res =requests.post("http://120.55.151.61/V2/StudentSkip/loginCheckV4.action",params)
# ids = res.headers['Set-Cookie'].strip().split(";")
# print(ids[2].strip().split(",")[1].split("=")[1])
# print(ids[0].split("=")[1])
# for i in res.headers['Set-Cookie'].strip().split(";"):
#     print(i.strip())
urls = "http://120.55.151.61/V2/Course/getCourseTableFromServer.action"
hearders = {
    'JSESSIONID':res.headers['Set-Cookie'].strip().split(";")[0].split("=")[1],
    'SERVERID':res.headers['Set-Cookie'].strip().split(";")[2].strip().split(",")[1].split("=")[1]
}
paramss = {
    "platform":1,
    "versionNumber":"9.4.0",
    "channel":"ppMarket",
    "phoneBrand":"samsung",
    "phoneModel":"SM-G955F",
    'term':1,
    'beginYear':2020,
    "phoneVersion":19
}
ress = requests.post(urls,json=paramss,headers=hearders)
print(ress.text)