

class SieveEratosthenes:
    
    def __init__(self, sieveSize):
        self.sieveSize = sieveSize
        self.couldBePrime = [True]*(sieveSize+1);
        self.couldBePrime[0] = False
        self.couldBePrime[1] = False
        self.nextNumberToCheck = 0
        
    def generatePrimes(self):
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
        multipleOfPrime = prime*prime
        while (multipleOfPrime <= self.sieveSize):
            self.couldBePrime[multipleOfPrime] = False
            multipleOfPrime += prime
            
            
def main():
    SIZE = 100
    sieve = SieveEratosthenes(SIZE)
    print ("Prime numbers up to %s:" % SIZE)
    for prime in sieve.generatePrimes():
        print (" %s" % prime)


if __name__ == "__main__":
    main()
