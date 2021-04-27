from simple_calc import SimpleCalc

cal = SimpleCalc()


def test_add():
    assert cal.add(2, 2) == 4


def test_subtract():
    assert cal.subtract(4, 1) == 3