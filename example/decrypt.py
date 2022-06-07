from tkinter import *
from tkinter import filedialog
from photoEncryption.decrypt import *
from PIL import Image, ImageTk
import numpy as np
import AES

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Photo Encryption')
        self.state('zoomed')

        self.selectIMGButton = Button(self, text="Select Image")
        self.selectIMGButton['command'] = self.selectIMG
        self.selectIMGButton.pack()

        self.passwordLabel = Label(self, text="Password")
        self.passwordLabel.pack()

        self.passwordInput = Text(self, width=30, height=1)
        self.passwordInput['state'] = 'disable'
        self.passwordInput.pack() 

        self.decryptButton = Button(self, text="Decrypt")
        self.decryptButton['command'] = self.decrypt
        self.decryptButton['state'] = 'disable'
        self.decryptButton.pack()

        self.decryptedText = Text(self, width=60, height=3)
        self.decryptedText['state'] = 'disable'
        self.decryptedText.pack()

    def decrypt(self):
        self.passwordString = self.passwordInput.get('1.0', 'end')
        self.decryptedText['state'] = 'normal'

        self.message = decrypt(self.image)

        self.message = AES.decrypt(self.message.encode(), self.passwordString)
        self.decryptedText.insert('1.0', self.message)

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File", '.bmp')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight()-self.selectIMGButton.winfo_height())
        self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.pack()

        self.decryptButton['state'] = 'normal'
        self.passwordInput['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()
