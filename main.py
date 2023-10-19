from src.services.image_loader import load_image
from src.services.image_converter import (
    rgb_2d_to_pixelvectors_1d,
    pixelvectors_1d_and_centroids_to_pixelvectors_2d,
    pixelvectors_1d_and_centroids_to_rgb_2d,
)
from src.modules.k_means import initialize_centroids_randomly_and_do_one_kn

import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 100
import matplotlib.pyplot as plt

image_rgb_2d = load_image("gates.jpg")
image_pixels_lab_1d, image_shape = rgb_2d_to_pixelvectors_1d(image_rgb_2d)

(
    image_pixels_lab_1d_to_centroid,
    centroids,
) = initialize_centroids_randomly_and_do_one_kn(image_pixels_lab_1d)
# new_image = pixelvectors_1d_and_centroids_to_pixelvectors_2d(
#     image_pixels_lab_1d_to_centroid, centroids, image_shape
# )


new_image = pixelvectors_1d_and_centroids_to_rgb_2d(
    image_pixels_lab_1d_to_centroid, centroids, image_shape
)

plt.figure()
plt.imshow(new_image)
plt.show()
plt.axis("off")
