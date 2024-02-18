import cv2
from skimage import io, color
import sklearn
import pandas
import skimage
import matplotlib
from skimage.transform import resize
import matplotlib.pyplot as plt

from util import  get_parking_spots, is_car_there

mask = 'C:\\Users\\dasak\\HackAi\\ParkingLotAvailability\\parkifymodel\\mask_crop.png'

parking_image_test = 'C:\\Users\\dasak\\HackAi\\ParkingLotAvailability\\parkifymodel\\parkingcrop2.png'
parking_image_test1 = cv2.imread(parking_image_test)

parking_image_test2 = resize(parking_image_test1,(455,380))
mask2 = io.imread(mask,0)

''' now we will use something called connected components,
connected components. It is a mathematical component that says
that if a pixel and another neighboring pixel have the same value
then they are connected. Here we will use this concept to outline
parking lot spaces'''

cc = cv2.connectedComponentsWithStats(mask2, 4, cv2.CV_32S)

parking_spaces = get_parking_spots(cc)

frame = parking_image_test2
    
park_test = parking_spaces[:4]

for space in park_test:
    # cv2.imshow('frame',frame)

    x1,y1,w,h = space
    print(space)
    # print(x1,y1,w,h)
    
    space_img = frame[y1:y1+h, x1:x1+w,:]

    space_status = is_car_there(space_img)
    
    print(space_status)
    if space_status:
        cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),2)
    else:
        cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,0,255),2)
        

cv2.imshow('frame',frame)

cv2.waitKey(0)
    
    
    # ret = False
cv2.destroyAllWindows()
    


