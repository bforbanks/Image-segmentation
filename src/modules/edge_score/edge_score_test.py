import unittest


class TestEgdeScoreFunctions(unittest.TestCase):
    def test_bottom_scores(self):
        from src.services.image_loader import load_image
        from src.services.image_converter import rgb_2d_to_pixelvectors_2d
        from src.modules.edge_score import bottom_scores

        pixelvectors_2d_list = [
            rgb_2d_to_pixelvectors_2d(load_image(name))
            for name in ["white_only", "mixed_3"]
        ]
        bottom_score_list = bottom_scores(pixelvectors_2d_list)


if __name__ == "__main__":
    unittest.main()
