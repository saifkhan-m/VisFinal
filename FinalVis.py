from matplotlib import pyplot as plt
import cv2
import Utils
import MarchingSquares
import numpy as np

img = cv2.imread('Mars_MGS_MOLA_DEM_mosaic_global_1024.jpg',0)#mars_mercator_2_512x512
#img = cv2.imread('mars_mercator_2_512x512.png',0)
plt.imshow(img)
totalBins=16
#plt.show()
quantizedImage=Utils.binImage(img,totalBins)
#cv2.imshow('image',quantizedImage)
marchedImage=MarchingSquares.marchingSquares(quantizedImage,2)

quantizedImageRGB = cv2.cvtColor(marchedImage,cv2.COLOR_GRAY2RGB)
shadedImage=Utils.shadeImage1(quantizedImageRGB,marchedImage,totalBins)
#hist = cv2.calcHist([quantizedImage], [0], None, [256], [0, 256])
cv2.imwrite('Elevation Map '+str(totalBins)+'.png',shadedImage)

plt.imshow(cv2.cvtColor(shadedImage, cv2.COLOR_BGR2RGB))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#cv2.imshow('image',shadedImage)

#cv2.imshow('image',shadedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()