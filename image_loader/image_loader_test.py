import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_load(self):
        from image_loader import load

        # test the add function from edgescore
        load("gates.jpg")


if __name__ == "__main__":
    unittest.main()
