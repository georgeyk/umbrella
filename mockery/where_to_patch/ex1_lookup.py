import sys; sys.path.insert(0, '.')
from unittest.mock import Mock

from b import UserInput


ui = UserInput()

# change "look-up" reference (namespace)

import b
b.get_number = Mock(return_value=2)


print('enter_number: ')
value = ui.read_even_number()
print('even={}'.format(bool(value)))
