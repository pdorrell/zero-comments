# See http://www.daniweb.com/software-development/python/threads/377441/is-my-code-too-descriptive for original example

class Alphabet:
    def __init__(self, firstLetter, lastLetter):
        self.firstLetter = firstLetter
        self.lastLetter = lastLetter
        self.size = ord(lastLetter) + 1 - ord(firstLetter)
        
    def contains(self, char):
        return char >= self.firstLetter and char <= self.lastLetter
    
    def charToIndex(self, char):
        return ord(char) - ord(self.firstLetter)
    
    def indexToChar(self, index):
        return chr(ord(self.firstLetter) + index)

class CaesarCipherMachine:
    def __init__(self, lowerCaseAlphabet, upperCaseAlphabet):
        self.lowerCaseAlphabet = lowerCaseAlphabet
        self.upperCaseAlphabet = upperCaseAlphabet
    
    def encryptMessage(self, messageString, shift):
        messageAsCharArray = [char for char in messageString]
        encryptedMessageAsCharArray = [self.encryptChar(char, shift) for char in messageAsCharArray]
        encryptedMessageString = self.charArrayToString(encryptedMessageAsCharArray)
        return encryptedMessageString
    
    def decryptMessage(self, messageString, shift):
        return self.encryptMessage(messageString, -shift)
    
    def charArrayToString(self, charArray):
        return "".join(charArray)
    
    def rotateIndex(self, index, alphabetSize, shift):
        return (index + shift) % alphabetSize
    
    def encryptChar(self, char, shift):
        if self.lowerCaseAlphabet.contains(char):
            return self.encryptCharWithinAlphabet(char, self.lowerCaseAlphabet, shift)
        elif self.upperCaseAlphabet.contains(char):
            return self.encryptCharWithinAlphabet(char, self.upperCaseAlphabet, shift)
        else:
            return char
    
    def encryptCharWithinAlphabet(self, char, alphabet, shift):
        indexInAlphabet = alphabet.charToIndex(char)
        rotatedIndex = self.rotateIndex(indexInAlphabet, alphabet.size, shift)
        encryptedChar = alphabet.indexToChar(rotatedIndex)
        return encryptedChar
    
def demonstrateEncryptionAndDecryption(cipherMachine, plainText, shift, expectedCipherText = None):
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
