from operator import le
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Szyfrowanie')
        self.geometry('500x500')

        self.selectIMGButton = Button(self, text="Select Image")
        self.selectIMGButton['command'] = self.selectIMG
        self.selectIMGButton.pack()

        self.inputLabel = Label(self, text="Write message")
        self.inputLabel.pack()

        self.message = StringVar()
        self.input = Entry(self, textvariable=self.message)
        self.input['state'] = 'disable'
        self.input.pack()

        self.encryptButton = Button(self, text="Encrypt")
        self.encryptButton['command'] = self.encrypt
        self.encryptButton['state'] = 'disable'
        self.encryptButton.pack()

    def encrypt(self):
        self.byte_array = np.asarray(self.image)
        self.byte_array = self.byte_array.flatten()
        self.messageString = self.message.get()
        self.lengthOfMessage = list(bin(len(self.messageString))[2::])
        for i in range(10-len(self.lengthOfMessage)):
            self.lengthOfMessage.insert(0, '0')
        print(self.lengthOfMessage)
        for i in range(10):
            if self.byte_array[i]%2 == 0:
                self.byte_array[i] += int(self.lengthOfMessage)
            else:
                self.byte_array[i] += int(self.lengthOfMessage) - 1

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width=1000, height=1000-self.selectIMGButton.winfo_height()-self.inputLabel.winfo_height()-self.input.winfo_height())
        self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.pack()

        self.encryptButton['state'] = 'normal'
        self.input['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()

