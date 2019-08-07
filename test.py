import cv2
import numpy as np
import Utils
from matplotlib import pyplot as plt

img = cv2.imread('mars_mercator_2_512x512.png', 0)
quantizedImage=Utils.binImage(img)
plt.hist(img.ravel(), 256, [0, 256]);
plt.show()