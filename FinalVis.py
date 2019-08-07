import cv2
import Utils
import MarchingSquares
import numpy as np

img = cv2.imread('mars_mercator_2_512x512.png',0)
quantizedImage=Utils.binImage(img)

marchedImage=MarchingSquares.marchingSquares(quantizedImage,2)

quantizedImageRGB = cv2.cvtColor(marchedImage,cv2.COLOR_GRAY2RGB)
shadedImage=Utils.shadeImage(quantizedImageRGB,marchedImage)
hist = cv2.calcHist([quantizedImage], [0], None, [256], [0, 256])
cv2.imshow('image',hist)

#cv2.imshow('image',shadedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()