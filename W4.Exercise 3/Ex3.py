import cv2
import numpy as np
from skimage import color, io
import matplotlib.pyplot as plt

from skimage.util import img_as_float
from skimage.util import img_as_ubyte
from skimage.filters import threshold_otsu

path = "Exercise 3/data/"

img = io.imread(path + "vertebra.png")

#-------------------- Threshold --------------------#
# ret, thres = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# io.imshow(thres)
# io.show() 

#-------------------- Histogram --------------------#
# plt.hist(img.ravel(), bins=256)
# plt.title('Image histogram')
# io.show()

print(img.dtype)
min = np.min(img)
max = np.max(img)

print("UNIT8. Min value:", min, "Max value:", max)

#-------------------- img_as_float --------------------#
img_float = img_as_float(img)
min = np.min(img_float)
max = np.max(img_float)

print("FLOAT. Min value:", min, "Max value:", max)

#-------------------- img_as_float --------------------#
img_ubyte = img_as_ubyte(img_float)
min = np.min(img_ubyte)
max = np.max(img_ubyte)

print("UBYTE. Min value:", min, "Max value:", max)

#------------------------------------------------------#
#----------------- HISTOGRAM STRTCHING ----------------#
#------------------------------------------------------#

def histogram_stretch(img_in):
    """
    Stretches the histogram of an image 
    :param img_in: Input image
    :return: Image, where the histogram is stretched so the min values is 0 and the maximum value 255
    """
    # img_as_float will divide all pixel values with 255.0
    img_float = img_as_float(img_in)
    min_val = img_float.min()
    max_val = img_float.max()
    min_desired = 0.0
    max_desired = 1.0
	
    # Do something here
    
    num = max_desired - min_desired
    den = max_val - min_val
    
    img_out = (num/den)*(img_float - min_val) + min_desired

    # img_as_ubyte will multiply all pixel values with 255.0 before converting to unsigned byte
    return img_as_ubyte(img_out)

img_out = histogram_stretch(img)

# f, axarr = plt.subplots(2)
# axarr[0].imshow(img)
# axarr[1].imshow(img_out)
# plt.show()

min = np.min(img_out)
max = np.max(img_out)

print("HISTOGRAM. Min value:", min, "Max value:", max)

#------------------------------------------------------#
#----------------- HISTOGRAM STRTCHING ----------------#
#------------------------------------------------------#

def gamma_map(img, gamma):
    
    img_float = img_as_float(img)
    img_out = np.power(img_float, gamma)
    return img_as_ubyte(img_out)

img_gamma = gamma_map(img, 10)

# f, axarr = plt.subplots(2)
# axarr[0].imshow(img)
# axarr[1].imshow(img_gamma)
# plt.show()

#------------------------------------------------------#
#----------------- IMAGE SEGMENTATION -----------------#
#------------------------------------------------------#

def threshold_image(img_in, thres):
    
    img_out = img_in > thres
    return img_as_ubyte(img_out)

img_thres = threshold_image(img, 50)
# f, axarr = plt.subplots(2)
# axarr[0].imshow(img)
# axarr[1].imshow(img_thres)
# plt.show()

#------------------------------------------------------#
#-------------------- OTSU'S METHOD -------------------#
#------------------------------------------------------#

thres_new = threshold_otsu(img)
img_otsu = threshold_image(img, thres = thres_new)
img_otsu = img_as_ubyte(img_otsu)

print(img_otsu.dtype)

# f, axarr = plt.subplots(nrows=1, ncols = 2, figsize = (12, 5))
# axarr[0].imshow(img)
# axarr[1].imshow(img_otsu)
# plt.show()

#------------------------------------------------------#
#-------------------- Exercise 12 ---------------------#
#------------------------------------------------------#

photo = io.imread(path + "dark_background.png")
photo_gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY).astype(np.float32)
photo_bin = threshold_image(photo_gray, 20)

# f, axarr = plt.subplots(nrows=1, ncols = 2, figsize = (12, 5))
# axarr[0].imshow(photo)
# axarr[1].imshow(photo_bin)
# plt.show()


#------------------------------------------------------#
#-------------------- Exercise 13 ---------------------#
#------------------------------------------------------#

im_org = io.imread(path + "DTUSigns2.jpg")

def detect_dtu_signs(im_org, color):
    
    r_comp = im_org[:, :, 0]
    g_comp = im_org[:, :, 1]
    b_comp = im_org[:, :, 2] 
     
    if (color == 'blue'):
        segm = (r_comp < 10) & (g_comp > 85) & (g_comp < 105) & \
                (b_comp > 180) & (b_comp < 200)
    
    if (color == 'red'):            
        segm = (r_comp > 140) & (r_comp < 210) & (b_comp < 70) & (g_comp < 70)
    
    return segm

segm_blue = detect_dtu_signs(im_org, "blue")
                
# f, axarr = plt.subplots(nrows=1, ncols = 2, figsize = (12, 5))
# axarr[0].imshow(im_org)
# axarr[1].imshow(segm_blue)
# plt.show()

#------------------------------------------------------#
#----------------- Exercise 14 & 15 -------------------#
#------------------------------------------------------#

def hsv(im_org, img_hsv):
    
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 2))
    ax0.imshow(im_org)
    ax0.set_title("RGB image")
    ax0.axis('off')
    ax1.imshow(img_hsv)
    ax1.set_title("Hue channel")
    ax1.axis('off')
    fig.tight_layout()
    io.show()
    
def detect_dtu_signs_hsv(im_org, col):
    
    hsv_img = color.rgb2hsv(im_org)
    h_comp = hsv_img[:, :, 0]
    s_comp = hsv_img[:, :, 1]
    v_comp = hsv_img[:, :, 2]
    
    if (col == 'blue'):
        segm = (h_comp < 0.6) & (h_comp > 0.4) & (v_comp < 0.77) & (v_comp > 0.7) 
    
    if (col == 'red'):            
        segm = (h_comp < 1.0) & (h_comp > 0.9)
    
    return segm

    
# img_hsv = detect_dtu_signs_hsv(im_org, "red")
# hsv(im_org, img_hsv)
