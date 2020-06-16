class FizzBuzz:
    def fizzBuzz(self, number):
        if number <= 0:
            raise InvalidNumberException
        if number % 15 == 0:
            return 'fizzbuzz'
        elif number % 3 == 0:
            return 'fizz'
        elif number % 5 == 0:
            return 'buzz'

        return str(number)

    def fizzBuzzGenerator(self, number):
        if number <= 0:
            raise InvalidNumberException
        result = ""
        for i in range(number):
            result += self.fizzBuzz(i+1) + ","

        return result[:-1]


class InvalidNumberException(Exception):
    pass


def main():
    fizzbuzz = FizzBuzz()
    print(fizzbuzz.fizzBuzzGenerator(100))


if __name__ == '__main__':
    main()