import os
import pyzbar
from PIL import Image

img = './src/QR_code.png'
def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)
    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])

test = decode_qr_code(img)
print(test)


import cv2
d=cv2.QRCodeDetector()
val,_,_ = d.detectAndDecode(cv2.imread('test.jpg'))
print('text is:',val)