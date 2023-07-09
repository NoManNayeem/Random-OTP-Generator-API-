import unittest
from otp_generator.otp import generate_otp

class OTPGeneratorTestCase(unittest.TestCase):
    def test_generate_otp_valid_length(self):
        length = 6
        otp = generate_otp(length)
        self.assertEqual(len(otp), length)

    def test_generate_otp_invalid_length(self):
        invalid_lengths = [0, -1, 1.5, "length"]
        for length in invalid_lengths:
            with self.assertRaises(ValueError):
                generate_otp(length)

if __name__ == "__main__":
    unittest.main()
