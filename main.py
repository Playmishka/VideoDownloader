from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pytube

window = Tk()

folder_path = StringVar()
fileLocation = StringVar()


def download():
    if inputURLForVideo.get() == '':
        messagebox.showerror('Ошибка', 'Укажите ссылку на видео')
    else:
        pytube.YouTube(inputURLForVideo.get()).streams.first().download(f'{fileLocation}')


def getURL():
    global fileLocation
    global folder_path
    fileLocation = filedialog.askdirectory()
    folder_path.set(fileLocation)


window.resizable(width=False, height=False)
window.title("VideoDownloader")
window.geometry('500x200')
window.iconbitmap('')

textWriteURL = Label(text='Введите ссылку на видео.', font='OutlineInverkrug 15', justify=CENTER)
inputURLForVideo = Entry(font='OutlineInverkrug 16')
downloadButton = Button(text='Скачать', font='OutlineInverkrug 16', command=download)
getDownloadLocationButton = Button(text='Указать место загрузки', font='OutlineInverkrug 16', command=getURL)

textWriteURL.place(relx=.25, rely=.025)
inputURLForVideo.place(relx=.16, rely=.2, width=350)
downloadButton.place(relx=.4, rely=.4)
getDownloadLocationButton.place(relx=.25, rely=.65)

window.mainloop()
