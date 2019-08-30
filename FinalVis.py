from matplotlib import pyplot as plt
import cv2
import Utils
import MarchingSquares

@Utils.timing
def initVis(img,totalBins,cellSize):
    quantizedImage=Utils.binImage(img,totalBins)
    marchedImage=MarchingSquares.marchingSquares(quantizedImage,cellSize)
    quantizedImageRGB = cv2.cvtColor(marchedImage,cv2.COLOR_GRAY2RGB)
    shadedImage=Utils.shadeImage(quantizedImageRGB,marchedImage,totalBins)

    return shadedImage


img = cv2.imread('Mars_MGS_MOLA_DEM_mosaic_global_1024.jpg',0)
#img = cv2.imread('mars_mercator_2_512x512.png',0)
while(1):
    print('############################################################')
    print('############################################################')
    print("Program to generate Elevation Map. Press CTRL+C to exit")
    print("Enter the size of cells: 1 or 2")
    cell=int(input())
    if cell not in [1,2]:
        print("Please enter cell size either 1 or 2.  Press CTRL+C to exit")
        continue
    print("Enter the number of color bins : 2 or 4 or 8 or 16")
    bin = int(input())
    if bin not in [2,4,8,16]:
        print("Please enter number of bins in [2,4,8,16].  Press CTRL+C to exit")
        continue
    print('You chose the cofiguration as cell={} and bin={}'.format(cell,bin))
    shadedImage=initVis(img,bin,cell)
    filename='Elevation_Map_of_cellsize_{}_and_{}_bins.png'.format(cell, bin)
    print(filename, 'written successfully' )
    cv2.imwrite(filename,shadedImage)

# shadedImage=initVis(img,16,1)
# plt.imshow(cv2.cvtColor(shadedImage, cv2.COLOR_BGR2RGB))
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

#cv2.imshow('image',shadedImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()