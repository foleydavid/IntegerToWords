import unittest
from Solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_assignTripletString(self):
        s = "Nine Hundred Ninety Nine "
        self.assertEqual(self.sol.assignTripletString(999, ""), s)

        s = "One Hundred Twenty Three "
        self.assertEqual(self.sol.assignTripletString(123, ""), s)

        s = "Nineteen "
        self.assertEqual(self.sol.assignTripletString(19, "One Thousand "), "One Thousand " + s)

        s = "Five "
        self.assertEqual(self.sol.assignTripletString(5, ""), s)

        s = ""
        self.assertEqual(self.sol.assignTripletString(0, ""), s)

    def test_numberToWords(self):
        s = "One Hundred Twenty Three"
        self.assertEqual(self.sol.numberToWords(123), s)

        s = "Twelve Thousand Three Hundred Forty Five"
        self.assertEqual(self.sol.numberToWords(12345), s)

        s = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        self.assertEqual(self.sol.numberToWords(1234567), s)

        s = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        self.assertEqual(self.sol.numberToWords(1234567891), s)

        s = "Zero"
        self.assertEqual(self.sol.numberToWords(0), s)

if __name__ == "__main__":
    unittest.main()
