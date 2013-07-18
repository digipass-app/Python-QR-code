import re, sys


def isPrime(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


N = int(sys.argv[1]) # number of primes wanted (from command-line)
M = 100              # upper-bound of search space
l = list()           # result list

while len(l) < N:
    l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
    M += 100                                # increment upper-bound

print l[:N] # print result list limited to N elements
