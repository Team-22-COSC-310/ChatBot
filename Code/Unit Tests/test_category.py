import unittest
import os
import sys

path = os.getcwd().removesuffix("\\Unit Tests")
if path not in sys.path:
    sys.path.append(path)
    import category


class TestCategory(unittest.TestCase):
    def test_tokenize(self):
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

    def test_term_frequency(self):
        pass

    def test_inverse_document_frequency(self):
        pass

    def test_tfidf(self):
        pass

    def test_cosine_similarity(self):
        pass

    def test_find_category(self):
        pass


if __name__ == "__main__":
    unittest.main()
