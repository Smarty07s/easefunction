import math

pi = 22/7


def isprime(pnum):
    """Returns True if pnum is prime number."""

    if pnum == 0 or pnum == 1:
        _tuff_ = False
    elif pnum == 2:
        _tuff_ = True

    else:
        for plp_ in range(2, pnum):
            if pnum % plp_ == 0:

                _tuff_ = False
                break
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
    """Returns raise to the power x."""

    return num**x


def sqrt(num, x):
    """Returns the square of x."""

    return math.sqrt(num, x)

def qzros(first_term,second_term,third_term):
    """Returns zeros of the quadratic polynomial"""

    _mul_=first_term*third_term

    
