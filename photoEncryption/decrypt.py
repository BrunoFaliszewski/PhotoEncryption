from PIL import Image
import numpy as np

def decrypt(image: Image):
        byte_array = np.asarray(image)
        byte_array = byte_array.flatten()

        lengthOfMessage = []
        for i in range(16):
            if byte_array[i]%2 == 0:
                lengthOfMessage.append(0)
            else:
                lengthOfMessage.append(1)
        lengthOfMessage = int("".join(str(x) for x in lengthOfMessage), 2)

        message = []
        for i in range(lengthOfMessage*8):
            if byte_array[i+16]%2 == 0:
                message.append(0)
            else:
                message.append(1)
        message = [message[i:i+8] for i in range(0, len(message), 8)]
        for i in range(len(message)):
            message[i] = chr(int("".join(str(x) for x in message[i]), 2))
        message = "".join(message)
        
        return message