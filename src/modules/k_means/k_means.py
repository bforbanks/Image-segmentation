import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import numpy as np
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab, lab2rgb
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def cluster_assignments(image_pixels, centers):
    return np.argmin(euclidean_distances(image_pixels, centers), axis=1)


def initialize_centroids_randomly_and_do_one_kn(image_pixels_lab_1d):
    """First

    Args:
        image_pixels_lab (_type_): _description_

    Returns:
        y_means clusters
    """
    K = 5
    centroid = np.array(
        [image_pixels_lab_1d.mean(0) + (np.random.randn(3) / 10) for _ in range(K)]
    )
    return do_k_means(image_pixels_lab_1d, centroid, 2)


def do_k_means(image_pixels_lab_1d, centroids, loops):
    # repeat estimation a number of times (could do something smarter, like comparing if clusters change)
    for i in range(loops):
        # assign each point to the closest center
        y_kmeans = cluster_assignments(image_pixels_lab_1d, centroids)

        # move the centers to the mean of their assigned points (if any)
        for i, c in enumerate(centroids):
            points = image_pixels_lab_1d[y_kmeans == i]
            if len(points):
                centroids[i] = points.mean(0)
    return (y_kmeans, centroids)
