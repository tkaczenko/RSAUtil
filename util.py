import random

def randomString( len ):
    list = [str(random.randint(0,1)) for i in range(len)]
    return int(''.join(list), 2)

def makeOdd( a ):
    a_bin = bin(a)[2:]
    a_bin = '1' + a_bin[1:-1] + '1'
    return int(a_bin, 2)

def eratosthenes( len ):
    multiples = set()
    for i in range(2, len):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, len, i))

def checkDivisibility( num ):
    return all(num % x != 0 for x in eratosthenes(2000))

def MillerRabin( n, k = 50 ):
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def test( num ):
    while (not MillerRabin(num) or not checkDivisibility(num)):
        num += 2
    return num

def powMod( a, b, n, flag = True ):
    d = 1
    b_bin = bin(b)[2:]
    for i in range(len(b_bin)):
        d = (d * d) if not flag else (d * d) % n
        if b_bin[i] == '1':
            d = (d * a) if not flag else (d * a) % n
    return d
