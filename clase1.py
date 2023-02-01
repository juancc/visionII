"""
Ejercicios de clase 1. Introducción

JCA
"""

import cv2 as cv
import numpy as np

S = 100


def im_1():
    im = np.zeros([100,100])
    for i in range(S): im[i,i] = 255

    cv.imwrite('imagen1.jpg', im)

im_1()