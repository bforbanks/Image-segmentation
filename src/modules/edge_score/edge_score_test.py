import unittest
import numpy as np

from src.modules.edge_score import bottom_scores, not_bottom_scores


class TestEgdeScoreFunctions(unittest.TestCase):
    def test_bottom_scores(self):
        self.assertEqual(
            bottom_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3]), [-3, 0]
        )
        self.assertEqual(
            bottom_scores(np.array([1, 1, 2, 1, 1, 2, 0, 1, 0]), [3, 3]), [-2, 0, 0]
        )

    def test_not_bottom_scores(self):
        self.assertEqual(
            not_bottom_scores(np.array([1, 1, 1, 1, 1, 1, 0, 0, 0]), [3, 3]), [0, 5]
        )
        self.assertEqual(
            not_bottom_scores(np.array([1, 1, 2, 1, 1, 2, 0, 1, 0]), [3, 3]), [0, 3, 2]
        )


if __name__ == "__main__":
    unittest.main()
