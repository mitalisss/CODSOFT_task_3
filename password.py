# password generator
from tkinter import *
import random
import string
from PIL import Image, ImageTk

#window
root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("710x425")

root.resizable(0,0)

root.configure(bg='#081c15')

# #background image
# bg_image = Image.open("b1.jpg") 
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = Label(root, image=bg_photo)
# bg_label.place(relwidth=1, relheight=1)

#enter password lenght
ent_len = Label(root, text='Enter Length of Password', font=('cambria', 18, 'bold', 'italic'), bg='#081c15', fg="white")
ent_len.grid(row=1, column=0, sticky=W, padx=10, pady=10) 
txt_len = Entry(root, font=('cambria', 22, 'bold'), bd=8, width=20, justify='right', background='azure')
txt_len.grid(row=1, column=1, columnspan=1, padx=5, pady=10) 

len_pass = 0  # Set initial value

#generate password button
def btn_generate():
    try:
        len_pass = int(txt_len.get())
        characters = string.ascii_letters + string.digits 
        password = ''.join(random.choice(characters) for _ in range(len_pass))
        txt_gen.delete(0, END)
        txt_gen.insert(END, str(password))
    except ValueError:
        txt_gen.delete(0, END)
        txt_gen.insert(END, "Invalid input. Please enter a valid integer for length.")

n_gen = Button(root, font=('cambria', 20), text='Generate Password', width=15, height=2, bg="#84a98c", fg='azure',command=btn_generate)
n_gen.grid(row=3, column=1, columnspan=1, padx=5, pady=5)  

#generated password
gen_pas = Label(root, text='Your Password Is', font=('cambria', 19, 'bold', 'italic'), bg='#081c15', fg="white")
gen_pas.grid(row=5, column=0, sticky=W, padx=5, pady=6)  
txt_gen = Entry(root, font=('cambria', 22, 'bold'), bd=8, width=20, justify='right', background='azure')
txt_gen.grid(row=5, column=1, columnspan=1, padx=5, pady=10)  

#clear button
def btn_clear():
    txt_len.delete(0,END)
    txt_gen.delete(0,END)

n_clear = Button(root, font=('cambria', 20), text='Clear', width=15, height=2, bg="#84a98c",fg='azure', command=btn_clear)
n_clear.grid(row=7, column=1, columnspan=1, padx=10, pady=10)  

root.mainloop()
