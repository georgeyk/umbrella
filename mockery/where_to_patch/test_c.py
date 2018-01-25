import sys; sys.path.insert(0, '.')
from unittest import mock

from c import UserInput


@mock.patch('?.get_number')
def test_user_input_even(mock_get_number):
    mock_get_number.return_value = 2
    ui = UserInput()
    value = ui.read_even_number()
    assert value == 2
    mock_get_number.assert_called_once_with()
