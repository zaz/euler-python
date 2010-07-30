from __future__ import generators

def getPrimes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    dictionary = {}  # map composite integers to primes witnessing their compositeness
    i = 2   # first integer to test for primality
    while True:
        p = dictionary.pop(i, None)  # remove item i from the dictionary
        if p:  # if i has been marked as a non-prime:
            multiple = p + i  # multiple = i^2 + i
            while multiple in dictionary: multiple += p  # search for a multiple of i (starting at i^2 + i), that's not in the dictionary
            dictionary[multiple] = p  # add p to the dictionary with at [multiple]
        else:  # if i has not been marked as a non-prime (then i must be a prime):
            dictionary[i*i] = i  # mark i^2 as a non-prime
            yield i
        i += 1

def getTriangles():
    '''Yields the sequence of triangle numbers.'''
    triangle = 1
    base = 1
    while True:
        yield triangle
        base += 1
        triangle += base        

def isFactor(number,factor):
    if number % factor: return False  # If it is not a factor, return false
    return True  # Otherwise, return true

def isPrime(number):
    '''Tests if a number is prime.'''
    number = abs(int(number))
    if number < 2: return False  # If the number is less than 2: return false
    if number == 2: return True  # If the number is 2: return true
    if not number & 1: return False  # If the number is odd: return false
    i = 2
    while i * i <= number:  # While i squared is less than or equal to number:
        if number % i == 0: return False  # If the remainder of number/i = 0: return false
        i += 1  # Increment 
    return True  # Return true

def getFactors_forSingleNumber(number):
    a = 1
    b = 0
    factors = []
    while a <= number:
        if isFactor(number,a):
            if factors.count(a) > 0: break  # If the number is already in the list (then we must have reached the halfway point): break
            factors.insert(b,a)  # Add the factor
            if a != a/number:  # If the factors twin is not identical:
                factors.insert(len(factors)-b,number/a)  # Add the factor's twin
            b += 1
        a += 1
    return factors

def getFactors(number):
    if type(number).__name__ == 'list':
        factors = []
        for item in list:
            itemFactors = getFactors_forSingleNumber(item)
            if type(itemFactors).__name__ == 'list':
                factors.extend(smallNumber)
            else: factors.append(smallNumber)
        return factors
    else: return getFactors_forSingleNumber(number)

def getPrimeFactors_inFull_forSingleNumber(factor):
    if isPrime(factor): return [factor]
    primeFactors = []
    for number in xrange(2,factor):
        if factor % number == 0:
            smallNumber = getPrimeFactors_inFull(number)
            bigNumber = getPrimeFactors_inFull(factor/number)
            primeFactors.extend(smallNumber)  
            primeFactors.extend(bigNumber)
            return primeFactors
    return [1]

def getPrimeFactors_inFull(number):
    factors = []
    if type(number).__name__ == 'list':
        for item in number:
            item = abs(int(item))  # Turn item into a positive integer if it is not already
            if item < 2: continue
            itemFactors = getPrimeFactors_inFull_forSingleNumber(item)
            if type(itemFactors).__name__ == 'list':
                factors.extend(itemFactors)      
            else: factors.append(itemFactors)
        factors.sort()
        return factors
    else:
        factors.extend(getPrimeFactors_inFull_forSingleNumber(number))
        return factors

def getPrimeFactors_inPowers(factor):
    originalFactors = getPrimeFactors_inFull(factor)
    newFactors = [[],[]]  # newFactors[0] contains the numbers, newFactors[1] contains the sum of powers
    for originalFactor in originalFactors:
        if newFactors[0].count(originalFactor) > 0:  # If number is already in the list
            newFactors[1][newFactors[0].index(originalFactor)] += 1  # Add 1 to it's power
        else: 
            newFactors[0].append(originalFactor)  # Add the number to the list
            newFactors[1].append(1)  # Add 1 as it's power
    return newFactors

def getPrimeFactors_inMaxPowers(factors):
    newFactors = [[],[]]
    for number in factors:
        originalFactors = getPrimeFactors_inPowers(number)
        i = 0
        while i < len(originalFactors[0]):
            if newFactors[0].count(originalFactors[0][i]) > 0:  # If number is already in the list
                if newFactors[1][newFactors[0].index(originalFactors[0][i])] < originalFactors[1][i]:  # Use the biggest power out of the two
                    newFactors[1][newFactors[0].index(originalFactors[0][i])] = originalFactors[1][i]
            else: 
                newFactors[0].append(originalFactors[0][i])  # Add the number to the list
                newFactors[1].append(originalFactors[1][i])  # Add it's power
            i += 1
    return newFactors

# MATH INFO
#     Prime Numbers:
#         0 and 1 are not prime numbers.
#         2 is the only even prime number.
#
#     Prime Factors:
#         Prime factors are often displayed as powers (e.g: 24 = 2^3 x 3 ),
#         Rather than in full (e.g: 12 = 2 x 2 x 2 x 3 ).
#
#     Factors:
#         Factors come in pairs (e.g: 20/1=20 [1 & 20], 20/2=10 [2 & 10], etc. ).
#
