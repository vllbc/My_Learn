import csv
import json

fp_csv = open("csvtable.csv","r")
fp_json = open("res.json","w",encoding="utf-8")
reader = csv.DictReader(fp_csv)
res = json.dumps(list(reader),ensure_ascii=False)
fp_json.write(res)
fp_json.close()
fp_csv.close()