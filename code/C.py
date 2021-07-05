
def countPrimes(n):
    if n==0:
         return 0
    def IsPrime(n):
        sqrt_n = int(n**0.5)
        for i in range(2,sqrt_n+1):
            if (n%i)==0:
                return 0
        return 1
    count = 0 
    for i in range(2,n):
        count+=IsPrime(i)
    return count
while True:
    a = input()
    if  not a:
        break
    else:
         a=int(a)
         ans=countPrimes(a+1)
         print(ans)