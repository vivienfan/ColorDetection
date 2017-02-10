# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:10:53 2017

@author: shang
"""

# Pyramid
# Color detect

import cv2
import numpy as np
#import matplotlib.pyplot as plt

def Pyramid(img):
    height, width, channels = img.shape

    # 4x4 pixels = 1 block
    new_height = height / 4
    new_width = width / 4
    thumbnail = np.zeros((new_height, new_width, channels), np.uint8)

    # BGR images
    for i in range(0, new_height):
        for j in range(0, new_width):
            blue = img[i*4, j*4, 0]
            green = img[i*4, j*4, 1]
            red = img[i*4, j*4, 2]
            thumbnail[i, j] = (blue, green, red)
    return thumbnail


def ColorDetect(thumbnail):
    height, width, channels = thumbnail.shape
    sum_h = 0
    sum_w = 0
    counter = 0

    for i in range(0, height):
        for j in range(0, width):
            blue = thumbnail[i, j, 0]
            green = thumbnail[i, j, 1]
            red = thumbnail[i, j, 2]
            # color red
            if (0 < blue < 80) and (0 < green < 80) and (150 < red < 256) :
                sum_h += i
                sum_w += j
                counter += 1

    if counter != 0 :
        avg_h = int(round(sum_h / counter))
        avg_w = int(round(sum_w / counter))
    else:
        avg_h = -1
        avg_w = -1

    return avg_h, avg_w


def main():
    img1 = cv2.imread('redball_1.jpg', cv2.IMREAD_COLOR)
    thumbnail1 = Pyramid(img1)
    cv2.imwrite('thumbnail_1.jpg', thumbnail1)
    height1, width1 = ColorDetect(thumbnail1)
    print('thumbnail_1.jpg: height: ' + str(height1) + ' width: ' + str(width1))

    img2 = cv2.imread('redball_2.jpg', cv2.IMREAD_COLOR)
    thumbnail2 = Pyramid(img2)
    cv2.imwrite('thumbnail_2.jpg', thumbnail2)
    height2, width2 = ColorDetect(thumbnail2)
    print('thumbnail_2.jpg: height: ' + str(height2) + ' width: ' + str(width2))
    return


if __name__ == "__main__":
    main()