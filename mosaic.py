"""
@File  :mosaic.py
@Author:chenyihan
@Date  :2024/6/15 14:37
@Desc  :图像打马赛克
"""
import cv2
import numpy as np
import random


def mosaic(image, patch_size, mode=1):
    h, w = image.shape[:2]
    half_patch = patch_size // 2
    result = image.copy()
    for i in range(half_patch, h - 1 - half_patch, patch_size):
        for j in range(half_patch, w - 1 - half_patch, patch_size):
            if mode == 1:
                k1 = random.random() - 0.5
                k2 = random.random() - 0.5
                i1 = int(i + k1 * (patch_size)) % h
                j1 = int(j + k2 * (patch_size)) % w
                result[i - half_patch:i + half_patch, j - half_patch:j + half_patch] = image[i1, j1]
            if mode == 2:
                result[i - half_patch:i + half_patch, j - half_patch:j + half_patch] = image[i, j]
            if mode == 3:
                x = np.arange(patch_size)
                y = np.arange(patch_size)
                np.random.shuffle(x)
                np.random.shuffle(y)
                for i1 in range(-half_patch, half_patch):
                    for j1 in range(-half_patch, half_patch):
                        result[i + i1, j + j1] = image[
                            i + y[i1 + half_patch] - half_patch, j + x[j1 + half_patch] - half_patch]

    return result


if __name__ == '__main__':
    image = cv2.imread('face2.jpg')
    out = mosaic(image, 20, 1)
    cv2.imwrite('out.png', out)
    # cv2.waitKey()
