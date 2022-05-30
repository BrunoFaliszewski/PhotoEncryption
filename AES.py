import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
BLOCK_SIZE = 16

def pad(plainText):
        numberOfBytesToPad = BLOCK_SIZE - len(plainText) % BLOCK_SIZE
        asciiString = chr(numberOfBytesToPad)
        paddingStr = numberOfBytesToPad * asciiString
        paddedPlainText = plainText + paddingStr
        return paddedPlainText

def unpad(plainText):
        lastCharacter = plainText[-1:]
        bytesToRemove = ord(lastCharacter)
        return plainText[:-bytesToRemove]

def encrypt(plain_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    plain_text = pad(plain_text.decode()).encode()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text))
    
def decrypt(cipher_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cipher_text[16:]))
