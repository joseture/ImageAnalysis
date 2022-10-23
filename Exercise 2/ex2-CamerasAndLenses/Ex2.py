from cmath import pi
import math
import numpy as np

def pitagoras(a, b):
    tetha = math.atan2(b,a)
    return tetha

# focal length f and an object distance g.
def camera_b_distance(f, g):
    b = 1/(1/f-1/g) 
    return b
    

    
    
# print(pitagoras (10, 3))

todg = pitagoras (10, 3)*180/pi

# print(todg)

# print("camera shit")
# print(camera_b_distance(0.015, 0.1))
# print(camera_b_distance(0.015, 1))
# print(camera_b_distance(0.015, 15))


#--------------- Exercise 3 ---------------#

height = 1.8 # meters
distance = 5 # meters
focal_length = 5e-3 #mm

# 1. A focused image of Thomas is formed inside the camera. At which distance from the lens?

dis = camera_b_distance(focal_length, distance)
print("The distance from the lens is:",dis, "meters")

# 2. How tall (in mm) will Thomas be on the CCD-chip?

tall = (dis * height/distance) * 1e3 

print("Thomas is", tall, " mm in the CCD-chip.")

# 3. What is the size of a single pixel on the CCD chip? (in mm)?

pixel_size = 6.4 / 640

print("Size of the pixel =", pixel_size, "mm")

# 4. How tall (in pixels) will Thomas be on the CCD-chip?

print("Thomas is", tall / pixel_size, "pixels tall on the chip" )

# 5. What is the horizontal field-of-view (in degrees)?

FOV_hor = 2 * math.atan2((6.4e-3/2), focal_length)*180 / pi

print("The horizontal FOV is:", FOV_hor, "degrees")

# 6. What is the vertical field-of-view (in degrees)?

FOV_ver = 2 * math.atan2((4.8e-3/2), focal_length)*180 / pi
print("The vertical FOV is:", FOV_ver, "degrees")
