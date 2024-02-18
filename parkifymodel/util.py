import joblib
from skimage.transform import resize
import numpy as np
import cv2

EMPTY=True
NOT_EMPTY = False

MODEL = joblib.load('parking_model.pkl')

def is_car_there(spot_bgr):
    flat_data =[]
    try:
        img_resized = resize(spot_bgr,(15,15,3))
        
        # cv2.imshow('window2',img_resized)
        # cv2.resizeWindow('window2', 500,500)

        # if cv2.waitKey(10000) & 0xFF == ord('q'):
        #     return    
        flat_data.append(img_resized.flatten())
        
        flat_data = np.array(flat_data)
        # print(flat_data)
        y_pred = MODEL.predict(flat_data)
    
        # print(y_pred)
        # print(y_pred)
        if y_pred == 0:
            return EMPTY
        else:
            return NOT_EMPTY
    
    except Exception as e:
        print("Error occurred during resizing:", e)
        return NOT_EMPTY
    

def get_parking_spots(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components

    slots = []
    coef = 1
    for i in range(1, totalLabels):

        # Now extract the coordinate points
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)

        slots.append([x1, y1, w, h])

    return slots


# def check_color(space_img, target_color, threshold=50):
    
#     space_img = cv2.convertScaleAbs(space_img)
#     # Convert the image to HSV
#     hsv_image = cv2.cvtColor(space_img, cv2.COLOR_BGR2HSV)

#     # Calculate histogram
#     histogram = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])

#     # Find the bin with the highest frequency
#     dominant_color_bin = np.argmax(histogram)

#     # Convert the dominant color bin to the corresponding hue value
#     dominant_hue = int(dominant_color_bin * 180 / 179)

#     # Convert the target color to HSV
#     target_color_hsv = np.array([[target_color]], dtype=np.uint8)
#     target_color_hsv = cv2.cvtColor(target_color_hsv, cv2.COLOR_BGR2HSV)
#     target_hue = target_color_hsv[0][0][0]

#     # Check if the dominant hue is within a threshold of the target hue
#     if abs(dominant_hue - target_hue) <= threshold:
#         return True
#     else:
#         return False
