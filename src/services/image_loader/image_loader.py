import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import numpy as np
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab, lab2rgb
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def load_image(image_to_load: str):
    image_raw = imread("./images/" + image_to_load + ".jpg")
    return image_raw
