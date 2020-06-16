import unittest


# A testcase is created by subclassing unittest.TestCase.
from fizzbuzz.FizzBuzz import FizzBuzz, InvalidNumberException

FIZZBUZZ = "fizzbuzz"

BUZZ = "buzz"

FIZZ = "fizz"


class FizzBuzzTest(unittest.TestCase):
    fizzbuzz = FizzBuzz()

    # tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.
    def test_should_return_number_when_1(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=1)

        self.assertEqual("1", fizzbuzz_result)

    def test_should_return_number_when_2(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=2)

        self.assertEqual("2", fizzbuzz_result)

    def test_should_return_fizz_when_3(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=3)

        self.assertEqual(FIZZ, fizzbuzz_result)

    def test_should_return_buzz_when_5(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=5)

        self.assertEqual(BUZZ, fizzbuzz_result)

    def test_should_return_fizz_when_9(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=9)

        self.assertEqual(FIZZ, fizzbuzz_result)

    def test_should_return_buzz_when_10(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=10)

        self.assertEqual(BUZZ, fizzbuzz_result)

    def test_should_return_fizzbuzz_when_15(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=15)

        self.assertEqual(FIZZBUZZ, fizzbuzz_result)

    def test_should_return_fizzbuzz_when_45(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzz(number=45)

        self.assertEqual(FIZZBUZZ, fizzbuzz_result)

    def test_should_throw_Exception_when_0(self):
        with self.assertRaises(InvalidNumberException):
            self.fizzbuzz.fizzBuzz(number=0)


class FizzBuzzGeneratorTest(unittest.TestCase):
    fizzbuzz = FizzBuzz()

    def test_should_return_1_when_1(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzzGenerator(number=1)

        self.assertEqual("1", fizzbuzz_result)

    def test_should_return_1comma2_when_2(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzzGenerator(number=2)

        self.assertEqual("1,2", fizzbuzz_result)

    def test_should_throw_Exception_when_0(self):
        with self.assertRaises(InvalidNumberException):
            self.fizzbuzz.fizzBuzzGenerator(number=0)

    def test_should_return_1comma2commafizz_when_3(self):
        fizzbuzz_result = self.fizzbuzz.fizzBuzzGenerator(number=3)

        self.assertEqual("1,2,fizz", fizzbuzz_result)


if __name__ == '__main__':
    unittest.main()
