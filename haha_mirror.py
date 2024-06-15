"""
@File  :haha_mirror.py
@Author:chenyihan
@Date  :2024/6/15 13:41
@Desc  :哈哈镜算法实现，对图像进行拉伸变换
"""
import cv2
import numpy
import math


def haha_mirror(image,radius):
    h,w,c = image.shape
    center_x = w/2
    center_y = h/2
    result = image.copy()
    for i in range(h):
        for j in range(w):
            tx = j - center_x
            ty = i - center_y
            distance = tx*tx+ty*ty
            if distance < radius*radius:
                newx = int(tx/2 * (math.sqrt(distance) / radius) + center_x)
                newy = int(ty/2 * (math.sqrt(distance) / radius) + center_y)
                if newx >=0 and newx < w and newy >=0 and newy < h:
                    result[i,j] = image[newy,newx]
    return result


if __name__ == '__main__':
    image = cv2.imread('face2.jpg')
    out = haha_mirror(image,250)
    cv2.imshow('out',out)
    cv2.waitKey()
