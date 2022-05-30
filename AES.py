import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
BLOCK_SIZE = 16

def pad(plain_text):
        number_of_bytes_to_pad = BLOCK_SIZE - len(plain_text) % BLOCK_SIZE
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

def unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]

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
# message=input("Enter message to encrypt: ")
# key = input("Enter encryption key: ")
# encrypted_msg = encrypt(message.encode(), key)
# print("Encrypted Message:", encrypted_msg)
# decrypted_msg = decrypt(encrypted_msg, key)
# print("Decrypted Message:", bytes.decode(decrypted_msg))