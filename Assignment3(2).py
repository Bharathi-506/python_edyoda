def isPrime(a) :
    count = 0
    for i in range(1, a+1) :
        if a % i == 0 :
            count = count + 1
        if count == 2:
            return True
n = 2
N = int(input("Enter the value of N : "))
while n < N :
    if isPrime(n) == True and isPrime(n+2) == True:
        print("({0},{1})".format(n, n+2), end = "    ")
    n = n + 1