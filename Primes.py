#Various functions working with prime numbers;
#findFactors can find all the prime factors of a given number
#isPrime returns whether a given number is prime or not
#listPrimes creates and prints a list of all the primes up to an input

import math

factors = []
primes = []

def findFactors(n):

  listPrimes(n)

  for i in range(2, int(n/2)):

    if (n/i) in primes:
      factors.append(n/i)

  print(factors)

def isPrime(n):

  if n == 2:
    return True
  
  if n % 2 == 0:
    return False

  for i in range(3, int(math.sqrt(n))+1, 2):
    if isPrime(i)==True:
      if n % i == 0:
        return False      

  return True

def listPrimes(n):

  for i in range(2,n):

    if isPrime(i) == True:

      primes.append(i)
