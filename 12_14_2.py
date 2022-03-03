import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def demosaic(cfa, pattern):
    cfah = cfa.shape[0]
    cfal = cfa.shape[1]
    img = np.zeros([cfah, cfal, 3])

    IR = np.zeros(cfa.shape)
    IG = np.zeros(cfa.shape)
    IB = np.zeros(cfa.shape)

    # flatter range
    matrix = 1
    while pow(matrix, 2) != len(pattern):
        matrix += 1

    # r=0, g=1 and 2, b=3 put into IR,IG,IB
    for i in range(cfa.shape[0]):
        for j in range(cfa.shape[1]):
            tem = i % matrix * matrix + j % matrix
            if tem == 0:
                IR[i, j] = cfa[i, j]
            if tem == 1 or tem == 2:
                IG[i, j] = cfa[i, j]
            if tem == 3:
                IB[i, j] = cfa[i, j]

    # demosaic and create img
    for i in range(cfa.shape[0]):
        for j in range(cfa.shape[1]):
            tem = i % matrix * matrix + j % matrix
            if tem == 0:
                IG[i, j] = int((IG[i, j+1] + IG[i+1, j]) / 2)
                IB[i, j] = IB[i+1, j+1]
            if tem == 1:
                IR[i, j] = IR[i, j-1]
                IB[i, j] = IB[i+1, j]
            if tem == 2:
                IR[i, j] = IR[i-1, j]
                IB[i, j] = IB[i, j+1]
            if tem == 3:
                IR[i, j] = IR[i - 1, j-1]
                IG[i, j] = int((IG[i-1, j] + IG[i, j-1]) / 2)
            img[i, j] = [IR[i, j], IG[i, j], IB[i, j]]
    img = img.astype('uint8')
    return img

cfa = (plt.imread('frog2cfaimage.png')*255).astype('uint8')
img = demosaic(cfa, pattern='rggb')
imgsave = Image.fromarray(img)
imgsave.save('frogcfa2image.png')
plt.imshow(img)
plt.show()