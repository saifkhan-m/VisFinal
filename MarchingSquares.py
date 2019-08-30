import copy
import numpy as np
def marchingSquares(image,cellSize):
    marchImage=copy.deepcopy(image)
    off=int(cellSize/2)
    for i in range(0,len(image)-cellSize-2,cellSize):
        for j in range(0,len(image[0])-cellSize-2,cellSize):
            checkDict = {1: image[i:i+off+1,j:j+off+1],
                         2: image[i:i+off+1,j+cellSize:j+cellSize+off+1],
                         3: image[i+cellSize:i+cellSize+off+1,j:j+off+1],
                         4: image[i+cellSize:i+cellSize+off+1,j+cellSize:j+cellSize+off+1]}
            makeB={1:[[i,i+off+1],[j,j+off+1]],
                   2:[[i,i+off+1],[j+cellSize,j+cellSize+off+1]],
                   3:[[i+cellSize,i+cellSize+off+1],[j,j+off+1]],
                   4:[[i+cellSize,i+cellSize+off+1],[j+cellSize,j+cellSize+off+1]]}
            changeList=marchCase(checkDict,cellSize)
            if max(changeList)>0:

                for k in changeList:
                    grayRange=makeB[k]
                    for x in range(grayRange[0][0],grayRange[0][1]):
                        for y in range(grayRange[1][0],grayRange[1][1]):
                            marchImage[x][y]=0
    return marchImage



def marchCase(caseDict,cellSize):
    elements=[]

    caseDict=norm(caseDict)
    #print(caseDict)
    for key,value in caseDict.items():
        elements.append(value)
    if(len(set(elements))==2):
        minval=min(elements)
        maxval=max(elements)

        if caseDict[1]==minval and caseDict[2]==minval and caseDict[3]==maxval and caseDict[4]==minval :
            return [3]
        elif caseDict[1] == minval and caseDict[2] == minval and caseDict[3] == minval and caseDict[4] == maxval :
            return [4]
        elif caseDict[1] == minval and caseDict[2] == minval and caseDict[3] == maxval and caseDict[4] == maxval :
            return [3,4]
        elif caseDict[1] == minval and caseDict[2] == maxval and caseDict[3] == minval and caseDict[4] == minval :
            return [2]
        elif caseDict[1] == minval and caseDict[2] == maxval and caseDict[3] == maxval and caseDict[4] == minval :
            return [1,4]
        elif caseDict[1] == minval and caseDict[2] == maxval and caseDict[3] == minval and caseDict[4] == maxval :
            return [2,4]
        elif caseDict[1] == minval and caseDict[2] == maxval and caseDict[3] == maxval and caseDict[4] == maxval :
            return [1]
        elif caseDict[1] == maxval and caseDict[2] == minval and caseDict[3] == minval and caseDict[4] == minval :
            return [1]
        elif caseDict[1] == maxval and caseDict[2] == minval and caseDict[3] == maxval and caseDict[4] == minval :
            return [1,3]
        elif caseDict[1] == maxval and caseDict[2] == minval and caseDict[3] == minval and caseDict[4] == maxval :
            return [2,3]
        elif caseDict[1] == maxval and caseDict[2] == minval and caseDict[3] == maxval and caseDict[4] == maxval :
            return [2]
        elif caseDict[1] == maxval and caseDict[2] == maxval and caseDict[3] == minval and caseDict[4] == minval :
            return [1,2]
        elif caseDict[1] == maxval and caseDict[2] == maxval and caseDict[3] == maxval and caseDict[4] == minval :
            return [4]
        elif caseDict[1] == maxval and caseDict[2] == maxval and caseDict[3] == minval and caseDict[4] == maxval :
            return [3]

    return [-1]

def norm(caseDict):
    for key,value in caseDict.items():
        max=np.amax(value)
        caseDict[key]=max
    return caseDict