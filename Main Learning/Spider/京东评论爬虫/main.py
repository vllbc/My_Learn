import time
import requests
import csv
import re
import json

fp = open("data.csv", "w", newline="")
writer = csv.writer(fp)
writer.writerow(["商品名称", "商品类型", "用户名", "用户等级", "PLUS会员", "评论ID", "评论内容", "评分", "点赞数", "回复数", "购买时间", "评论时间", "图片数量", "视频数量", "追评内容", "追评时间", "追评图片数量", "追评天数"])

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", 
    "referer" : "https://item.jd.com/100008210432.html?cu=true&utm_source=c.mktdatatech.com&utm_medium=tuiguang&utm_campaign=t_16282_173261509&utm_term=87df2ba2d557476ab503726ef0669ff4"
}

url = "https://club.jd.com/comment/productPageComments.action"

params = [{
"callback": "fetchJSON_comment98",
"productId": "100008210432", # 商品ID
"score": 0, # 评分
"sortType": 6, 
"page": i, # 当前页数
"pageSize": 10, # 每一页的评论数
"isShadowSku": 0,
"rid": 0,
"fold": 1
} for i in range(100)]

for page, param in enumerate(params):
    r = requests.get(url, params=param).text
    js = json.loads(re.search(r'(?<=fetchJSON_comment98\().*(?=\);)',r).group(0))["comments"]
    for i, j in enumerate(js):
        referenceName = j["referenceName"] # 商品名称
        productColor = j["productColor"] # 购买的商品类型
        nickname = j["nickname"] # 用户名
        userClient = j["userClient"] # 用户等级
        plusAvailable = int(j["plusAvailable"]) 
        plusAvailable = "是" if plusAvailable > 200 else "否" # 是否是plus会员
        id = j["id"] # 评论id
        content = j["content"] # 评论内容
        score = j["score"] # 评分
        vote = j["usefulVoteCount"] # 点赞数
        replyCount = j["replyCount"] # 回复数   
        referenceTime = j["referenceTime"] # 购买时间
        creationTime = j["creationTime"] # 评论时间
        if "imageCount" in j.keys():
            images_num = j["imageCount"] # 图片数量
        else:
            images_num = 0
        if "videos" in j.keys():
            videos_num = len(j["videos"]) # 视频数量
        else:
            videos_num = 0
        if "afterUserComment" in j.keys(): # 如果有追评
            afterUserComment = j["afterUserComment"]["content"] # 追评内容
            afterUserDate = j["afterUserComment"]["created"] # 追评时间
        else:
            afterUserComment = ""
            afterUserDate = ""
        if "afterImages" in j.keys(): # 如果有追评图片
            afterImagesCount = len(j["afterImages"]) # 追评图片数量
        else:
            afterImagesCount = 0
        afterDays = j["afterDays"] # 追评天数

        writer.writerow([referenceName, productColor, nickname, userClient, plusAvailable, id, content, score, vote, replyCount, referenceTime, creationTime, images_num, videos_num, afterUserComment, afterUserDate, afterImagesCount, afterDays])
        print(f"第{page}页第{i+1}条评论...." + "已保存")
        time.sleep(0.1)


