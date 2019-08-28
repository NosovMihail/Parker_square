from math import sqrt
import time


def isint(n):
    return int(n) == float(n)


def search(k, start):
    for num in range(start, int(sqrt(k / 2))):
        if isint(sqrt(k - num * num)):
            return num
    return 0


def passed(main, first, second, third):
    return first * first + second * second + third * third == main


startnum = 1000
endnum = 1000000
timing = time.time()
for n in range(startnum, endnum):
    for a in range(1, int(sqrt(n / 3))):
        num1 = search(n - a * a, 1)
        num11 = n - a * a - num1 * num1
        if num1 != 0 and num11 != 0 and num1 != a:
            num2 = search(n - a * a, num1 + 1)
            num22 = n - a * a - num2 * num2
            if num2 != 0 and num22 != 0 and num2 != a:
                num3 = search(n - a * a, num2 + 1)
                num33 = n - a * a - num3 * num3
                if num3 != 0 and num33 != 0 and num3 != a:
                    num4 = search(n - a * a, num3 + 1)
                    num44 = n - a * a - num4 * num4
                    if num4 != 0 and num44 != 0 and num4 != a:
                        if (passed(n, num1, num2, num3) or passed(n, num11, num22, num33)) or (
                                passed(n, num1, num2, num33) or passed(n, num11, num22, num3)) or (
                                passed(n, num1, num22, num3) or passed(n, num11, num2, num33)) or (
                                passed(n, num11, num2, num3) or passed(n, num1, num22, num33)):
                            print(n, a, num1, num2, num3, num4)
    if n % 1000 == 0:
        print(n, time.time()-timing)
