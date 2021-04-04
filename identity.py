def factorial(n: int) -> int:
    '''of factorial for computing
    multiplication 1 until the n use becomes'''
    if not isinstance(n, int):
        raise TypeError('this function only for int definition becomes')
        return None
    elif n < 0:
        raise ValueError('this function for number \
                         negative definition not becomes')
        return None
    elif n == 0:
        return 1
    else:
        factorial1 = n * factorial(n-1)
        return factorial1


def isq(a: int, b: int) -> int:
    '''(a+b)^2=a^2+2ab+b^2'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        Isq = (a+b)**2
        return Isq


def iisq(a: int, b: int) -> int:
    '''(a-b)^2=a^2-2ab+b^2'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        IIsq = (a-b)**2
        return IIsq


def square_3(a: int, b: int, c: int) -> int:
    '''(a+b+c)^2=a^2+b^2+c^2+2ab+2ac+2bc'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(c, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        square_3 = (a+b+c)**2
        return square_3


def square_3_neg(a: int, b: int, c: int) -> int:
    '''(a+b-c)^2=a^2+b^2+c^2+2ab-2ac-2bc'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(c, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        square_3_neg = (a+b-c)**2
        return square_3_neg


def opshn_s(*argus: int) -> int:
    '''optional identity square'''
    for arg in argus:
        if not isinstance(arg, int):
            raise TypeError('this function only for int definition becomes')
            return None
    else:
        opshn_s = sum(argus)**2
        return opshn_s


def opshn_s_neg(endneg: int, *argus: int) -> int:
    '''optional identity square negative'''
    for arg in argus:
        if not isinstance(arg, int) or not isinstance(endneg, int):
            raise TypeError('this function only for int definition becomes')
            return None
    else:
        sumarg = sum(argus)
        opshn_s_neg = (sumarg-endneg)**2
        return opshn_s_neg


def cube(a: int, b: int) -> int:
    '''(a+b)^3=a^3+3a^2b+3ab^2+b^3'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        cube = (a+b)**3
        return cube


def cube_neg(a: int, b: int) -> int:
    '''(a-b)^3=a^3-3a^2b+3ab^2-b^3'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        cube_neg = (a-b)**3
        return cube_neg


def opshn_c(*argus: int) -> int:
    '''optional identity cube'''
    for arg in argus:
        if not isinstance(arg, int):
            raise TypeError('this function only for int definition becomes')
            return None
    else:
        opshn_c = sum(argus)**3
        return opshn_c


def coupled(a: int, b: int) -> int:
    '''(a+b)(a-b)=a^2-b^2'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        coupled = a**2-b**2
        return coupled


def one_sentence_joint(x: int, a: int, b: int) -> int:
    '''(x+a)(x+b)=x^2+(a+b)x+ab'''
    if not isinstance(x, int) or not isinstance(a, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        one_sentence_joint = (x+a)*(x+b)
        return one_sentence_joint


def o_one_sentence_joint(x, *argus):
    '''optional identity one sentence joint'''
    for arg in argus:
        if not isinstance(x, int) or not isinstance(arg, int):
            raise TypeError('this function only for int definition becomes')
            return None
    else:
        for o in list(argus):
            o_one_sentence_joint = 1
            o_one_sentence_joint *= (x+o)
        return o_one_sentence_joint


def fatandthin(a: int, b: int) -> int:
    '''a^3+b^3=(a+b)(a^2−ab+b^2)'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        fatandthin = a**3+b**3
        return fatandthin


def fatandthin_n(a: int, b: int) -> int:
    '''a^3+b^3=(a-b)(a^2+ab+b^2)'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        fatandthin_n = a**3-b**3
        return fatandthin_n


def o_fatandthin(a: int, b: int, n: int) -> int:
    '''optional identity fat and thin'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(n, int):
        raise TypeError('this function only for int definition becomes')
        return None
    elif n % 2 == 1:
        print('power should odd number be')
        return None
    else:
        o_fatandthin = a**n+b**n
        return o_fatandthin


def o_fatandthin_neg(a: int, b: int, n: int) -> int:
    '''optional identity fat and thin negative'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(n, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        o_fatandthin_neg = a**n-b**n
        return o_fatandthin_neg


def lagrange(a: int, b: int, x: int, y: int) -> int:
    '''(a^2+b^2)(x^2+y^2)=(ax+by)^2+(ay−bx)^2'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        lagrange = (a**2+b**2)*(x**2+y**2)
        return lagrange


def avlir(a: int, b: int, c: int) -> int:
    '''(a+b+c)(a^2+b^2+c^2−ab−ac−bc)=a^3+b^3+c^3−3abc'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(c, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        avlir = a**3+b**3+c**3-3*a*b*c
        return avlir


def newton_two(a: int, b: int, n: int) -> int:
    '''(a+b)^n=a^n+a^(n-1)b+a^(n-2)b^2+...+b^n'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(n, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        newton_two = (a+b)**n
        return newton_two


def newton_two_n(a: int, b: int, n: int) -> int:
    '''(a-b)^n=a^n-a^(n-1)b-a^(n-2)b^2-...-b^n'''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('this function only for int definition becomes')
        return None
    if not isinstance(n, int):
        raise TypeError('this function only for int definition becomes')
        return None
    else:
        newton_two = (a-b)**n
        return newton_two
