"""It is a small library for solving some mathematical alliances
and some mathematical instructions such as factorial."""


def factorial(n: int) -> int:
    """of factorial for computing
    multiplication 1 until the n use becomes"""
    if not isinstance(n, int):
        raise TypeError("this function only for int definition becomes")
    elif n < 0:
        raise ValueError(
            "this function for number \
                         negative definition not becomes"
        )
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def isq(a: int, b: int) -> int:
    """(a+b)^2=a^2+2ab+b^2"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a + b) ** 2


def iisq(a: int, b: int) -> int:
    """(a-b)^2=a^2-2ab+b^2"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a - b) ** 2


def square_3(a: int, b: int, c: int) -> int:
    """(a+b+c)^2=a^2+b^2+c^2+2ab+2ac+2bc"""
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError("this function only for int definition becomes")

    else:
        return (a + b + c) ** 2


def square_3_neg(a: int, b: int, c: int) -> int:
    """(a+b-c)^2=a^2+b^2+c^2+2ab-2ac-2bc"""
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a + b - c) ** 2


def opshn_s(*argus: int) -> int:
    """optional identity square"""
    for arg in argus:
        if not isinstance(arg, int):
            raise TypeError("this function only for int definition becomes")
    else:
        return sum(argus) ** 2


def opshn_s_neg(*argus: int, endneg: int) -> int:
    """optional identity square negative"""
    for arg in argus:
        if not isinstance(arg, int) or not isinstance(endneg, int):
            raise TypeError("this function only for int definition becomes")
    else:
        return (sum(argus) - endneg) ** 2


def cube(a: int, b: int) -> int:
    """(a+b)^3=a^3+3a^2b+3ab^2+b^3"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a + b) ** 3


def cube_neg(a: int, b: int) -> int:
    """(a-b)^3=a^3-3a^2b+3ab^2-b^3"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a - b) ** 3


def opshn_c(*argus: int) -> int:
    """optional identity cube"""
    for arg in argus:
        if not isinstance(arg, int):
            raise TypeError("this function only for int definition becomes")
    else:
        return sum(argus) ** 3


def coupled(a: int, b: int) -> int:
    """(a+b)(a-b)=a^2-b^2"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return a ** 2 - b ** 2


def one_sentence_joint(x: int, a: int, b: int) -> int:
    """(x+a)(x+b)=x^2+(a+b)x+ab"""
    if not isinstance(x, int) or not isinstance(a, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (x + a) * (x + b)


def o_one_sentence_joint(*argus, x):
    """optional identity one sentence joint"""
    for arg in argus:
        if not isinstance(x, int) or not isinstance(arg, int):
            raise TypeError("this function only for int definition becomes")
    else:
        i_one_sentence_joint = 1
        for i in list(argus):
            i_one_sentence_joint *= x + i
        return i_one_sentence_joint


def fatandthin(a: int, b: int) -> int:
    """a^3+b^3=(a+b)(a^2−ab+b^2)"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return a ** 3 + b ** 3


def fatandthin_n(a: int, b: int) -> int:
    """a^3+b^3=(a-b)(a^2+ab+b^2)"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return a ** 3 - b ** 3


def o_fatandthin(a: int, b: int, n: int) -> int:
    """optional identity fat and thin"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(n, int):
        raise TypeError("this function only for int definition becomes")
    elif n % 2 == 1:
        print("power should odd number be")
    else:
        return a ** n + b ** n


def o_fatandthin_neg(a: int, b: int, n: int) -> int:
    """optional identity fat and thin negative"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(n, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return a ** n - b ** n


def lagrange(a: int, b: int, x: int, y: int) -> int:
    """(a^2+b^2)(x^2+y^2)=(ax+by)^2+(ay−bx)^2"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a ** 2 + b ** 2) * (x ** 2 + y ** 2)


def avlir(a: int, b: int, c: int) -> int:
    """(a+b+c)(a^2+b^2+c^2−ab−ac−bc)=a^3+b^3+c^3−3abc"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(c, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return a ** 3 + b ** 3 + c ** 3 - 3 * a * b * c


def newton_two(a: int, b: int, n: int) -> int:
    """(a+b)^n=a^n+a^(n-1)b+a^(n-2)b^2+...+b^n"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(n, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a + b) ** n


def newton_two_n(a: int, b: int, n: int) -> int:
    """(a-b)^n=a^n-a^(n-1)b-a^(n-2)b^2-...-b^n"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("this function only for int definition becomes")
    if not isinstance(n, int):
        raise TypeError("this function only for int definition becomes")
    else:
        return (a - b) ** n
