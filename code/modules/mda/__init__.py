import math

pi=22/7


def isprime(pnum):
    """This checks whether the number is prime or not."""

    if pnum == 0 or 1:
        _tuff_ = False
    elif pnum == 2:
        _tuff_ = True
    elif pnum % plp_ == 0:
        for plp_ in range(2, pnum):
            _tuff_ = False
    else:
        _tuff_ = True

    return _tuff_


def isrtriangle(hypo, side1, side2):
    """Checks whether the triangle is right angle triangle or not."""

    if math.sqrt(hypo) == math.sqrt(side1)+math.sqrt(side2):
        _tuffh_ = True
    else:
        _tuffh_ = False

    return _tuffh_


def cube(num): 

    """Returns the cube of x."""

    return num**3


def raise_power(num, x):

    """Returns the x raise to the power."""

    return num**x


def sqrt(num, x):

    """Returns the square of x."""

    return math.sqrt(num, x)
