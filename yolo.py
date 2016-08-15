import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy
image = cv2.imread("wide.png",1)
plt.subplot(121),plt.imshow(image,cmap = 'cool')
plt.title('Image'), plt.xticks([]), plt.yticks([])
plt.show()
