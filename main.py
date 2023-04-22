import sys
from tkinter import *
import customtkinter
import webbrowser
from PIL import ImageTk, Image
import os

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = customtkinter.CTk()
root.title('Calculator')
root.iconbitmap(resource_path('logo.ico'))
root.geometry('445x585')





# input/output box

input_box = customtkinter.CTkEntry(master=root, width=400, height=40, font=("Helvetica", 20))
input_box.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# functions of the claculator

def button_input(number):
    current = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, str(current) + str(number))


def button_clear():
    input_box.delete(0, END)


def button_add():
    first_number = input_box.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_subtract():
    first_number = input_box.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_multiply():
    first_number = input_box.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_divide():
    first_number = input_box.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_power2():
    first_number = input_box.get()
    global f_num
    global math
    math = 'power2'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_square_root():
    first_number = input_box.get()
    global f_num
    global math
    math = 'square_root'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_lbs_to_kg():
    first_number = input_box.get()
    global f_num
    global math
    math = 'LBS_to_KG'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_kg_to_lbs():
    first_number = input_box.get()
    global f_num
    global math
    math = 'KG_to_LBS'
    f_num = float(first_number)
    input_box.delete(0, END)


def button_equal():
    second_number = input_box.get()
    input_box.delete(0, END)

    if math == 'addition':
        input_box.insert(0, float(f_num) + float(second_number))
    if math == 'subtraction':
        input_box.insert(0, float(f_num) - float(second_number))
    if math == 'multiplication':
        input_box.insert(0, float(f_num) * float(second_number))
    if math == 'division':
        input_box.insert(0, float(f_num) / float(second_number))
    if math == 'power2':
        input_box.insert(0, float(f_num) ** float(second_number))
    if math == 'square_root':
        input_box.insert(0, float(f_num) ** 0.5)
    if math == 'LBS_to_KG':
        input_box.insert(0, float(f_num) * 0.45)
    if math == 'KG_to_LBS':
        input_box.insert(0, float(f_num) / 0.45)


# buttons of claculator


button_0 = customtkinter.CTkButton(root, text='0', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(0))
button_1 = customtkinter.CTkButton(root, text='1', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(1))
button_2 = customtkinter.CTkButton(root, text='2', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(2))
button_3 = customtkinter.CTkButton(root, text='3', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(3))
button_4 = customtkinter.CTkButton(root, text='4', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(4))
button_5 = customtkinter.CTkButton(root, text='5', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(5))
button_6 = customtkinter.CTkButton(root, text='6', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(6))
button_7 = customtkinter.CTkButton(root, text='7', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(7))
button_8 = customtkinter.CTkButton(root, text='8', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(8))
button_9 = customtkinter.CTkButton(root, text='9', font=("Helvetica", 30), width=100, height=70, anchor='center',
                                   command=lambda: button_input(9))
button_point = customtkinter.CTkButton(root, text='.', font=("Helvetica", 40), fg_color='#113b69', width=100, height=70,
                                       anchor='center', command=lambda: button_input('.'))
button_addition = customtkinter.CTkButton(root, text='+', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                          height=70, anchor='center', command=button_add)
button_equals = customtkinter.CTkButton(root, text='=', font=("Helvetica", 30), text_color='black', fg_color='#47b1e8',
                                        width=210, height=70, anchor='center', command=button_equal)
button_clear = customtkinter.CTkButton(root, text='C', font=("Helvetica", 30), fg_color='#113b69', width=100, height=70,
                                       anchor='center', command=button_clear)

button_subtract = customtkinter.CTkButton(root, text='-', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                          height=70, anchor='center', command=button_subtract)
button_multiply = customtkinter.CTkButton(root, text='×', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                          height=70, anchor='center', command=button_multiply)
button_divide = customtkinter.CTkButton(root, text='÷', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                        height=70, anchor='center', command=button_divide)
button_power2 = customtkinter.CTkButton(root, text='x²', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                        height=70, anchor='center', command=button_power2)
button_square_root = customtkinter.CTkButton(root, text='√', font=("Helvetica", 30), fg_color='#113b69', width=100,
                                             height=70, anchor='center', command=button_square_root)
button_lbs_to_kg = customtkinter.CTkButton(root, text='LBS → KG', font=("Helvetica", 30), fg_color='#113b69', width=212,
                                           height=70, anchor='center', command=button_lbs_to_kg)
button_kg_to_lbs = customtkinter.CTkButton(root, text='KG → LBS', font=("Helvetica", 30), fg_color='#113b69', width=212,
                                           height=70, anchor='center', command=button_kg_to_lbs)
# putting buttons on the screen

# bottom row
button_1.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
button_2.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
button_3.grid(row=3, column=2, columnspan=1, padx=5, pady=5)
# middle row
button_4.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
button_5.grid(row=2, column=1, columnspan=1, padx=5, pady=5)
button_6.grid(row=2, column=2, columnspan=1, padx=5, pady=5)
# top row
button_7.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
button_8.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
button_9.grid(row=1, column=2, columnspan=1, padx=5, pady=5)
# other buttons
button_clear.grid(row=4, column=2, columnspan=1, padx=5, pady=5)
button_point.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
button_0.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

button_addition.grid(row=1, column=3, columnspan=1, padx=5, pady=5)
button_equals.grid(row=6, column=2, columnspan=2, padx=5, pady=5)
button_subtract.grid(row=2, column=3, columnspan=1, padx=5, pady=5)

button_multiply.grid(row=3, column=3, columnspan=1, padx=5, pady=5)
button_divide.grid(row=4, column=3, columnspan=1, padx=5, pady=5)
button_power2.grid(row=5, column=2, columnspan=1, padx=5, pady=5)
button_square_root.grid(row=5, column=3, columnspan=1, padx=5, pady=5)
button_lbs_to_kg.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
button_kg_to_lbs.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# hyperlink to my gitHub

gitlink = customtkinter.CTkLabel(master=root, text='     My Github', text_color='#83c6d6', cursor='hand2',
                                 font=('Times', 16, 'bold', 'italic'))
gitlink.grid(row=7, column=0, columnspan=2)
gitlink.bind('<Button-1>', lambda x: webbrowser.open_new('https://github.com/JonasAurelius'))
giticon = customtkinter.CTkImage(size=(40, 40), light_image=Image.open(resource_path('images\\github_logo.jpg')))
gitlabel = customtkinter.CTkLabel(master=root, image=giticon, width=60, height=40, text='')
gitlabel.grid(row=7, column=0, columnspan=1)
# hyperlink to my YouTube

ytlink = customtkinter.CTkLabel(master=root, text='          My Youtube', text_color='#83c6d6', cursor='hand2',
                                font=('Times', 16, 'bold', 'italic'))
ytlink.grid(row=7, column=2, columnspan=2)
ytlink.bind('<Button-1>', lambda x: webbrowser.open_new('https://www.youtube.com/channel/UC0Ftjb-aEQkONtw4sjJhBwg'))
yticon = customtkinter.CTkImage(size=(45, 30), light_image=Image.open(resource_path('images\\youtube_logo2.jpg')))
ytlabel = customtkinter.CTkLabel(master=root, image=yticon, width=60, height=40, text='')
ytlabel.grid(row=7, column=2, columnspan=1)
# end
root.mainloop()
