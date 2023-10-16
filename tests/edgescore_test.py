import unittest
import edgescore


class TestMathFunctions(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_add(self):
        # import the add function from edgescore

        # test the add function from edgescore
        result = edgescore.add(1, 1)
        self.assertEqual(result, 2)
