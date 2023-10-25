from src.services.image_loader import load_image
from src.services.image_converter import (
    rgb_2d_to_pixelvectors_1d,
    pixelvectors_1d_and_centroids_to_pixelvectors_2d,
    pixelvectors_1d_and_centroids_to_rgb_2d,
)
from src.services.cam import cam
from src.modules.k_means import initialize_centroids_randomly_and_do_one_kn

import matplotlib as mpl
import numpy as np

mpl.rcParams["figure.dpi"] = 100
import matplotlib.pyplot as plt
import asyncio


def main():
    my_cam = cam()
    # image_rgb_2d = load_image("gates")
    plt.ion()
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)

    im1 = ax1.imshow(np.zeros((200, 200, 3)))
    im2 = ax2.imshow(np.zeros((200, 200, 3)))
    while True:
        image_rgb_2d = my_cam.getCurrentImage()
        image_pixels_lab_1d, image_shape = rgb_2d_to_pixelvectors_1d(image_rgb_2d)

        (
            image_pixels_lab_1d_to_centroid,
            centroids,
        ) = initialize_centroids_randomly_and_do_one_kn(image_pixels_lab_1d, 5)
        # new_image = pixelvectors_1d_and_centroids_to_pixelvectors_2d(
        #     image_pixels_lab_1d_to_centroid, centroids, image_shape
        # )

        new_image = pixelvectors_1d_and_centroids_to_rgb_2d(
            image_pixels_lab_1d_to_centroid, centroids, image_shape
        )

        im1.set_data(image_rgb_2d)
        im2.set_data(new_image)
        plt.pause(0.2)


main()
