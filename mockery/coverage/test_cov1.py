def score(x):
    if x > 0 and x % 2 == 0:
        return x + 1
    return x + 2


def test_score_even():
    assert score(2) == 3


def test_score_odd():
    assert score(3) == 5
