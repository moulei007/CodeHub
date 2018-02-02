# -*- coding:utf-8 -*-
'''
    @Time:2018/2/2
    @Author: moulei
    @Email: 1144545359@qq.com
'''
# import 一些需要的包
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import numpy as np
import cv2
from PIL import Image

image = img_as_float(io.imread('4.jpg'))

segments = slic(image, 2000, 15)
result = mark_boundaries(image, segments)
io.imsave('1111-500.png', result)  # 保存分割后的图片

# 接下来找到每一个单独的超像素块
for (i, segValue) in enumerate(np.unique(segments)):
    # 为每一个segment构造一个mask
    print "[X] inspecting segment %d " % i
    mask = np.zeros(image.shape[:2], dtype="uint8")
    mask[segments == segValue] = 255

    # 显示标注区域
    save_image_arr = cv2.bitwise_and(image, image, mask=mask)
    io.imsave('retina/' + str(i) + '.png', save_image_arr)
    # cv2.imshow("applied", cv2.bitwise_and(image, image, mask=mask))
    # cv2.waitKey(0)
