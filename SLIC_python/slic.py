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

image = img_as_float(io.imread('1111.jpg'))

segments = slic(image, 500, 10)
result = mark_boundaries(image, segments)
io.imsave('1111-500.png', result)

