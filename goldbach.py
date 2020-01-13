"""
Sum of 2 primes exercise
Goal: Create a function to verify Goldbach's conjecture for a range
      between two given positive integers
"""

#Create a list of primes up to ubound (inclusive)
def primes(ubound):
    """
    Creates a list of prime integers between 0 and ubound (inclusive)
    Returns list
    ubound must be integer higher than 2
    """
    if not isinstance(ubound,int) or ubound<=2:
        raise ValueError('Primes: upper bound (ubound) must be an integer higher than 2')
    def check(i):
        """
        Check if i is prime
        Returns boolean
        
        Checks all integers 1-i exclusive to see if there are any other
        factors for i. If none are found, i is prime.
        """
        output = True
        for x in range(2,i):
            if i % x == 0:
                output = False
                break
        return output
    
    primes = [2]
    for i in range(3,ubound+1,2):
        if check(i): primes.append(i)
    return primes

#Check all even numbers 4-ubound to see if two primes add to number
def goldbach(ubound,lbound = 4,gb1 = True):
    """
    Check all even integers between 4 and ubound (inclusive) to verify
    Goldbachs first conjecture:
        Every even integer greater than 2 can be written as the sum of two primes
    
    Set gb1 = False to verify Goldbachs second conjecture:
        Every integer greater than 5 can be written as the sum of three primes
        
    Uses a brute force approach to find satisfying equation for each integer 
    in range.
    
    Raises a value error if an exception to Goldbach is found.
    """
    if not isinstance(ubound,int) or not isinstance(lbound,int):
        raise ValueError('Goldbach: ubound and lbound must be integers')
    if lbound>=ubound:
        raise ValueError('Goldbach: ubound must be greater than lbound')
    lbound = max(lbound,(6 - (2*gb1)))
    ubound = max(ubound,(7 - (2*gb1)))
    def solvegb(i, primes):
        """
        Checks possible pairs/trios to find an equation that satisfies
        Goldbach's conjecture. Raises a value error if any exceptions to the
        conjecture are found. Otherwise returns satisfying equation as string.
        
        Uses a series of subsets of primes that include only viable integers
        For example:
            if i = 10, subset1 = [7,5,3,2]
            For the first prime (7), subset2 is (subset1 <= (10-7)) or
                [3,2]
        """
        output = ''
        subset = [x for x in primes[::-1] if x <= i]
        for n in subset:
            if output: break
            subset2 = [x for x in subset if x <= (i-n)]
            for m in subset2:
                if gb1 and (m+n) == i:
                    output = f'{i} = {n} + {m}'
                    break
                elif not gb1:
                    if output: break
                    subset3 = [x for x in subset2 if x <= (i-n-m)]
                    for l in subset3:
                        if (m+n+l) == i:
                            output = f'{i} = {n} + {m} + {l}'
                            break
                    
        if not output:
            raise ValueError(f'FAILURE: NO EQUATION FOUND FOR {i}')
        return output
    
    prime = primes(ubound)
    equations = list()
    for i in range(lbound, ubound+1, 1 + gb1):
        equations.append(solvegb(i, prime))
    return(equations)

gb = goldbach(100)
#gb = goldbach(100, gb1=False)
#gb = goldbach(1000, lbound=500, gb1=False)
[print(x) for x in gb]

#print(primes(1000))