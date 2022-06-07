from PIL import Image
import numpy as np

def encrypt(image: Image, message: str):
    byte_array = np.asarray(image)
    photoShape = byte_array.shape
    byte_array = byte_array.flatten()

    binaryMessage = list(map(bin, bytearray(message, 'utf-8')))
    for i in range(len(binaryMessage)):
        binaryMessage[i] = binaryMessage[i][2::]
        binaryMessage[i] = [int(char) for char in binaryMessage[i]]
        for j in range(8-len(binaryMessage[i])):
            binaryMessage[i].insert(0, 0)
    binaryMessage = np.asarray(binaryMessage).flatten()

    lengthOfMessage = list(map(int, list(bin(len(message))[2::])))
    for i in range(16-len(lengthOfMessage)):
        lengthOfMessage.insert(0, 0)
    for i in range(16):
        if byte_array[i]%2 == 0:
            byte_array[i] += lengthOfMessage[i]
        else:
            byte_array[i] += lengthOfMessage[i] - 1

    for i in range(len(message)*8):
        if byte_array[i+16]%2 == 0:
            byte_array[i+16] += binaryMessage[i]
        else:
            byte_array[i+16] += binaryMessage[i] - 1
    byte_array = byte_array.reshape(photoShape)
    byte_array = np.ascontiguousarray(byte_array)

    return Image.fromarray(byte_array)