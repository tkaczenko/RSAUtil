import util
from math import gcd

def initSign():
    bitSize = 1000
    p = util.test(util.makeOdd(util.randomString(bitSize)))
    q = util.test(util.makeOdd(util.randomString(bitSize)))

    n = p * q
    m = (p - 1) * (q - 1)

    e = util.makeOdd(util.randomString(bitSize))
    while gcd(e, m) != 1:
        e = util.makeOdd(util.randomString(bitSize))

    d = modinv(e, m)
    return p, q, n, e, d

def calcSign(mess, key, d, n):
    h = xor_strings(mess, key)
    sign = util.powMod(h, d, n)
    return sign

def checkSign(mess, key, sign, e, n):
    h = xor_strings(mess, key)
    H = util.powMod(sign, e, n)
    if H == h:
        return True, h, H
    else:
        return False, h, H

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def xor_strings(xs, ys):
    return sum((ord(x) ^ ord(y)) for x, y in zip(xs, ys))

mess = "Tkachenko"
key = "Andrii"

p, q, n, e, d = initSign()
sign = calcSign(mess, key, d, n)
flag, h, H = checkSign(mess, key, sign, e, n)
print("flag  =", flag)
print("p     =", p)
print("q     =", q)
print("n     =", n)
print("e     =", e)
print("d     =", d)
print("sign  =", sign)
print("h     =", h)
print("H     =", H)
