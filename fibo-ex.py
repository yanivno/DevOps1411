def fibo(n):
    if n <= 1:
        return n
    print(n-1)
    print(n-2)
    return fibo(n-1) + fibo(n-2)

def recoursive_fibo(n):
    nMinusOne = 1
    nMinusTwo = 0
    result = 0
    for i in range(1,n-1):
        result = nMinusTwo + nMinusOne
        nMinusTwo = nMinusOne
        nMinusOne = result
    return result

#0,1,1,2,3,5,8,13,21,34
print(recoursive_fibo(9))