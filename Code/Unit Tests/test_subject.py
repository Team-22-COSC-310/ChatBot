import unittest
import os
import sys

path = os.getcwd().removesuffix("\\Unit Tests")
if path not in sys.path:
    sys.path.append(path)
    import subject
    import preprocess


class TestSubject(unittest.TestCase):
    def test_find_subject(self):
        # test case 1
        answer = "shoe"
        result = subject.find_subject(
            preprocess.parse_string(
                "I bough a pair of shoes from your store and they are worn out."
            )
        )
        self.assertEqual(answer, result)

        # test case 2
        answer = "dress"
        result = subject.find_subject(
            preprocess.parse_string(
                "I bough a pair of dress from your store and they are worn out."
            )
        )
        self.assertEqual(answer, result)

        # test case 3
        answer = "boot"
        result = subject.find_subject(
            preprocess.parse_string(
                "I bough a pair of boots from your store and they are worn out."
            )
        )
        self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
