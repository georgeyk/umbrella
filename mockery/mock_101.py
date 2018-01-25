from unittest.mock import Mock, MagicMock, create_autospec, call

# https://docs.python.org/3/library/unittest.mock.html


# calls and properties
foo = Mock(return_value=1, bar=2)
assert foo() == 1
assert foo.bar == 2


# errors
foo = Mock(side_effect=ValueError('lol'))
try:
    foo()
except ValueError as exc:
    assert True
else:
    assert False


# multiple calls
iterator = Mock(__next__=Mock(side_effect=[1, 2, StopIteration]))
assert next(iterator) == 1
assert next(iterator) == 2
assert next(iterator, 0) == 0  # sentinel


# nested
parent = Mock(child=Mock(return_value=2))
assert parent.child() == 2
assert parent.mock_calls == [call.child()]
# helpers
assert parent.child.called is True
assert parent.child.call_count == 1
assert parent.child.call_args == call()
parent.child()
assert parent.child.call_args_list == [call(), call()]


# tuple-ness
foo = Mock()
foo(a=1)
assert foo.call_args[0][0] == 1
assert foo.call_args[1] == {}
# wat
assert call(1) == ('', (1,), {})

foo.reset_mock()
assert foo.call_count == 0


# assert methods
foo = Mock()
foo(1)
foo.assert_called_once_with(1)
# assert foo.called
# assert foo.call_count == 1
# assert foo.call_args == call(1)


bar = Mock()
bar.assert_not_called()
# assert bar.called is False
# assert bar.call_count == 0


# autospec

def lol(x, y):
    return x + y + 1


lol_mock = create_autospec(lol, return_value=3)

assert lol_mock(1, 1) == 3
lol_mock.assert_called_once_with(1, 1)

try:
    lol_mock(1)
except TypeError:
    assert True
else:
    assert False

# patch(..., autospec=True, spec_set=True), Mock(spec=..., spec_set=...)
# (*caution: https://docs.python.org/3/library/unittest.mock.html#autospeccing)


# MagicMock: default impl. of dunder methods

ex = MagicMock()
assert len(ex) == 0  # __len__
ex.__len__.assert_called_once_with()
