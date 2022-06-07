# photoEncryption

photoEncryption is library for encrypting and decrypting messages in images

## Instalation

```bash
pip install photoencryption
```
## Usage

**Encryption**

```python
from photoEncryption.encrypt import *
from PIL import Image

img = Image.open('img.jpg')
encryptedImage = encrypt(img, 'This is encrypted message')
encryptedImage.save('encryptedImage.bmp')
```

**Decryption**

```python
from photoEncryption.decrypt import *
from PIL import Image

img = Image.open('encryptedImage.bmp')
print(decrypt(img))
```