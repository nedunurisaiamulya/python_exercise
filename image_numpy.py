import numpy as np
import matplotlib.pylab as plt
im = plt.imread("dora.jpg")
def plti(im, h=8, **kwargs):
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')

plti(im)
plt.show()


