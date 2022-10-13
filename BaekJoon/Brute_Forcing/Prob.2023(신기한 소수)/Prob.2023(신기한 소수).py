n=int(input())

primeNum = [2,3,5,7]
oddNum = [1,3,5,7,9]

def isPrime(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i==0: return False
    return True

def solve(limit,cnt,num):
    if (limit<=cnt): return print(num)
    for odd in oddNum:
        nextNum = num*10 + odd
        if isPrime(nextNum):
            solve(limit,cnt+1,nextNum)

for prime in primeNum:
    solve(n,1,prime)
