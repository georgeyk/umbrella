from unittest.mock import Mock


# specific mocks and asserts

m = Mock(age=10, get_name=Mock(return_value='Foobar'))
assert m.age == 10
assert m.get_name() == 'Foobar'
m.get_name.assert_called_once_with()


# typos ? -> fail first

m = Mock(return_value=1)
assert m(2) == 1
# m(2)
m.assert_called_once_with(2)


# specs ?

stdout_mock = Mock(write=Mock(return_value=3))
assert stdout_mock.write('lol') == 3
stdout_mock.write.assert_called_once_with('lol')


# mock what you "own"
# socket/requests
# client-apis/requests

# flat is better than nested
