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

![image](../src/cryptography/164894593-e537dd40-83ee-4a4f-9c34-747c40cac937.png)


### 手机九宫格解码：

![image](../src/cryptography/179184599-3cb0e915-0029-45cf-a2d2-315b712e55ca.png)


### 猪圈密码

![image](../src/cryptography/179659502-8c19d41a-00c2-4c46-9c8f-184b8890f26b.png)

