from src.services.image_loader import load_image
from src.services.image_converter import (
    rgb_2d_to_pixelvectors,
    pixelvectors_and_centroids_to_rgb_2d,
    rescale_image,
)
from src.services.cam import cam
from src.modules.k_means import initialize_centroids_randomly, do_k_means
from src.modules.edge_score import total_edge_scores

import matplotlib as mpl
import numpy as np

mpl.rcParams["figure.dpi"] = 100
import matplotlib.pyplot as plt

image_names = ["altman", "avicii", "dicaprio", "gates", "woman"]

centroid_count = 6
initial_k_means_iterations = 2
after_edgescore_k_means_iterations = 10

iterations_pr_image = 60


def main():
    my_cam = cam()
    plt.ion()
    ax1 = plt.subplot(1, 4, 1)
    ax2 = plt.subplot(1, 4, 2)
    ax3 = plt.subplot(1, 4, 3)
    ax4 = plt.subplot(1, 4, 4)

    im1 = ax1.imshow(np.zeros((300, 300, 3)))
    im2 = ax2.imshow(np.zeros((300, 300, 3)))
    im3 = ax3.imshow(np.zeros((300, 300, 3)))
    im4 = ax4.imshow(np.zeros((300, 300, 3)))
    for i in range(0, len(image_names) * iterations_pr_image):
        # load the image
        # image_rgb_2d = my_cam.getCurrentImage()
        image_rgb_2d, image_shape = rescale_image(
            load_image(f"{image_names[i % len(image_names)]}.jpg"), 200
        )
        correct_image_rgba_2d, _ = rescale_image(
            load_image(f"{image_names[i % len(image_names)]}.png"), 200
        )

        (
            image_pixels_lab_1d,
            image_rgb_2d,
        ) = rgb_2d_to_pixelvectors(image_rgb_2d)

        # initialize centroids and do initial k-means
        centroids = initialize_centroids_randomly(image_pixels_lab_1d, centroid_count)
        (pixelvector_to_centroids_index, centroids) = do_k_means(
            image_pixels_lab_1d, centroids, initial_k_means_iterations
        )

        # take the edge score and the imge
        edge_score = total_edge_scores(
            pixelvector_to_centroids_index, image_shape, len(centroids)
        )
        im2.set_data(
            pixelvectors_and_centroids_to_rgb_2d(
                pixelvector_to_centroids_index, centroids, image_shape
            )
        )

        # save the background and foregroudn centroids
        centroids_argsorted = np.argsort(edge_score)
        background_centroid_indexs = centroids_argsorted[:3]
        foreground_centroid_indexs = centroids_argsorted[-3:]

        # continue doing k-means
        (
            pixels_to_centroidindex,
            centroids,
        ) = do_k_means(
            image_pixels_lab_1d, centroids, after_edgescore_k_means_iterations
        )

        # convert the background of this image to pink and keep the foreground as the original color

        # show the image with the background removed
        image_rgba = np.zeros((len(pixels_to_centroidindex), 4))
        for i, pixel in enumerate(image_rgb_2d.reshape(-1, 3)):
            if pixels_to_centroidindex[i] in foreground_centroid_indexs:
                image_rgba[i] = list(pixel) + [1.0]

        # check for accuracy

        image_alpha = image_rgba[:, 3]
        correct_image_alpha = correct_image_rgba_2d.reshape(-1, 4)[:, 3]

        incorrect_alpha = np.size(
            np.where(abs(image_alpha - correct_image_alpha) > 0.1)
        )
        alpha_accuracy = abs(1 - incorrect_alpha / np.size(image_alpha))
        print(alpha_accuracy)

        im4.set_data(image_rgba.reshape(image_shape[0], image_shape[1], 4))

        for i in background_centroid_indexs:
            centroids[i] = [53.23288178584245, 80, 67]
        for i in foreground_centroid_indexs:
            centroids[i] = [87, -87, 88]

        new_image = pixelvectors_and_centroids_to_rgb_2d(
            pixels_to_centroidindex, centroids, image_shape
        )

        im3.set_data(new_image)
        im1.set_data(image_rgb_2d)
        plt.pause(0.02)


main()
