import numpy as np 
import cv2


def get_limits(color):

    c =np.uint8([[color]]) # Here Insert the BGR Values which you want to convert to HSV
    hsvc = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    LowerLimit = hsvc[0][0][0] - 10, 100, 100
    UpperLimit = hsvc[0][0][0] + 10, 255, 255

    LowerLimit = np.array(LowerLimit, dtype=np.uint8)
    UpperLimit = np.array(UpperLimit, dtype=np.uint8)

    return LowerLimit, UpperLimit
