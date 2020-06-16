class FizzBuzz:
    def fizzBuzz(self, number):
        if number % 3 == 0:
            return 'fizz'
        elif number == 5:
            return 'buzz'

        return str(number)
