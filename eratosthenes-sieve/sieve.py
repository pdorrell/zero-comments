
class SieveOfEratosthenes:
    """Class representing a Sieve of Eratosthenes of a given size"""
    
    def __init__(self, sieveSize):
        """Construct, given the sieve size."""
        self.sieveSize = sieveSize
        
    def initialiseSieve(self):
        """Initialise the sieve state, ready to start generating primes"""
        self.couldBePrime = [True]*(self.sieveSize+1);
        self.couldBePrime[0] = False
        self.couldBePrime[1] = False
        self.nextNumberToCheck = 0
        
    def generatePrimes(self):
        """Generator to yield all the primes from 2 up to the sieve size."""
        self.initialiseSieve()
        pastTheSquareRootOfSize = False
        while self.nextNumberToCheck <= self.sieveSize:
            if self.couldBePrime[self.nextNumberToCheck]:
                prime = self.nextNumberToCheck
                if not pastTheSquareRootOfSize:
                    if prime*prime > self.sieveSize:
                        pastTheSquareRootOfSize = True
                    if not pastTheSquareRootOfSize:
                        self.markMultiplesNotPrime(prime)
                yield prime
            self.nextNumberToCheck += 1
            
    def markMultiplesNotPrime(self, prime):
        """Having found a new prime, mark as not prime all the multiples of
        that prime from its square up to the largest multiple in the sieve."""
        multipleOfPrime = prime*prime
        while (multipleOfPrime <= self.sieveSize):
            self.couldBePrime[multipleOfPrime] = False
            multipleOfPrime += prime
            
def main():
    """Generate and print all primes up to 100."""
    SIZE = 100
    sieve = SieveOfEratosthenes(SIZE)
    print ("Prime numbers up to %s:" % SIZE)
    for prime in sieve.generatePrimes():
        print (" %s" % prime)


if __name__ == "__main__":
    main()
