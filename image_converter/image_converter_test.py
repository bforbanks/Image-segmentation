import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_convert(self):
        from image_loader import load_image
        from image_converter import convert_image

        # test the add function from edgescore
        image = load_image("gates.jpg")
        convert_image(image)


if __name__ == "__main__":
    unittest.main()
