Caesar Cipher
=============

Wikipedia link: [Caesar Cipher](http://en.wikipedia.org/wiki/Caesar_cipher)

In a Caesar cipher, the key is a number from 0 to 25 (so the key space isn't
very large at all). Letters of the alphabet are encrypted by adding the key to
the letter's position in the alphabet, modulo 26. Anything that is not a letter
remains unchanged. To decrypt, you just subtract the same key, modulo 26.

ROT13 is the Caesar cipher with key 13. Since 13 = -13 mod 26, ROT13 is self-decrypting.
