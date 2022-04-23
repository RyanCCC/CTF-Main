import binascii
# decode
s1 = b'6e6f784354467b57333163306d335f37305f4368316e343730776e7d'
print(binascii.a2b_hex(s1).decode())

# encode
h = binascii.b2a_hex(s1)
print(h)