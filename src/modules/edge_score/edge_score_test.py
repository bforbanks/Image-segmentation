import unittest
import numpy as np

from src.modules.edge_score import bottom_scores, not_bottom_scores, total_edge_scores


class TestEgdeScoreFunctions(unittest.TestCase):
    def test_bottom_scores(self):
        # test for the following image:
        # +---------+
        # | 1  1  1 |
        # | 1  1  1 |
        # | 0  0  0 |                                  You can also see what it should return rigth here
        # +---------+                                                       |
        # shoud return [3, 0]                                               V
        self.assertEqual(
            bottom_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3], 2), [3, 0]
        )
        # test for the following image:
        # +---------+
        # | 1  3  2 |
        # | 1  1  2 |
        # | 0  1  0 |
        # +---------+
        # shoud return [2, 1, 0, 0] because we have 2 centroid-zeros in the lower row and 1 centroid-one.
        self.assertEqual(
            bottom_scores(np.array([1, 3, 2, 1, 1, 2, 0, 1, 0]), [3, 3], 4),
            [2, 1, 0, 0],
        )

    def test_not_bottom_scores(self):
        self.assertEqual(
            not_bottom_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3], 2), [0, -5]
        )
        self.assertEqual(
            not_bottom_scores(np.array([1, 1, 2, 1, 1, 2, 0, 1, 0]), [3, 3], 3),
            [0, -3, -2],
        )

    def test_total_scores(self):
        # test for the following image:
        # +---------+
        # | 1  1  1 |
        # | 1  1  1 |
        # | 0  0  0 |
        # +---------+
        self.assertEqual(
            total_edge_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3], 2), [3, -5]
        )
        # test for the following image:
        # +---------+
        # | 1  1  2 |
        # | 1  1  2 |
        # | 0  1  0 |
        # +---------+
        self.assertEqual(
            total_edge_scores(np.array([1, 1, 2, 1, 1, 2, 0, 1, 0]), [3, 3], 3),
            [2, -2, -2],
        )


if __name__ == "__main__":
    unittest.main()
