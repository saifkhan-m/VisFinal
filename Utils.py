import math
from functools import wraps
from time import time

def binImage(image, totalBins):
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = quantize(image[i][j], totalBins)
    return image

def quantize(grayVal, totalBins):
    interval = 256 / totalBins
    for i in range(1, totalBins + 1):
        if grayVal <= interval * i - 1:
            return int(interval * i - 1)

def shadeImage(RGB, img, totalBins):
    for i in range(len(img)):
        for j in range(len(img[i])):
            color = getColor(img[i][j], totalBins)
            RGB[i][j] = color
    return RGB


def getColor(grayVal, totalBins):
    colorList = [[191, 55, 34],
                 [226, 69, 21],
                 [226, 117, 21],
                 [249, 122, 11],
                 [198, 150, 37],
                 [247, 176, 10],
                 [118, 125, 15],
                 [253, 221, 10],
                 [205, 216, 54],
                 [239, 255, 6],
                 [27, 149, 112],
                 [82, 183, 153],
                 [178, 240, 222],
                 [154, 166, 245],
                 [58, 80, 222],
                 [7, 22, 118],

                 ]
    if grayVal == 0:
        return 0
    interval = 256 / totalBins
    for i in range(1, totalBins + 1):  #
        if grayVal == interval * i - 1:
            return colorList[i * (len(colorList) // totalBins) - 1]
    return grayVal


def getInterval(maxVal, minVal, total_bins):
    range = maxVal - minVal
    interval = math.ceil(range / total_bins)
    return interval


#code referred from https://codereview.stackexchange.com/questions/169870/decorator-to-measure-execution-time-of-a-function
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print( 'Elevation Map of cellsize | {} | with | {} | bins took | {} | seconds'.format(args[2],args[1],end-start))
        return result
    return wrapper