# See http://www.daniweb.com/software-development/python/threads/377441/is-my-code-too-descriptive for original example

class Alphabet:
    """An Alphabet is a sequence of contiguous characters in the Unicode character set.
    In practice there are two we are interested in - 'a' to 'z' and 'A' to 'Z'."""
    
    def __init__(self, firstLetter, lastLetter):
        """Construct given the first and last letters of the alphabet."""
        self.firstLetter = firstLetter
        self.lastLetter = lastLetter
        self.size = ord(lastLetter) + 1 - ord(firstLetter)
        
    def contains(self, char):
        """Does this alphabet contain the given character?"""
        return char >= self.firstLetter and char <= self.lastLetter
    
    def charToIndex(self, char):
        """What is the zero-based index of the character within this alphabet?
        (No check is made on whether or not the character is actually in the alphabet.)"""
        return ord(char) - ord(self.firstLetter)
    
    def indexToChar(self, index):
        """Given a zero-based index, what is the character? (This method is the inverse of charToIndex.)"""
        return chr(ord(self.firstLetter) + index)

class CaesarCipherMachine:
    """A CaesarCipherMachine is a machine which specifies the lower and upper case alphabets, within
    which each character is encrypted by adding the key value (a number from 0 to one less than the alphabet size, 
    i.e. from 0 to 25) to the index of the character modulo the alphabet size (i.e. 26)"""
    
    def __init__(self, lowerCaseAlphabet, upperCaseAlphabet):
        """Construct from Alphabet objects that describe the locations of lower and upper case alphabets
        within the Unicode character set."""
        self.lowerCaseAlphabet = lowerCaseAlphabet
        self.upperCaseAlphabet = upperCaseAlphabet
    
    def encryptMessage(self, messageString, shift):
        """Encrypt a string, one character at a time, by applying the shift (which is the key value) to
        each character."""
        messageAsCharArray = [char for char in messageString]
        encryptedMessageAsCharArray = [self.encryptChar(char, shift) for char in messageAsCharArray]
        encryptedMessageString = self.charArrayToString(encryptedMessageAsCharArray)
        return encryptedMessageString
    
    def decryptMessage(self, messageString, shift):
        """Decrypt a string, by reversing the shift applied by encryptMessage."""
        return self.encryptMessage(messageString, -shift)
    
    def charArrayToString(self, charArray):
        """Convert an array of characters to a Python string."""
        return "".join(charArray)
    
    def rotateIndex(self, index, alphabetSize, shift):
        """Apply the shift to an index of a character within an alphabet, modulo the size of the alphabet."""
        return (index + shift) % alphabetSize
    
    def encryptChar(self, char, shift):
        """Encrypt on character - if it's lower or upper case letter, then apply the shift, otherwise leave
        the character unchanged."""
        if self.lowerCaseAlphabet.contains(char):
            return self.encryptCharWithinAlphabet(char, self.lowerCaseAlphabet, shift)
        elif self.upperCaseAlphabet.contains(char):
            return self.encryptCharWithinAlphabet(char, self.upperCaseAlphabet, shift)
        else:
            return char
    
    def encryptCharWithinAlphabet(self, char, alphabet, shift):
        """Encrypt a letter within an alphabet (e.g. lower or upper case alphabet), by applying the
        shift to the index of the letter within that alphabet."""
        indexInAlphabet = alphabet.charToIndex(char)
        rotatedIndex = self.rotateIndex(indexInAlphabet, alphabet.size, shift)
        encryptedChar = alphabet.indexToChar(rotatedIndex)
        return encryptedChar
    
def demonstrateEncryptionAndDecryption(cipherMachine, plainText, shift, expectedCipherText = None):
    """Demonstrate the encryption and description of a message by a given shift value, optionally
    checking the result of encryption against an expected cipher text value."""
    print("=============================================================================== ")
    print("plainText = %r, shift = %s" % (plainText, shift))
    cipherText = cipherMachine.encryptMessage(plainText, shift)
    if expectedCipherText != None:
        assert cipherText == expectedCipherText
    print("  cipherText = %r" % cipherText)
    decryptedCipher = cipherMachine.decryptMessage(cipherText, shift)
    print("   decrypted = %r" % decryptedCipher)
    assert decryptedCipher == plainText

caesarCipherMachine = CaesarCipherMachine(lowerCaseAlphabet = Alphabet(firstLetter = 'a', 
                                                                       lastLetter = 'z'), 
                                          upperCaseAlphabet = Alphabet(firstLetter = 'A', 
                                                                       lastLetter = 'Z'))

def rot13(plainText):
    """ROT13 is Caesar cipher with shift 13, which, since 13 + 13 = 26, is self-decrypting."""
    return caesarCipherMachine.encryptMessage(plainText, 13)

def main():
    demonstrateEncryptionAndDecryption(caesarCipherMachine, 
                                       plainText = "the quick brown fox jumps over the lazy dog", 
                                       shift = 3, 
                                       expectedCipherText = "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj")
    
    print("")
    print("How can you tell an extrovert from an introvert at NSA?")
    encipheredAnswer = "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
    answer = rot13(encipheredAnswer)
    print("Answer: %r" % answer)
    
if __name__ == "__main__":
    main()
