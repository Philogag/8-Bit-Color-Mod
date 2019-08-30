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

    # 256色配色方案 // 实际为216种(历史遗留问题)
    ls = [0x00,0x33,0x66,0x99,0xcc,0xff]
    for r in ls:
        for g in ls:
            for b in ls:
                bgr_img[:,:,0] = r
                bgr_img[:,:,1] = g
                bgr_img[:,:,2] = b
                colorstring = rgb(r,g,b)
                name = basepath + R"\rgb_" + colorstring + ".png"
                cv2.imwrite(name,bgr_img)