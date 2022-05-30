from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import AES

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Photo Encryption')
        self.geometry('500x500')

        self.menu = Frame(self)
        self.menu.place(relx=0.5, anchor=N)

        self.selectIMGButton = Button(self.menu, text="Select Image")
        self.selectIMGButton['command'] = self.selectIMG
        self.selectIMGButton.grid(row=1, column=1, columnspan=2)

        self.inputLabel = Label(self.menu, text="Write message")
        self.inputLabel.grid(row=2, column=1)

        self.message = StringVar()
        self.input = Entry(self.menu, textvariable=self.message)
        self.input['state'] = 'disable'
        self.input.grid(row=3, column=1)

        self.passwordLabel = Label(self.menu, text="Password")
        self.passwordLabel.grid(row=2, column=2)

        self.password = StringVar()
        self.passwordInput = Entry(self.menu, textvariable=self.password)
        self.passwordInput['state'] = 'disable'
        self.passwordInput.grid(row=3, column=2)

        self.encryptButton = Button(self.menu, text="Encrypt")
        self.encryptButton['command'] = self.encrypt
        self.encryptButton['state'] = 'disable'
        self.encryptButton.grid(row=4, column=1, columnspan=2)

    def encrypt(self):
        self.byte_array = np.asarray(self.image)
        self.photoShape = self.byte_array.shape
        self.byte_array = self.byte_array.flatten()
        self.messageString = self.message.get()
        self.passwordString = self.password.get()
        self.messageString = AES.encrypt(self.messageString.encode(), self.passwordString).decode()
        self.binaryMessage = list(map(bin, bytearray(self.messageString, 'utf-8')))
        for i in range(len(self.binaryMessage)):
            self.binaryMessage[i] = self.binaryMessage[i][2::]
            self.binaryMessage[i] = [int(char) for char in self.binaryMessage[i]]
            for j in range(8-len(self.binaryMessage[i])):
                self.binaryMessage[i].insert(0, 0)
        self.binaryMessage = np.asarray(self.binaryMessage).flatten()
        self.lengthOfMessage = list(map(int, list(bin(len(self.messageString))[2::])))
        for i in range(10-len(self.lengthOfMessage)):
            self.lengthOfMessage.insert(0, 0)
        for i in range(10):
            if self.byte_array[i]%2 == 0:
                self.byte_array[i] += self.lengthOfMessage[i]
            else:
                self.byte_array[i] += self.lengthOfMessage[i] - 1
        for i in range(len(self.messageString)*8):
            if self.byte_array[i+10]%2 == 0:
                self.byte_array[i+10] += self.binaryMessage[i]
            else:
                self.byte_array[i+10] += self.binaryMessage[i] - 1
        self.byte_array = self.byte_array.reshape(self.photoShape)
        self.byte_array = np.ascontiguousarray(self.byte_array)
        self.encryptedImage = Image.fromarray(self.byte_array)
        self.savePath = filedialog.asksaveasfile(mode='wb' ,filetypes=[("Bitmap", '*.bmp')], defaultextension=[("Bitmap", '*.bmp')])
        if not self.savePath:
            return
        self.encryptedImage.save(self.savePath)

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("Image File", '.png')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width=1000, height=1000-self.selectIMGButton.winfo_height()-self.inputLabel.winfo_height()-self.input.winfo_height()-self.passwordInput.winfo_height())
        self.imgContainer = self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.place(y=self.selectIMGButton.winfo_height()+self.inputLabel.winfo_height()+self.input.winfo_height()+self.encryptButton.winfo_height())

        self.encryptButton['state'] = 'normal'
        self.input['state'] = 'normal'
        self.passwordInput['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()

