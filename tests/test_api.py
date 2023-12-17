import unittest

from main import app

# set our application to testing mode
app.testing = True


class TestApi(unittest.TestCase):

    def test_ping(self):
        with app.test_client() as client:
            result = client.get(
                '/ping'
            )

            expected_result = 'pong'

            actual_result = result.data.decode("utf-8")

            # check result from server with expected data
            self.assertEqual(
                actual_result,
                expected_result
            )

    def test_invalid_input(self):
        with app.test_client() as client:

            sent = {'input': 'some string'}

            expected_status_code = 422
            expected_result = 'Input error - input should be numerical'

            result = client.post(
                '/square',
                json=sent
            )

            actual_status_code = result.status_code
            actual_result = result.data.decode("utf-8")

            # check for error status code
            self.assertEqual(
                actual_status_code,
                expected_status_code
            )

            # check for error message
            self.assertEqual(
                actual_result,
                expected_result
            )

    def test_valid_input(self):
        with app.test_client() as client:

            sent = {'input': 12}

            result = client.post(
                            '/square',
                            json=sent
                        )

            expected_result = 144

            actual_result = result.json['result']

            # check result from server with expected data
            self.assertEqual(
                actual_result,
                expected_result
            )


if __name__ == '__main__':
    unittest.main()
