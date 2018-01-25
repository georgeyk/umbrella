import sys

from unittest.mock import Mock


# generic assertions are bad

m = Mock()
assert m.foobar  # bad

m = Mock(foobar=1)
assert m.foobar == 1  # "good"


# too "smart"

response = Mock()
assert response.ok
assert response.text
assert response.cookies
assert response.status_code
assert response.json()


# nesting

m = Mock(bar=Mock(foo=Mock(return_value=1)))
assert m.bar.foo() == 1

m = Mock(bar=Mock(return_value=Mock(foo=Mock(return_value=1))))
assert m.bar().foo() == 1


# typos ?

m = Mock()
m()
m.asert_called_once_with()
# m.assret_called_once_with()


# spec/spec_set ?

m = Mock(spec=sys.stdout)

try:
    m.written  # good! (attribute or method does not exist)
except AttributeError:
    assert True
else:
    assert False


assert m.write(1, 2, 3, 4, 5)  # bad, sys.stdout.write() requires only one arg

# another try
n = Mock(spec=sys.stdout.write)
assert n(1, 2, 3)
assert n()

# =/
