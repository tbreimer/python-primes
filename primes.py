import math

# Determines if num is prime

# Returns True if prime
# Returns False if composite

def isPrime(num):
    factors = 0

    if (num == 1):
        return False

    if (num < 4):
        return True
    
    for x in range(1, math.ceil(math.sqrt(num))+1):        
        difference = num/x

        if (difference).is_integer():
            factors += 1

            if (factors == 2):
                return False
            
    return True


# Given a start and end as parameters, returns an array of all the prime numbers within the parameters

# Both the beginning and end are inclusive

def isPrimeArray(start, end):
    primes = []
    
    for x in range(start, end+1):
        value = isPrime(x)
        if (value == True):
            primes.append(x)

    return primes

print(isPrimeArray(2000, 3000))





            


    
            
