# divide the number n by 2 m times
def divide(n, m):
    return n >> m


# multiply the number n by 2 m times
def multiply(n, m):
    return n << m


# check odd or even
def isOdd(n):
    if n & 1:
        return True
    else:
        return False


# store 32 flags in a variable
def flagging():
    flag = 0

    # set flag 1 be true
    flag |= 1

    # set flag 2 be true
    flag |= 2

    # check if 1st flag is true
    if flag & 1:
        print("Flag 1 is true.")
    else:
        print("Flag 1 is false.")

    # check if 2nd flag is true
    if flag & 2:
        print("Flag 2 is true.")
    else:
        print("Flag 2 is false.")

    # check if 3rd flag is true
    if flag & 4:
        print("Flag 3 is true.")
    else:
        print("Flag 3 is false.")

    # reset flags
    flag = flag & (~(1 << 0))
    flag = flag & (~(1 << 1))
    flag = flag & (~(1 << 2))


# find 2's complement
def findTwoComplement(n):
    return ~n + 1


# toggle case
def toggleCase(a):
    for i in range(len(a)):
        a = a[:i] + chr(ord(a[i]) ^ 32) + a[i + 1:]
    return a


# swap number
def swap(a, b):
    print("a =", a, "b =", b)
    a ^= b
    b ^= a
    a ^= b
    print("a =", a, "b =", b)


if __name__ == "__main__":
    print(divide(10, 1))

    print(multiply(10, 2))

    print(isOdd(3))
    print(isOdd(4))

    flagging()

    print(findTwoComplement(12))
    print(findTwoComplement(-32))

    print(toggleCase('HelloWorld'))

    swap(1, 24)
