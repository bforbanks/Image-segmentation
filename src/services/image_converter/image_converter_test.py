import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_convert(self):
        from image_loader import load_image
        from image_converter import rgb_2d_to_pixelvectors_1d

        # test the add function from edgescore
        image = load_image("gates.jpg")
        rgb_2d_to_pixelvectors_1d(image)


if __name__ == "__main__":
    unittest.main()
