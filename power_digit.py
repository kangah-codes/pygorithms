def powerDigit(exp):
    ans = 2**exp
    sum = 0
    while ans > 0:
        print(ans%10)
        sum += ans%10
        ans //= 10
    return sum

print(powerDigit(15))
