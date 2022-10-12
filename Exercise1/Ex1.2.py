import numpy as np
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import pydicom as dicom

#---------------Exercise 22----------------#

im = io.imread("Exercise1/data/metacarpals.png")

im = color.gray2rgb(im)
mask = im > 250
io.imshow(mask)
io.show()
# print(im.shape)
# io.imshow(im)
# io.show()


