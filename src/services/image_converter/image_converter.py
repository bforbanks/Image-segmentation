import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import numpy as np
from skimage.transform import rescale
from skimage.color import rgb2lab, lab2rgb


def rgb_2d_to_pixelvectors_1d(image_rbg_2d):
    """Convert image to the 1d array

    Args:
        image_rbg_2d (image): input

    Returns
    -------
    pixelvectors_1d : (..., 3, ...) ndarray
        The image in Lab format. Same dimensions as input.
    image_shape :
    """
    image_width = 3
    image_rgb_2d = rescale(
        image_rbg_2d,
        image_width / image_rbg_2d.shape[0],
        mode="reflect",
        channel_axis=2,
        anti_aliasing=True,
    )
    image_shape = image_rgb_2d.shape
    pixelvector = rgb2lab(image_rgb_2d).reshape(-1, 3)
    return (pixelvector, image_shape)


def pixelvectors_1d_and_centroids_to_pixelvectors_2d(
    image_pixels_lab_1d_to_centroid,
    centroids,
    image_shape,
):
    return centroids[image_pixels_lab_1d_to_centroid, :].reshape(
        image_shape[0], image_shape[1], 3
    )


def pixelvectors_1d_and_centroids_to_rgb_2d(
    image_pixels_lab_1d_to_centroid,
    centroids,
    image_shape,
):
    return lab2rgb(
        centroids[image_pixels_lab_1d_to_centroid, :].reshape(
            image_shape[0], image_shape[1], 3
        )
    )
