import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import numpy as np
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab, lab2rgb
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def load(image_to_load: str):
    image_raw = imread("./images/" + image_to_load)
    image_width = 200
    image = rescale(
        image_raw,
        image_width / image_raw.shape[0],
        mode="reflect",
        channel_axis=2,
        anti_aliasing=True,
    )
    shape = image.shape
    plt.figure()
    plt.imshow(image)
    plt.axis("off")

    image_pixels_lab = rgb2lab(image).reshape(-1, 3)

    plt.figure()
    ax = plt.axes(projection="3d")
    ax.view_init(elev=20.0, azim=120)
    ax.set_xlabel("L")
    ax.set_ylabel("A")
    ax.set_zlabel("B")
    image_c = [
        image.reshape(-1, 3)[i, :] for i in range(image.shape[0] * image.shape[1])
    ]
    ax.scatter3D(
        image_pixels_lab[:, 0],
        image_pixels_lab[:, 1],
        image_pixels_lab[:, 2],
        marker="o",
        c=image_c,
        linewidths=0,
    )
    ax.scatter3D(
        image_pixels_lab[:, 0],
        image_pixels_lab[:, 1],
        image_pixels_lab[:, 2],
        marker="o",
        c=image_c,
        linewidths=0,
    )
    return image_pixels_lab
