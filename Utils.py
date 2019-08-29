import math


def binImage(image, totalBins):
    maxVal = max(map(max, image))
    minVal = min(map(min, image))

    # interval=getInterval(maxVal,minVal,total_bins)

    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = quantize(image[i][j])
            image[i][j] = quantize2(image[i][j], totalBins)
            # image[i][j] = quantize1(image[i][j],interval,total_bins,maxVal,minVal)

    return image


def quantize(grayVal):
    for i in range(1, 17):
        if grayVal <= (pow(2, 4) * i) - 1:
            return (pow(2, 4) * i) - 8 - 1


def quantize2(grayVal, totalBins):
    interval = 256 / totalBins
    for i in range(1, totalBins + 1):  #
        if grayVal <= interval * i - 1:
            return int(interval * i - 1)


def quantize1(grayVal, interval, total_bins, maxVal, minVal):
    for i in range(total_bins):
        if minVal + (interval * i) <= grayVal < minVal + (interval * (i + 1)):
            return math.ceil((minVal + (interval * i) + (minVal + (interval * (i + 1)))) / 2)


def shadeImage(RGB, img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            color = getColor(img[i][j])
            RGB[i][j] = color
    return RGB


def shadeImage1(RGB, img, totalBins):
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


# print(quantize1(65,3,16,100,55))
# print(getInterval(100,55,16))

#print(binImage([[20, 200, 130], [150, 90, 181], [242, 62, 220]], 4))
