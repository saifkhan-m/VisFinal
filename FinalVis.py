from matplotlib import pyplot as plt
import cv2
import Utils
import MarchingSquares

def initVis(img,totalBins):
    quantizedImage=Utils.binImage(img,totalBins)
    marchedImage=MarchingSquares.marchingSquares(quantizedImage,2)
    quantizedImageRGB = cv2.cvtColor(marchedImage,cv2.COLOR_GRAY2RGB)
    shadedImage=Utils.shadeImage1(quantizedImageRGB,marchedImage,totalBins)

    return shadedImage


img = cv2.imread('Mars_MGS_MOLA_DEM_mosaic_global_1024.jpg',0)
#img = cv2.imread('mars_mercator_2_512x512.png',0)
totalBins=16
shadedImage=initVis(img,totalBins)
cv2.imwrite('Elevation Map '+str(totalBins)+'.png',shadedImage)

plt.imshow(cv2.cvtColor(shadedImage, cv2.COLOR_BGR2RGB))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#cv2.imshow('image',shadedImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()