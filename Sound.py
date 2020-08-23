from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as messagebox
import numpy as numpyVar
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import contextlib
import wave
from scipy.io import wavfile as wav
from scipy.fftpack import fft,fftfreq
import os
import sys

fname=""

root=Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Signal Processing")

def uploadFile():
    global fname
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Dell\Downloads", filetype=(("Audio Signal", "*.wav"), ("All Files", "*.*")), title="Upload")
    fname=root.filename



#Plot Audio Signal
def signalFunction(Frame1):
    if (root.filename != '' and root.filename != 0):
        rate, sound = wav.read(root.filename)       ######wav.read(r'C:\Users\Dell\Downloads\maybe-next-time.wav')

        shape = sound.shape[0]
        nameOfSound = root.filename                 ######r'C:\Users\Dell\Downloads\maybe-next-time.wav'
        with contextlib.closing(wave.open(nameOfSound, 'r')) as getMyFrame:
            itsMyFrame = getMyFrame.getnframes()
            rate = getMyFrame.getframerate()
            duration = itsMyFrame / float(rate)
            print(round(duration, 2))



        Frame1.destroy()
        Frame1 = Frame(root, width=50, height=50)
        Frame1.pack()
        myCanvas1 = Canvas(Frame1, width=40, height=40)
        myCanvas1.pack()

        record = Button(myCanvas1, text="Plot Signal", fg="red", command=lambda: signalFunction(Frame1))
        record.pack(side=LEFT, padx=40, pady=5)

        time = Label(myCanvas1, text="Duration(seconds): ", fg='black')
        time.pack()

        timeDuration = Label(myCanvas1, text="0:00", fg='black')
        timeDuration.pack()

        timeDuration.configure(text=round(duration, 2))

        f = Figure(figsize=(6,3))
        a = f.add_subplot(122)
        a.plot(numpyVar.arange(shape) / rate, sound)

        canvas1 = FigureCanvasTkAgg(f, Frame1)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=TOP,expand=True)
        toolbar = NavigationToolbar2Tk(canvas1, Frame1)
        toolbar.update()
        canvas1._tkcanvas.pack()

        a.set_xlabel('Time (s)')
        a.set_ylabel('Amplitude')
        a.set_title('Audio Signal')
       # plt.show()



#Plot Fast Fourier Transform
def plotFastFT(Frame2):
    if (root.filename != '' and root.filename != 0):

        soundRate,sound = wav.read(root.filename)
        fourierTransform=numpyVar.arange(len(sound))/float(soundRate)
        soundShape=sound.shape[0]

        if len(sound.shape) > 1:
           sound = sound[:, 0]
        else:
            sound = sound

        sound.shape

        fftPlot=fft(sound)

        calcFFT=(fftPlot)
        frequency=fftfreq(soundShape,1.0/(float)(soundRate))


        Frame2.destroy()
        Frame2 = Frame(root, width=100, height=100,relief='ridge')
        Frame2.pack()

        myCanvas2 = Canvas(Frame2, width=100, height=100)
        myCanvas2.pack()

        myFFT = Button(myCanvas2, text="Plot FFT", fg="red", command=lambda: plotFastFT(Frame2))
        myFFT.pack(side=LEFT, padx=40, pady=5)

        f = Figure(figsize=(6,3))
        a = f.add_subplot(122)

        a.plot(frequency, calcFFT)
        canvas1 = FigureCanvasTkAgg(f, master=Frame2)
        canvas1.draw()
        canvas1.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas1, Frame2)
        toolbar.update()
        canvas1._tkcanvas.pack()

        a.set_xlabel('Frequency')
        a.set_ylabel('Imaginary')
        a.set_title('Fast Fourier Transform')

Frame1 = Frame(root, width = 50, height = 50)
Frame1.pack()

Frame2=Frame(root, width = 50, height = 50)
Frame2.pack()

myCanvas1 = Canvas(Frame1, width=40, height=40)
myCanvas1.pack()
myCanvas2 = Canvas(Frame2, width=40, height=40)
myCanvas2.pack()
myCanvas3 = Canvas(root, width=40, height=40)
myCanvas3.pack()


upload = Button(myCanvas3, text="Upload", fg="black", command=uploadFile)

record = Button(myCanvas1, text="Plot Signal", fg="red", command=lambda:signalFunction(Frame1))

time = Label(myCanvas1, text="Duration(seconds): ", fg='black')
time.pack()

timeDuration = Label(myCanvas1, text="0:00", fg='black')
timeDuration.pack()

myFFT = Button(myCanvas2, text="Plot FFT", fg="red", command=lambda:plotFastFT(Frame2))


upload.pack(side=LEFT, padx=20, pady= 5)
record.pack(side=RIGHT, padx=20, pady= 5)
myFFT.pack(side=LEFT, padx=20, pady=5)

root.mainloop()