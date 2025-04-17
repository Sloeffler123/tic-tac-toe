from tkinter import *
from setup import *
window = Tk()
window.title('Tic-Tac-Toe')
window.config(padx=100,pady=100)
canvas = Canvas(width=400,height=400)

canvas.create_line(0, 100, 300, 100, width=2)
canvas.create_line(0, 200, 300, 200, width=2)

# Vertical lines
canvas.create_line(100, 0, 100, 300, width=2)
canvas.create_line(200, 0, 200, 300, width=2)
canvas.place(x=0,y=0)


button_7 = Button()
button_7.grid(column=0,row=0,padx=30,pady=30)
button_8 = Button()
button_8.grid(column=1,row=0,padx=40,pady=30)
button_9 = Button()
button_9.grid(column=2,row=0,padx=20,pady=30)

button_4 = Button()
button_4.grid(column=0,row=1,padx=35,pady=40)
button_5 = Button()
button_5.grid(column=1,row=1,padx=40,pady=30)
button_6 = Button()
button_6.grid(column=2,row=1,padx=20,pady=30)

button_1 = Button()
button_1.grid(column=0,row=2,padx=30,pady=30)
button_2 = Button()
button_2.grid(column=1,row=2,padx=40,pady=30)
button_3 = Button()
button_3.grid(column=2,row=2,padx=20,pady=30)

window.mainloop()