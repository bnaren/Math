
# Find the GCD based on the Euclid Algorithm
def gcd_euclid(a, b):
    assert a >= 0 and b >= 0
    while a > 0 and b > 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return max(a,b)

def extended_gcd(a, b):
    # ax + by = d
    # given: a, b
    # find x, y and d
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)

