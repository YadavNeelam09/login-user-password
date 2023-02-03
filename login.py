from tkinter import *

window = Tk()  # create a window widget
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title("login system")
window.geometry("350x300")
window.configure(bg= "cyan")

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ============= Page 1 =========
pag1_label = Label(page1, text='Username', font=('Arial', 15, 'bold'))
pag1_label.place(x=50, y=100)

pag1_entry = Entry(page1)
pag1_entry.place(x=170, y=106)

pag1_label2 = Label(page1, text='Password', font=('Arial', 15, 'bold'))
pag1_label2.place(x=50, y=150)

pag1_entry2 = Entry(page1)
pag1_entry2.place(x=170, y=155)

pg1_button = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))
pg1_button.place(x=170, y=200)

# ======== Page 2 ===========
page2.config(background='yellow')
pag2_label = Label(page2, text='WELCOME TO PAGE 2', font=('Arial', 30, 'bold'))
pag2_label.place(x=50, y=100)

pg2_button = Button(page2, text='NEXT', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg2_button.place(x=190, y=400)

# ======== Page 3 ===========
page3.config(background='gray')
pag3_label = Label(page3, text='WELCOME TO PAGE 3', font=('Arial', 30, 'bold'))
pag3_label.place(x=50, y=100)

pg3_button = Button(page3, text='NEXT', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
pg3_button.place(x=190, y=400)



window.mainloop()