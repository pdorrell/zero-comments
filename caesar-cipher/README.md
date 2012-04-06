Caesar Cipher
=============

Wikipedia link: [Caesar Cipher](http://en.wikipedia.org/wiki/Caesar_cipher)

In a Caesar cipher, the key is a number from 0 to 25 (so the key space isn't
very large at all). Letters of the alphabet are encrypted by adding the key to
the letter's position in the alphabet, modulo 26. Upper and lower case letters
are encrypted by the same algorithm, but case must be preserved, so that it
reappears correctly when the cipher is decrypted. Anything that is not a letter
remains unchanged when encrypted (so apart from being a very weak cipher for
encrypting written text, it is a truly awful cipher for encrypting credit card numbers).

To decrypt, you just subtract the same key, modulo 26.

ROT13 is the Caesar cipher with key 13. Since 13 = -13 mod 26, ROT13 is self-decrypting.

Code Notes
----------

To correctly handle lower case, upper case and non-alphabetic characters, the program
provides the notion of an **Alphabet**, which is a sequence of characters in the character
encoding. There is one "Alphabet" for lower case letters, and a second one for upper case letters.

For each character to be encrypted, the program must decide if it is in either of those
alphabets: if it is in an alphabet, then it is encrypted within that alphabet, otherwise, if it
is not in either of those two alphabets (because it is not alphabetic), it remains unchanged.

The program also takes advantage of the fact that "a" to "z" and "A" to "Z" are each contiguous
sequences of characters in the Unicode character encoding, which is what Python 3 uses to 
encode and decode characters (via the functions **chr** and **ord**). Thus, for example, the 
**index** of a lower case character such as "f" is equal to the
character code for "f" minus the character code for "a". The actual encryption can then be described
as addition of the key (or "shift") to the index, modulo 26.

Encryption is implemented by describing how to encrypt each character in turn.

It is not necessary to repeat this logic for decryption, because decryption by a shift **N** 
can be implemented directly as encryption by a shift of **-N**.
