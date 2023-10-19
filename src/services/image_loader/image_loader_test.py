import unittest


class TestImageLoaderFunctions(unittest.TestCase):
    def test_load(self):
        from src.services.image_loader import load_image

        # test the add function from edgescore
        load_image("gates")


if __name__ == "__main__":
    unittest.main()
