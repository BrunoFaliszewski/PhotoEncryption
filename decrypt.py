from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Photo Encryption')
        self.geometry('500x500')

        self.selectIMGButton = Button(self, text="Select Image")
        self.selectIMGButton['command'] = self.selectIMG
        self.selectIMGButton.pack()

        self.decryptButton = Button(self, text="Decrypt")
        self.decryptButton['command'] = self.decrypt
        self.decryptButton['state'] = 'disable'
        self.decryptButton.pack()

        self.decryptedString = StringVar()
        self.decryptedText = Label(self, textvariable=self.decryptedString)
        self.decryptedText.pack()

    def decrypt(self):
        self.byte_array = np.asarray(self.image)
        self.photoShape = self.byte_array.shape
        self.byte_array = self.byte_array.flatten()
        self.lengthOfMessage = []
        for i in range(10):
            if self.byte_array[i]%2 == 0:
                self.lengthOfMessage.append(0)
            else:
                self.lengthOfMessage.append(1)
        self.lengthOfMessage = int("".join(str(x) for x in self.lengthOfMessage), 2)
        self.message = []
        for i in range(self.lengthOfMessage*8):
            if self.byte_array[i+10]%2 == 0:
                self.message.append(0)
            else:
                self.message.append(1)
        self.message = [self.message[i:i+8] for i in range(0, len(self.message), 8)]
        for i in range(len(self.message)):
            self.message[i] = chr(int("".join(str(x) for x in self.message[i]), 2))
        self.message = "".join(self.message)
        self.decryptedString.set(self.message)

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File", '.bmp')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width=1000, height=1000-self.selectIMGButton.winfo_height())
        self.imgContainer = self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.pack()

        self.decryptButton['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()

