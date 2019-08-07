import copy

def marchingSquares(image,lim):
    marchImage=copy.deepcopy(image)
    off=int(lim/2)
    for i in range(len(image)-off):
        for j in range(len(image[0])-off):
            checkDict = {1: image[i][j], 2: image[i][j + off], 3: image[i + off][j], 4: image[i + off][j + off]}
            makeB={1:[i,j],2:[i,j+off],3:[i+off,j],4:[i+off,j+off]}
            changeList=marchCase(checkDict)
            if max(changeList)>0:
                for k in changeList:
                    marchImage[makeB[k][0],makeB[k][1]]=0

    return marchImage



def marchCase(caseDict):
    elements=[]
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


