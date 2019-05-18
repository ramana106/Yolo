import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'top': 175, 'left': 20, 'width': 1010, 'height': 325}

sct = mss()
co = 0
while (co < 50):
    print co
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    cv2.imwrite('./out/{}.jpg'.format(str(co)), np.array(img, dtype='uint8'))
    co += 1
