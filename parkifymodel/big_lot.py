import cv2
from skimage import io, color
import sklearn
import pandas
import skimage
import matplotlib
from skimage.transform import resize
import matplotlib.pyplot as plt
import datetime

from util import  get_parking_spots, is_car_there


mask = 'C:\\Users\\dasak\\HackAi\\ParkingLotAvailability\\parkifymodel\\mask_1920_1080.png'

parking_image_test = 'C:\\Users\\dasak\\HackAi\\ParkingLotAvailability\\parkifymodel\\big_lot.png'
parking_image_test1 = cv2.imread(parking_image_test)

parking_image_test2 = resize(parking_image_test1,(1080,1920))

# import cv2

# Load the image in color
mask2 = cv2.imread(mask)

# Convert the image to grayscale
mask2_gray = cv2.cvtColor(mask2, cv2.COLOR_BGR2GRAY)

# Threshold to create binary image
_, binary_mask = cv2.threshold(mask2_gray, 127, 255, cv2.THRESH_BINARY)

# Perform connected components analysis
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_mask, 4, cv2.CV_32S)


# mask2 = io.imread(mask,0)

# if mask2.shape[2] == 4:  # Check if the image has an alpha channel
#     mask2 = mask2[:, :, :3]  # Remove the alpha channel


# mask2_gray = color.rgb2gray(mask2)



# ''' now we will use something called connected components,
# connected components. It is a mathematical component that says
# that if a pixel and another neighboring pixel have the same value
# then they are connected. Here we will use this concept to outline
# parking lot spaces'''

# # mask2 = cv2.imread('mask2.png', cv2.IMREAD_GRAYSCALE)

# # Threshold to create binary image
# _, binary_mask = cv2.threshold(mask2, 127, 255, cv2.THRESH_BINARY)

# # Perform connected components analysis
# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_mask, 4, cv2.CV_32S)


# cc = cv2.connectedComponentsWithStats(mask2, 4, cv2.CV_32S)
cc = (num_labels, labels, stats, centroids)

parking_spaces = get_parking_spots(cc)
open_space = 0
closed_space =0
frame = parking_image_test2
# frame = parking_image_test1
alpha = .3
# park_test = parking_spaces[:4]

# for space in park_test:
for space in parking_spaces:
    # cv2.imshow('frame',frame)

    x1,y1,w,h = space
    # print(space)
    # print(x1,y1,w,h)
    
    space_img = frame[y1:y1+h, x1:x1+w,:]

    space_status = is_car_there(space_img)
    
    # print(space_status)
    if space_status:
        open_space+=1
        cv2.rectangle(frame,(x1+15,y1),(x1+w+17,y1+h),(0,255,0),2)

        
    else:
        closed_space+=1
        cv2.rectangle(frame,(x1+15,y1),(x1+w+17,y1+h),(0,0,255),1)

total_spaces = open_space+closed_space
window_str = f"Number of Spots Available are : {open_space} / {total_spaces} \n Time: {datetime.datetime.now()}"
org = (50,50)
font = cv2.FONT_HERSHEY_DUPLEX
fontScale = 1
color_of_text = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
cv2.putText(frame, window_str, org, font,  
                   fontScale, color_of_text, thickness, cv2.LINE_AA)

cv2.imshow('frame',frame)
# cv2.imwrite('')

cv2.waitKey(0)
    
    
    # ret = False
cv2.destroyAllWindows()
    


