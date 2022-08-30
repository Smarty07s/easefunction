import math

pi = 22/7


def isprime(pnum=int):
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


def isrtriangle(hypo=float(), side1=float(), side2=float()):
    """Checks whether the triangle is right angle triangle or not."""

    if square(hypo) == square(side1)+square(side2):
        _tuffh_ = True
    else:
        _tuffh_ = False

    return _tuffh_


def cube(num=float()):
    """Returns the cube of x."""

    return num**3


def pwr(num=float(), x=float()):
    """Returns raise to the power x."""

    return num**x


def square(num=float()):
    """Returns the square of x."""

    return (num)**2


def qzros(first_term=float, second_term=float, third_term=float, zero=float(0)):
    """Returns zeros of the quadratic polynomial 
        Warning! : Not works properly

    ft = first_term
    st = second_term
    tht = third_term

    _d_ = square(st) - (4 * (ft * tht))

    if _d_*(-1)==math.sqrt(square(_d_)):

        _ro_ = math.sqrt(_d_*(-1))

    else:

        _ro_ = math.sqrt(_d_)

    _zst_ = float((((-st) + _ro_)/2*ft)-zero)

    _znd_ = float((((-st) - _ro_)/2*ft)-zero)

    return [_zst_, _znd_]"""




