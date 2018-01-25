import a


class UserInput:

    def read_even_number(self):
        number = a.get_number()
        if number % 2 == 0:
            return number
