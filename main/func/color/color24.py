import cv2
import numpy as np
import os

try :
    from Tool import *
except BaseException:
    from func.color.Tool import *

def makeColor(basepath):
    # 材质存储位置
    basepath += R"\resources\assets\fcbm\textures\blocks"

    size = 16
    img = np.ones((size,size),dtype=np.uint8)
    bgr_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    # 24位色生成 共 16,777,216‬ 种，慎用
    for r in range(256):
        for g in range(256):
            for b in range(256):
                bgr_img[:,:,0] = r
                bgr_img[:,:,1] = g
                bgr_img[:,:,2] = b
                colorstring = rgb(r,g,b)
                name = basepath + R"\rgb_" + colorstring + ".png"
                cv2.imwrite(name,bgr_img)