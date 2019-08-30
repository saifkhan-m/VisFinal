import cv2
import numpy as np
import Utils
from matplotlib import pyplot as plt

mat = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
mainoff=2
off=mainoff//2
#print(mat[0:2,0:2])
#print(mat[0:2,2:4])
#print(mat[2:4,0:2])

#print(mat[0:0+off+1,0:0+off+1])
# print(mat[0:0+off+1,mainoff:mainoff+off+1])
# print(mat[0:0+off+1][mainoff:mainoff+off+1])
# print(mat[mainoff:mainoff+off+1,0:0+off+1])
# print(mat[mainoff:mainoff+off+1,mainoff:mainoff+off+1])
for x in (mat[0]):
    for y in (mat[1]):
        print(x,y)
        #marchImage[x][y] = 0



