
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
            gray_scale_image[i][j][0] = mean
            gray_scale_image[i][j][1] = mean
            gray_scale_image[i][j][2] = mean
    
    return gray_scale_image



def convert_to_reverse(image):
    height = len(image)
    width = len(image[0])

    reverse_image = image.copy()

    for i in range(height):
        for j in range(width):
            x = 255
            reverse_image[i][j][0] = x - image[i][j][0]
            reverse_image[i][j][1] = x - image[i][j][1]
            reverse_image[i][j][2] = x - image[i][j][2]

    return reverse_image