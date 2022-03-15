import unittest
import Code.preprocess as preprocess


class TestPreprocess(unittest.TestCase):
    def test_replace(self):
        # test case 1
        answer = "Hello how are you guys today"
        result = preprocess.replace(
            "Hello how are you guys today!", preprocess.REPLACEMENT_MAP
        )
        self.assertEqual(result, answer)

        # test case 2
        answer = "I am currently on vacation for 2 3 months"
        result = preprocess.replace(
            "I am currently on vacation for 2-3 months!", preprocess.REPLACEMENT_MAP
        )
        self.assertEqual(result, answer)

        # test case 3
        answer = "The time is 230 I better get started washing the dishs"
        result = preprocess.replace(
            "The time is 2:30. I better get started washing the dish's.",
            preprocess.REPLACEMENT_MAP,
        )
        self.assertEqual(result, answer)

    def test_parse_string(self):
        answer = "hello how are you guy today"
        result = preprocess.parse_string("Hello how are you guys today!")
        self.assertEqual(result, answer)

        # test case 2
        answer = "i am current on vacat for 2 3 month"
        result = preprocess.parse_string("I am currently on vacation for 2-3 months!")
        self.assertEqual(result, answer)

        # test case 3
        answer = "the time is 230 i better get start wash the dish"
        result = preprocess.parse_string(
            "The time is 2:30. I better get started washing the dish's."
        )
        self.assertEqual(result, answer)


if __name__ == "__main__":
    unittest.main()
