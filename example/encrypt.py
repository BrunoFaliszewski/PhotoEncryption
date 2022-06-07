from tkinter import *
from tkinter import filedialog
from photoEncryption.encrypt import *
from PIL import Image, ImageTk
import numpy as np
import AES

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title('Photo Encryption')
        self.state('zoomed')

        self.menu = Frame(self)
        self.menu.place(relx=0.5, anchor=N)

        self.selectIMGButton = Button(self.menu, text="Select Image")
        self.selectIMGButton['command'] = self.selectIMG
        self.selectIMGButton.grid(row=1, column=1, columnspan=2)

        self.inputLabel = Label(self.menu, text="Write message")
        self.inputLabel.grid(row=2, column=1)

        self.input = Text(self.menu, width=30, height=3)
        self.input['state'] = 'disable'
        self.input.grid(row=3, column=1)

        self.passwordLabel = Label(self.menu, text="Password")
        self.passwordLabel.grid(row=2, column=2)

        self.passwordInput = Text(self.menu, width=30, height=3)
        self.passwordInput['state'] = 'disable'
        self.passwordInput.grid(row=3, column=2)

        self.encryptButton = Button(self.menu, text="Encrypt")
        self.encryptButton['command'] = self.encrypt
        self.encryptButton['state'] = 'disable'
        self.encryptButton.grid(row=4, column=1, columnspan=2)

    def encrypt(self):
        self.messageString = self.input.get('1.0', 'end')
        self.passwordString = self.passwordInput.get('1.0', 'end')
        self.messageString = AES.encrypt(self.messageString.encode(), self.passwordString).decode()
        
        self.encryptedImage = encrypt(self.image, self.messageString)

        self.savePath = filedialog.asksaveasfile(mode='wb' ,filetypes=[("Bitmap", '*.bmp')], defaultextension=[("Bitmap", '*.bmp')])
        if not self.savePath:
            return
        self.encryptedImage.save(self.savePath)

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("Image File", '.png')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.image = self.image.convert("RGB")
        
        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight()-self.selectIMGButton.winfo_height()-self.inputLabel.winfo_height()-self.input.winfo_height())
        self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.place(y=self.selectIMGButton.winfo_height()+self.inputLabel.winfo_height()+self.input.winfo_height()+self.encryptButton.winfo_height())

        self.encryptButton['state'] = 'normal'
        self.input['state'] = 'normal'
        self.passwordInput['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()
