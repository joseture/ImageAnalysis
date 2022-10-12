import numpy as np
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import pydicom as dicom

#---------------Exercise 2----------------#


# Directory containing data and images
in_dir = "Exercise1/data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

print(im_org.shape)

print(im_org.dtype)


#---------------Exercise 3----------------#

# io.imshow(im_org)
# plt.title('Metacarpal image')
# io.show()

#---------------Exercise 4----------------#

# io.imshow(im_org, cmap="terrain")
# plt.title('Metacarpal image (with colormap)')
# io.show()

#---------------Exercise 5----------------#

# io.imshow(im_org, vmin = 20, vmax = 170)
# plt.title('Gray level scale')
# io.show()

#---------------Exercise 6----------------#

# io.imshow(im_org, vmin = 127, vmax = 128)
# plt.title('b&W')
# io.show()

#---------------Exercise 7----------------#

# plt.hist(im_org.ravel(), bins=256)
# plt.title('Image histogram')
# io.show()

#h is a tuple containing the count fo pixels and the value of the edges

# h = plt.hist(im_org.ravel(), bins=256)
# bin_no = 100
# count = h[0][bin_no]
# print(f"There are {count} pixel values in bin {bin_no}")

# bin_left = h[1][bin_no]
# bin_right = h[1][bin_no + 1]
# print(f"Bin edges: {bin_left} to {bin_right}")


#---------------Exercise 8----------------#

#y, x, _ = plt.hist(im_org.ravel(), bins=256)

#print(max(y))


#---------------Exercise 9----------------#

r = 100
c = 90
im_val = im_org[r, c]
print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")

#---------------Exercise 10----------------#

# im_org[:30] = 0
# io.imshow(im_org)
# io.show()

#---------------Exercise 11----------------#

# mask = im_org > 150
# io.imshow(mask)
# io.show()

# im_org[mask] = 255
# io.imshow(im_org)
# io.show()


#------------------------------------------#
            #COLOR IMAGES#
#------------------------------------------#

#---------------Exercise 12----------------#

im_name2 = "ardeche.jpg"
im_col = io.imread(in_dir + im_name2)
io.imshow(im_col)
io.show()


