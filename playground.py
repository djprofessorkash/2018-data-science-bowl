"""
NAME:           playground.py (2018-data-science-bowl/)
AUTHOR:         Aakash Sudhakar
"""

# ====================================================================================
# ================================ IMPORT STATEMENTS =================================
# ====================================================================================

# import timeit as ti
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy as sp
# import seaborn as sb
# import pandas as pd
from PIL import Image
# from __future__ import with_statement

im = Image.open("files/stage1_train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/images/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9.png")
# im = Image.open("files/stage1_train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks/0adbf56cd182f784ca681396edc8b847b888b34762d48168c7812c79d145aa07.png")

# load the pixel info
pix = im.load()

# get a tuple of the x and y dimensions of the image
width, height = im.size

'''for images'''
with open('train_image_1.csv', 'w+') as f:
    f.write('R, G, B\n')
    # read the details of each pixel and write them to the file
    for y in range(height):
        for x in range(width):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            f.write('{0},{1},{2}\n'.format(r, g, b))

'''only red data'''
with open('train_image_1_red.csv', 'w+') as f:
    for x in range(width):
        if x == width-1:
            f.write('{}\n'.format(x))
        else:
            f.write('{},'.format(x))
    # read the details of each pixel and write them to the file
    for y in range(height):
        for x in range(width):
            red = pix[x, y][0]
            if x == width - 1:
                f.write('{}\n'.format(red))
            else:
                f.write('{},'.format(red))

'''only green data'''
with open('train_image_1_green.csv', 'w+') as f:
    for x in range(width):
        if x == width-1:
            f.write('{}\n'.format(x))
        else:
            f.write('{},'.format(x))
    # read the details of each pixel and write them to the file
    for y in range(height):
        for x in range(width):
            green = pix[x, y][1]
            if x == width - 1:
                f.write('{}\n'.format(green))
            else:
                f.write('{},'.format(green))

'''only blue data'''
with open('train_image_1_blue.csv', 'w+') as f:
    for x in range(width):
        if x == width-1:
            f.write('{}\n'.format(x))
        else:
            f.write('{},'.format(x))
    # read the details of each pixel and write them to the file
    for y in range(height):
        for x in range(width):
            blue = pix[x, y][2]
            if x == width - 1:
                f.write('{}\n'.format(blue))
            else:
                f.write('{},'.format(blue))

'''for masks'''
# with open('masks_image_1_1.csv', 'w+') as f:
#     for x in range(width):
#         if x == width-1:
#             f.write('{}\n'.format(x))
#         else:
#             f.write('{},'.format(x))
#     # read the details of each pixel and write them to the file
#     for y in range(height):
#         for x in range(width):
#             # 0 or 255
#             rgb = pix[x, y]
#             if x == width - 1:
#                 f.write('{}\n'.format(rgb))
#             else:
#                 f.write('{},'.format(rgb))
