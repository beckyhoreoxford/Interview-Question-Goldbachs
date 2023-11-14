import pytest

#isPrime(n)
#input: int(n) && 0<=n
#output: True if n is prime, False otherwise
#time complexity: O(sqrt(n))
#space complexity: O(1)
def isPrime(n):
    assert(isinstance(n,int) and 0<=n)
    if (n <= 1):
        return False
    s = int(n**0.5)
    i = 2
    while (i<=s):
        if n%i == 0:
            return False
        i += 1
    return True


#FINDALLPRIMES(n)
#input: int(n) && 2<=n
#time complexity: O(nlog(log(n)))
#space complexity: O(n)
def findAllPrimes(n):
    assert(isinstance(n,int) and 2<=n)
    #P: a boolean array of size n, indexed 0..n, P[i] is true if i is prime and vice versa
    P = [1]*n
    P[0] = 0
    P[1] = 0

    s = int(n**0.5)
    p = 2
    while(p<=s):
        if P[p] == 1:
            #if p hasn't been crossed out yet, cross off all multiples of p strictly greater than p
            #but we only have to start at p^2, because smaller multiples of p will have already been crossed out
            #ie, cross out: p^2,     p^2 + p,    p^2 + 2p,   p^2 + 3p,   ...up to and including n
            k = p*p
            while(k < n):
                P[k] = 0
                k+=p
        p+=1
    #in each iteration we're crossing off <= n/2 then n/3 then n/5... elements (sum of the reciprocal of the primes)
    #so the total number of constant operations is: n*(1/2 + 1/3 + 1/5 + 1/7 + ...) ~= log(log(n))

    for i in range(2,n//2 + 1):
        if P[i] and P[n-i]:
        #alternative: if isPrime(i) and isPrime(n-i)
            print("{},{}".format(i,n-i))
    print("")

#GETINPUT
#output: n: even integer strictly greater than 2
def getInput():
    safeInput = False
    while(not safeInput):
        n = input("Input an even integer strictly greater than 2: ")
        #sanitise input
        #check input is numerical
        if (not n.isdigit()):
            print("Your input is not a plain numerical digit, please try again.")
        else:
            n = int(n)
            #check input is even and strictly greater than 2
            if (n <= 2):
                print("Your input is not strictly greater than 2, please try again.")
            elif (n%2 != 0):
                print("Your input is not an even number, please try again.")
            else:
                safeInput = True
    return n
    

#GOLDBACHS()
def goldbachs():
    n = getInput()
    #find a pair of primes
    print("\nHere is a pair of primes which sum to {}:".format(n))
    #O(n*sqrt(n)), but v. likely to be much less bad than that
    found = False
    i = 2
    while(not found):
        if isPrime(i) and isPrime(n-i):
            print("{},{}".format(i,n-i))
            found = True
        else:
            i += 1
    
    #Give use the option to find all pairs of primes
    safeInput = False
    while (not safeInput):
        ans = input("\nWould you like to see all pairs of primes which sum to {}? (Y/N): ".format(n))
        if ans in ["Y", "y", "yes", "Yes"]:
            safeInput = True
            findAllPrimes(n)
        elif ans in ["N", "n", "no", "No"]:
            safeInput = True
        else:
            print("Your input is not in the correct form, please try again.")

goldbachs()