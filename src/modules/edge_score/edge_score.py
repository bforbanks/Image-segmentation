import numpy as np

def bottom_scores(pixelvector_to_centroids_index, image_shape, centroids) -> list[int]:
    """Will give positive score to the centroids that have pixels in the sides and the top.

    Args:
        pixelvector_to_centroids_index (1d array): The numbers correspond to the index of the centroids,
        and the location in the list corresponse to the pixels location.

        image_shape (1x2 array): Shape of the image

    Returns:
        list[int]: Returns a list of the centroids score, in a list that is indexed by centroids index
    """
    pixelvector_to_centroids_index_2d = pixelvector_to_centroids_index.reshape(
        image_shape[0], image_shape[1]
    )
    # TODO: implement this function, use the pixelvector_to_centroids_index_2d
    bottom_array = pixelvector_to_centroids_index[-image_shape[0]:]

    for i in bottom_array:
        
    # example of return. If centroid 0 have have 1 point, and centroid 1 have 3 points, return the following array:


print(bottom_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3], 2))






def not_bottom_scores(pixelvector_to_centroids_index, image_shape) -> list[int]:
    """Will give negative score to the centroids that have pixels in the sides and the top.

    Args:
        pixelvector_to_centroids_index (1d array): The numbers correspond to the index of the centroids,
        and the location in the list corresponse to the pixels location.

        image_shape (1x2 array): Shape of the image

    Returns:
        list[int]: Returns a list of the centroids score, in a list that is indexed by centroids index
    """
    pixelvector_to_centroids_index_2d = pixelvector_to_centroids_index.reshape(
        image_shape[0], image_shape[1]
    )
    # TODO: implement this function, use the pixelvector_to_centroids_index_2d

    # example of return. If centroid 0 have have -1 point, and centroid 1 have -3 points, return the following array:
    return [-1, -3]


def total_scores(pixelvector_to_centroids_index, image_shape) -> list[int]:
    """Will use the two scoring functions, and sum them to get the total score for each

    Args:
        pixelvector_to_centroids_index (1d array): The numbers correspond to the index of the centroids,
        and the location in the list corresponse to the pixels location.

        image_shape (1x2 array): Shape of the image

    Returns:
        list[int]: Returns a list of the centroids score, in a list that is indexed by centroids index
    """
    pixelvector_to_centroids_index_2d = pixelvector_to_centroids_index.reshape(
        image_shape[0], image_shape[1]
    )
    # TODO: implement this function, use the pixelvector_to_centroids_index_2d

    # example of return. If centroid 0 have have 1 total point, and centroid 1 have 2 points, return the following array:
    return [1, 2]
