import cv2
import numpy as np
print(cv2.__version__)

img = cv2.imread('mars_mercator_2_512x512.png',1)
print(len(img))
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
print(np.shape(img))
max=-1
min=300
for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(3):
            if img[i][j][k]>max:
                max=img[i][j][k]
            if img[i][j][k]<min:
                min=img[i][j][k]


for i in range(40,100):
    for j in range(40,100):
        img[i][j]=[155, 100, 155]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img[1][1])
print('max : ',max)
print('min : ',min)


# def marchingSquares(image, lim):
#     marchImage = copy.deepcopy(image)
#     off = lim / 2
#     for i in range(image - lim / 2):
#         for j in range(image[0]):
#             changeDict, changeFlag = marchCase(
#                 {1: [i for i in image[i][j]], 2: image[i][j + off], 3: image[i + off][j], 4: image[i + off][j + off]})
#
#
# def makeDict(image, i, j, off, index):
#     if index == 1:
#
#         for x in range(i, i + off):
#             for y in range(j, j + off):