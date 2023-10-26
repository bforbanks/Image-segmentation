import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_convert(self):
        from src.services.image_loader import load_image
        from src.services.image_converter import rgb_2d_to_pixelvectors

        # test the add function from edgescore
        image = load_image("gates.jpg")
        rgb_2d_to_pixelvectors(image)


if __name__ == "__main__":
    unittest.main()
