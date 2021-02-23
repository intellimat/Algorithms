def euclid_gcd(a,b):
    if b == 0:
        return a
    else:
        a_mod_b = a % b
        return euclid_gcd(b, a_mod_b)


def lcm(a,b):
    gcd_ab = euclid_gcd(a,b)
    lcm = ( a//gcd_ab ) * b  # since gcd_ab divides also a, we first divide a by gcd_ab and then we multiply by b (more efficient)
    return lcm

def lcm_slow(a,b):
    for lcm in range(1, a*b + 1):
        if lcm % a == 0 and lcm % b == 0:
            return lcm
    return a*b


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))