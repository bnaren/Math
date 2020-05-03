
# Euclid Algorithm
def gcd_euclid(a, b):
    assert a >= 0 and b >= 0
    while a > 0 and b > 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return max(a,b)
