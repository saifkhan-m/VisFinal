def binImage(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = quantize(image[i][j])

    return image


def quantize(grayVal):
    for i in range(1, 17):
        if grayVal <= (pow(2, 4) * i) - 1:
            return (pow(2, 4) * i) - 8 - 1


def shadeImage(RGB, img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            color = getColor(img[i][j])
            RGB[i][j] = color
    return RGB


def getColor(grayVal):
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
    if grayVal==0:
        return 0
    for i in range(1, 17):
        if grayVal == (pow(2, 4) * i) - 8 - 1:
            return colorList[i - 1]
    return grayVal


print(getColor(55))
