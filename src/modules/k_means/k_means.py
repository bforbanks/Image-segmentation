import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import numpy as np
from skimage.io import imread
from skimage.transform import rescale
from skimage.color import rgb2lab, lab2rgb
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def cluster_assignments(image_pixels, centroids):
    return np.argmin(euclidean_distances(image_pixels, centroids), axis=1)


def initialize_centroids_randomly(image_pixels_lab, centroid_count):
    """First

    Args:
        image_pixels_lab_1d: text

    Returns:
        pixelvector_to_centroids_index: text
        centroids: text

    """
    np.random.seed(42)
    centroids = np.array(
        [
            image_pixels_lab.mean(0) + (np.random.randn(3) / 10)
            for _ in range(centroid_count)
        ]
    )
    return centroids


def do_k_means(image_pixels_lab_1d, centroids, loops):
    # repeat estimation a number of times (could do something smarter, like comparing if clusters change)
    for i in range(loops):
        # assign each point to the closest center
        pixelvector_to_centroids_index = cluster_assignments(
            image_pixels_lab_1d, centroids
        )

        # move the centers to the mean of their assigned points (if any)
        for i, c in enumerate(centroids):
            points = image_pixels_lab_1d[pixelvector_to_centroids_index == i]
            if len(points):
                centroids[i] = points.mean(0)
    return (pixelvector_to_centroids_index, centroids)
