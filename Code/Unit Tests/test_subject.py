import unittest
import Code.subject as subject
import Code.preprocess as preprocess


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
