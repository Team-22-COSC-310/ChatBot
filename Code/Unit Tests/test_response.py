import unittest
import os
import sys

path = os.getcwd().removesuffix("\\Unit Tests")
if path not in sys.path:
    sys.path.append(path)
    import response


class TestResponse(unittest.TestCase):
    def test_generate_response(self):
        # test case 1
        category = "product satisfaction"
        subject = "product"
        answers = [
            resp.format(subject=subject)
            for resp in response.product_satisfaction_responses
        ]
        result = response.generate_response(category, subject)
        self.assertIn(result, answers)

        # test case 2
        category = "complaint"
        subject = "product"
        answers = [
            resp.format(subject=subject) for resp in response.complaint_responses
        ]
        result = response.generate_response(category, subject)
        self.assertIn(result, answers)

        # test case 3
        category = "review"
        subject = "product"
        answers = [resp.format(subject=subject) for resp in response.review_responses]
        result = response.generate_response(category, subject)
        self.assertIn(result, answers)


if __name__ == "__main__":
    unittest.main()
