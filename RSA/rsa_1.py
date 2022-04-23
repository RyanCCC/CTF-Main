def getEuler(prime1, prime2):
    return (prime1 - 1) * (prime2 - 1)

def getDkey(e, Eulervalue):  
    k = 1
    while True:
        if (((Eulervalue * k) + 1) % e) == 0:
            (d, m) = divmod(Eulervalue * k + 1, e)
            return d  
        k += 1
def Ming(c, d, n):
    return pow(c, d, n)

if __name__ == '__main__':
    p = 473398607161
    q = 4511491
    d = getDkey(17, getEuler(p, q))
    print('私钥为： %d' % d)