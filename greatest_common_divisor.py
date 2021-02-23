# Naive algorithm (very slow when a+b has more than 20 digits)
def gcd_slowest(a,b):
    best = 0
    for d in range(1,a+b):
        if a%d == 0 and b%d == 0:
            best = d
    return best

def gcd_slow(a,b):
    upper_bound = min(a,b)
    for d in range(upper_bound, 0, -1):
        if a%d == 0 and b%d == 0:
            best = d
            break
    return best

# gcd fast
# It uses the lemma: be a' the remainder of the division a/b, then gcd(a,b)=gcd(a',b)=gcd(b,a') ::::::: Page 934 on Introductions to algorithims Cromen
def euclid_gcd(x,y):
    a = max(x,y)
    b = min(x,y)
    if b == 0:
        return a
    else:
        a_mod_b = a % b
        print(f'--------------->gcd({a_mod_b},{b})')
        return euclid_gcd(a_mod_b, b)
"""
#Alternatively
def euclid_gcd(a,b):
    if b == 0:
        return a
    else:
        a_mod_b = a % b
        return euclid_gcd(b, a_mod_b)
"""

try:
    while True:
        userInput = input('Type two numbers: ')
        l = userInput.split(' ')
        a = int(l[0])
        b = int(l[1])
        print(f'GCD({a},{b}) = {euclid_gcd(a,b)}')
except KeyboardInterrupt:
    print('Ended loop. ')
