from tkinter import *

def accept():
    print("Temp is " + str(scale.get()) + " degrees C")

window = Tk()
scale = Scale(window,
              from_=70,
              to=0,
              length=700,
              font=('Times New Roman', 15),
              tickinterval=10,
              resolution=2,
              troughcolor='blue',
              fg='red',
              bg='green',
              orient=VERTICAL,

              )
scale.set(((scale['from']-scale['to'])/2) + scale['to'])
button = Button(window,
                text='Accept',
                command=accept)

scale.pack()
button.pack()
window.mainloop()