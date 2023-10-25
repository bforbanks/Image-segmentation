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
    bottom_array = pixelvector_to_centroids_index[
        -image_shape[0] :
    ]  # creates a list with the bottom values
    bottom_score = [
        0
    ] * centroids  # sets all elements of list to 0 based on the amount of centroids

    for value in bottom_array:
        bottom_score[value] += 1

    return bottom_score

    # example of return. If centroid 0 have have 1 point, and centroid 1 have 3 points, return the following array:


def not_bottom_scores(
    pixelvector_to_centroids_index, image_shape, centroid
) -> list[int]:
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
    rows, columns = pixelvector_to_centroids_index_2d.shape
    top_row = list(pixelvector_to_centroids_index_2d[0, :])
    left_side = list(pixelvector_to_centroids_index_2d[1:-1, 0])
    right_side = list(pixelvector_to_centroids_index_2d[1:-1, columns - 1])
    not_bottom_array = top_row + left_side + right_side

    not_bottom_score = [0] * centroid

    for value in not_bottom_array:
        not_bottom_score[value] -= 1

    # example of return. If centroid 0 has -1 point, and centroid 1 has -3 points, return the following array:
    return not_bottom_score


def total_edge_scores(
    pixelvector_to_centroids_index, image_shape, centroid
) -> list[int]:
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

    # First the function will pull the scores from the bottom_scores and not_bottom_scores functions.
    # These will be saved as scores and deduction

    scores = bottom_scores(pixelvector_to_centroids_index, image_shape, centroid)
    deduction = not_bottom_scores(pixelvector_to_centroids_index, image_shape, centroid)

    bottom_score = bottom_scores(pixelvector_to_centroids_index, image_shape, centroid)
    not_bottom_score = not_bottom_scores(
        pixelvector_to_centroids_index, image_shape, centroid
    )

    total_score = np.add(not_bottom_score, bottom_score)

    # Hereafter return the score, which should be identical to the structure of the previous scoring functions, having relied on them as the only source of information.
    # example of return. If centroid 0 have have 1 total point, and centroid 1 have 2 points, return the following array:
    return list(total_score)
