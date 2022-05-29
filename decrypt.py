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

    def decrypt(self):
        self.byte_array = np.asarray(self.image)
        self.photoShape = self.byte_array.shape
        self.byte_array = self.byte_array.flatten()
        self.lengthOfMessage = []
        # for i in range(10):
        #     if self.byte_array[i]%2 == 0:
        #         self.lengthOfMessage.append(0)
        #     else:
        #         self.lengthOfMessage.append(1)
        print(self.byte_array[0:10])

    def selectIMG(self):
        self.path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg'), ("Image File", '.png')])
        self.image = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(self, width=1000, height=1000-self.selectIMGButton.winfo_height())
        self.imgContainer = self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.pack()

        self.decryptButton['state'] = 'normal'

if __name__ == "__main__":
    app = App()
    app.mainloop()
