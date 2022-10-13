
def convert_to_gray_scale(image):
    height = len(image)
    width = len(image[0])

    gray_scale_image = image.copy()

    for i in range(height):
        for j in range(width):
            sum = 0
            mean = 0
            for pixelVal in image[i][j]: sum += pixelVal
            mean = int(sum / len(image[i][j]))

            # k is index of red green and blue in current pixel
            for k in range(len(image[i][j])):
                gray_scale_image[i][j][k] = mean
    
    return gray_scale_image



def convert_to_reverse(image):
    height = len(image)
    width = len(image[0])

    reverse_image = image.copy()

    for i in range(height):
        for j in range(width):
            # k is index of red green and blue in current pixel
            # 255 is max pixel value and it is white
            for k in range(len(image[i][j])):
                reverse_image[i][j][k] = 255 - reverse_image[i][j][k]

    return reverse_image