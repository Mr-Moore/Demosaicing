import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# color compare to number r:0, g:1, b:2
def rgb2cfa(img, number):

    IR = img[:,:,0]
    togray_img = np.zeros(IR.shape)

    # calculate number matrix
    matrix = len(number)
    pownumber = 1
    while matrix != pow(pownumber, 2):
        pownumber+=1

    # change img to cfaimage
    for i in range(img.shape[0]):
        tem = i % pownumber
        short_variable = tem * pownumber
        now_number = int(number[short_variable])
        for j in range(img.shape[1]):
            color = img[i, j][now_number]
            togray_img[i, j] = color

            if (j+1) % pownumber != 0:
                now_number = int(number[short_variable + (j+1) % pownumber])
            else:
                now_number = int(number[short_variable])
    togray_img = togray_img.astype('uint8')
    # plt the cfa image
    # imgsave = Image.fromarray(togray_img)
    # imgsave.save('frog2cfaimage.png')
    plt.imshow(togray_img, cmap='gray', interpolation='none')
    plt.show()

img = (plt.imread('frog.png')*255).astype('uint8')[:,:,0:3]

# color compare to number r:0, g:1, b:2
color_number = '0112'
rgb2cfa(img, color_number)