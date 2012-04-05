Sieve of Eratosthenes
=====================

Wikipedia link: [Sieve of Eratosthenes](Sieve of Eratosthenes)

The Sieve of Eratosthenes is an algorithm for finding all prime numbers
up to a certain limit, which works as follows:

* Decide up to what number you want calculate the primes. Call this number **N**.
* List all numbers from 1 to N
* Cross out 1 as not being a prime
* Repeat the following step, until all primes up to N have been found:
   * Pick the first number not yet crossed out.
   * This number is the next prime that you have found. Call this number **P**.
   * Cross out all multiples of **P** greater than **P** itself.

There are various refinements of this algorithm which improve efficiency. Two which
I have used in the accompanying code are:

* The first multiple of **P** that you need to cross out is **P**<sup>2</sup>, because
every smaller multiple of **P** must also be a multiple of some prime smaller than **P**,
and must therefore already have been crossed out.
* Once you get to **P** where **P**<sup>2</sup> is greater than **N**, you know that you
don't have to check any multiples at all -- you can just read off the remaining numbers
not crossed out as primes.
