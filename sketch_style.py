"""
@File  :sketch_style.py
@Author:chenyihan
@Date  :2024/6/15 14:12
@Desc  :素描效果实现，灰度图与反相图加权融合
"""
import cv2
import numpy as np


def sketch(image, kernel_size):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray1 = 255 - gray  # 反相
    cv2.imshow('gray1', gray1)
    gray1 = cv2.GaussianBlur(gray1, (kernel_size, kernel_size), 0)
    dst = cv2.addWeighted(gray, 0.5, gray1, 0.5, 0)
    return dst


if __name__ == '__main__':
    image = cv2.imread('face2.jpg')
    out = sketch(image, 81)
    cv2.imshow('out', out)
    cv2.waitKey()
