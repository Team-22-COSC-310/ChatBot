import unittest
import os
import sys

path = os.getcwd().removesuffix("\\Unit Tests")
if path not in sys.path:
    sys.path.append(path)
    import category


class TestCategory(unittest.TestCase):
    def test_get_bofw(self) -> None:
        """
        Tests the get_bofw() method
        :return: None
        """
        # test case 1
        answer: dict[str:int] = {
            "the": 2,
            "quick": 1,
            "brown": 1,
            "fox": 1,
            "jumps": 1,
            "over": 1,
            "lazy": 1,
            "dog": 1,
        }
        result: dict[str:int] = category.get_bofw(
            "the quick brown fox jumps over the lazy dog"
        )
        self.assertEqual(answer, result)

        # test case 2
        answer: dict[str:int] = {
            "over": 1,
            "the": 2,
            "hedge": 2,
            "back": 1,
            "to": 1,
        }
        result: dict[str:int] = category.get_bofw("over the hedge back to the hedge")
        self.assertEqual(answer, result)

        # test case 3
        answer: dict[str:int] = {
            "black": 2,
            "to": 2,
            "the": 1,
            "back": 2,
        }
        result: dict[str:int] = category.get_bofw("black to the back back to black")
        self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
