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

plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()

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
# io.show()
print(im_col.shape)

print(im_col.dtype)


#---------------Exercise 13----------------#
r = 110
c = 90
im_col[:300, :]  =[0, 255, 0]
# io.imshow(im_col)
# io.show()

#---------------Exercise 14----------------#
im_name3 = "Exercise1\photo.jpg"
im_me = io.imread(im_name3)
print("este es antes", im_me.shape)

# io.imshow(im_me)
# io.show()

# im_rescaled = rescale(im_me, 0.25, anti_aliasing=True, channel_axis=2)
# io.imshow(im_rescaled)
# io.show()
# print(im_rescaled.shape)
# print(im_rescaled[50][50])

# im_resized = resize(im_me, (im_me.shape[0] // 4, im_me.shape[1] // 6))
# io.imshow(im_resized)
# io.show()
#print("etse es el nuevo", im_resized.shape)

#---------------Exercise 15----------------#
# shape = im_me.shape
# print(shape[1])
# scale = 400/shape[1]
# print(scale)
# im_rescaled = rescale(im_me, scale, anti_aliasing=True, channel_axis=2)
# print(im_rescaled.shape)

#---------------Exercise 16----------------#

im_gray = color.rgb2gray(im_me)
print(im_gray.dtype)
im_byte = img_as_ubyte(im_gray)
print(im_byte.dtype)

#---------------Exercise 17----------------#

# plt.hist(im_me.ravel(), bins=256)
# plt.title('Image histogram')
# io.show()

#---------------Exercise 18----------------#





#------------------------------------------#
            #COLOR CHANNELS#
#------------------------------------------#

# im_name4 = "Exercise1\data\DTUSign1.jpg"
# im_dtu = io.imread(im_name4)
# io.imshow(im_dtu)
# io.show()


# fig, axes = plt.subplots(1, 3, figsize = (8, 4))
# ax = axes.ravel()

# r_comp = im_dtu[:, :, 0]
# ax[0].imshow(r_comp)

# g_comp = im_dtu[:, :, 1]
# ax[1].imshow(g_comp)

# b_comp = im_dtu[:, :, 2]
# ax[2].imshow(b_comp)

# fig.tight_layout()
# plt.show()



#------------------------------------------#
            #SIMPLE IMAGE MANIPULATIONS#
#------------------------------------------#


#---------------Exercise 20----------------#

im_name4 = "Exercise1\data\DTUSign1.jpg"
im_dtu = io.imread(im_name4)
im_dtu[500:1000, 800:1500, :] = 0

io.imshow(im_dtu)
# io.show()

io.imshow(im_dtu)
io.show()

io.imsave("Exercise1\data\DTU.jpg", im_dtu)
#---------------Exercise 21----------------#



