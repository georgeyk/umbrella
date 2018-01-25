from a import get_number


class UserInput:

    def read_even_number(self):
        number = get_number()
        if number % 2 == 0:
            return number
