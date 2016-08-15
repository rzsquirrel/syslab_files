import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

#image = cv2.imread("disp5_monopoly.png",1)
image = cv2.imread("white.jpg",1)

cv2.circle(image,(400,40), 3, (0,255,0), -1)

plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])



plt.show()
