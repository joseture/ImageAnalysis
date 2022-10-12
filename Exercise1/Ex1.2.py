import numpy as np
from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import pydicom as dicom

#---------------Exercise 22----------------#

# im = io.imread("Exercise1/data/metacarpals.png")

# im = color.gray2rgb(im)
# mask = im > 250
# io.imshow(mask)
# io.show()
# print(im.shape)
# io.imshow(im)
# io.show()


#------------------------------------------#
        #ADVANCED IMAGE VISUALISATION#
#------------------------------------------#

#---------------Exercise 23----------------#

# im = io.imread("Exercise1/data/metacarpals.png")
# io.imshow(im)
# io.show()


# p = profile_line(im, (342, 77), (320, 160))
# plt.plot(p)
# plt.ylabel("Intensity")
# plt.xlabel("Distance along line")
# plt.show()


#---------------Exercise 24----------------#

# in_dir = "Exercise1/data/"
# im_name = "road.png"
# im_org = io.imread(in_dir + im_name)
# im_gray = color.rgb2gray(im_org)
# ll = 200
# im_crop = im_gray[40:40 + ll, 150:150 + ll]
# xx, yy = np.mgrid[0:im_crop.shape[0], 0:im_crop.shape[1]]
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# surf = ax.plot_surface(xx, yy, im_crop, rstride=1, cstride=1, cmap=plt.cm.jet,
# linewidth=0)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()


#------------------------------------------#
            #DICOM images#
#------------------------------------------#

#---------------Exercise 25----------------#

in_dir = "Exercise1/data/"
im_name = "1-442.dcm"
ds = dicom.dcmread(in_dir + im_name)
print(ds)

#---------------Exercise 26----------------#

im = ds.pixel_array

io.imshow(im)
io.show()

print(im.shape)
print(im.dtype)

#---------------Exercise 27----------------#

io.imshow(im, vmin=-1000, vmax=1000, cmap='gray')
io.show()

