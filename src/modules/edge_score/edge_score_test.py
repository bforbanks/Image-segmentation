import unittest


class TestEgdeScoreFunctions(unittest.TestCase):
    def test_bottom_scores(self):
        from src.services.image_loader import load_image
        from src.services.image_converter import rgb_2d_to_pixelvectors_1d

        converted_image = rgb_2d_to_pixelvectors_1d(load_image("white_only"))

        self.assertEqual()


if __name__ == "__main__":
    unittest.main()
