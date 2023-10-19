import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_load(self):
        from image_loader import load_image

        # test the add function from edgescore
        load_image("gates.jpg")


if __name__ == "__main__":
    unittest.main()
