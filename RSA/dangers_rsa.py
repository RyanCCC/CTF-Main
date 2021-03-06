'''
低加密指数攻击：
所谓低加密指数指的就是e非常小的情况下，通常为3。
这种题目通常有两种类型，一种直接爆破，另外一种是低指数广播攻击。
1.先介绍比较简单的情况。假设e=3, e很小，但是n很大。
回顾RSA加密公式： C=M^e % n (C密文，M明文)

1.当M^e < n 时，
 C = M^e ，所以对C开方就能得到M
1
2
2. 当M^e ＞ n 时，此时用爆破的方法
 假设我们　 Ｍ^e / n 商 k 余数为c，
 所以Ｍ^e  = k*n + C，对K进行爆破，只要k满足 k*n + C能够开方就可以
'''

from gmpy2 import iroot
import libnum
n = 0x52d483c27cd806550fbe0e37a61af2e7cf5e0efb723dfc81174c918a27627779b21fa3c851e9e94188eaee3d5cd6f752406a43fbecb53e80836ff1e185d3ccd7782ea846c2e91a7b0808986666e0bdadbfb7bdd65670a589a4d2478e9adcafe97c6ee23614bcb2ecc23580f4d2e3cc1ecfec25c50da4bc754dde6c8bfd8d1fc16956c74d8e9196046a01dc9f3024e11461c294f29d7421140732fedacac97b8fe50999117d27943c953f18c4ff4f8c258d839764078d4b6ef6e8591e0ff5563b31a39e6374d0d41c8c46921c25e5904a817ef8e39e5c9b71225a83269693e0b7e3218fc5e5a1e8412ba16e588b3d6ac536dce39fcdfce81eec79979ea6872793

c = 0x10652cdfaa6b63f6d7bd1109da08181e500e5643f5b240a9024bfa84d5f2cac9310562978347bb232d63e7289283871efab83d84ff5a7b64a94a79d34cfbd4ef121723ba1f663e514f83f6f01492b4e13e1bb4296d96ea5a353d3bf2edd2f449c03c4a3e995237985a596908adc741f32365

k = 0
while 1:
    res=iroot(c+k*n,3)
    if(res[1]==True):
        print(libnum.n2s(int(res[0])))
        break
    k=k+1