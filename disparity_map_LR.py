import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('literally_their_left.png',0)
imgR = cv2.imread('literally_their_right.png',0)
#stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
#stereo = cv2.StereoBM(ndisparities=24, SADWindowSize=15)
#stereo = cv2.StereoBM(ndisparities=16, blockSize=15)
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()

