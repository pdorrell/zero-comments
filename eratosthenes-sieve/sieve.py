
class SieveOfEratosthenes:
    
    def __init__(self, sieveSize):
        self.sieveSize = sieveSize
        
    def initialiseSieve(self):
        self.couldBePrime = [True]*(self.sieveSize+1);
        self.couldBePrime[0] = False
        self.couldBePrime[1] = False
        self.nextNumberToCheck = 0
        
    def generatePrimes(self):
        self.initialiseSieve()
        pastTheSquareRootOfSize = False
        while self.nextNumberToCheck <= self.sieveSize:
            candidatePrime = self.nextNumberToCheck
            if self.couldBePrime[candidatePrime]:
                nextPrimeFound = candidatePrime
                if not pastTheSquareRootOfSize:
                    if nextPrimeFound*nextPrimeFound > self.sieveSize:
                        pastTheSquareRootOfSize = True
                    if not pastTheSquareRootOfSize:
                        self.markMultiplesNotPrime(nextPrimeFound)
                yield nextPrimeFound
            self.nextNumberToCheck += 1
            
    def markNumberAsComposite(self, number):
        self.couldBePrime[number] = False
            
    def markMultiplesNotPrime(self, prime):
        multipleOfPrimeToBeMarked = prime*prime
        while (multipleOfPrimeToBeMarked <= self.sieveSize):
            self.markNumberAsComposite(multipleOfPrimeToBeMarked)
            multipleOfPrimeToBeMarked += prime
            
def main():
    SIZE = 100
    sieve = SieveOfEratosthenes(SIZE)
    print ("Prime numbers up to %s:" % SIZE)
    for prime in sieve.generatePrimes():
        print (" %s" % prime)


if __name__ == "__main__":
    main()
