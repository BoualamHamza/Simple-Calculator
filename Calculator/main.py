from logging import root
from  tkinter import *

root = Tk()
root.title("CALCULATOR")

#_____numbers holders_______________
input = Entry(root, bg="white")
input.grid(row=0, column=0, columnspan=5)

#_____display on screen_____________
def display(number):
    current_number = input.get()
    clear()
    input.insert(0, str(current_number) + str(number)) 

#_____operations____________________
def add():
    global first_number, operation
    first_number = input.get()
    operation = "addition"
    clear()

def substract():
    global first_number, operation
    first_number = input.get()
    operation = "substraction"
    clear()

def multiply():
    global first_number, operation
    first_number = input.get()
    operation = "multiplication"
    clear()

def devide():
    global first_number, operation
    first_number = input.get()
    operation = "devision"
    clear()

#_____clean_screen________________
def clear():
    input.delete(0, END)

#____calculate the result________
def equal_Button():
    second_num = input.get()
    clear()
    if operation == "addition":
        input.insert(0, int(first_number) + int(second_num))
    elif operation == "subtraction":
        input.insert(0, int(first_number) - int(second_num))
    elif operation == "multiplication":
        input.insert(0, int(first_number) * int(second_num))
    else :
        if operation == "devision" and int(second_num) != 0 :
            input.insert(0, int(first_number) / int(second_num))
        else:
            input.insert(0, "Error")


#________Numbers Buttons_________
button1 = Button(root, text= "1", command=lambda: display(1), padx=40, pady=40).grid(row=1, column=1)
button2 = Button(root, text= "2", command=lambda: display(2), padx=40, pady=40).grid(row=1, column=2)
button3 = Button(root, text= "3", command=lambda: display(3), padx=40, pady=40).grid(row=1, column=3)
button4 = Button(root, text= "4", command=lambda: display(4), padx=40, pady=40).grid(row=2, column=1)
button5 = Button(root, text= "5", command=lambda: display(5), padx=40, pady=40).grid(row=2, column=2)
button6 = Button(root, text= "6", command=lambda: display(6), padx=40, pady=40).grid(row=2, column=3)
button7 = Button(root, text= "7", command=lambda: display(7), padx=40, pady=40).grid(row=3, column=1)
button8 = Button(root, text= "8", command=lambda: display(8), padx=40, pady=40).grid(row=3, column=2)
button9 = Button(root, text= "9", command=lambda: display(9), padx=40, pady=40).grid(row=3, column=3)
button0 = Button(root, text= "0", command=lambda: display(0), padx=40, pady=40).grid(row=4, column=1)

#____Operation buttons_________
Add_Button = Button(root, text= "+", command=add, padx=40, pady=40).grid(row=1, column=4)
Substract_Button = Button(root, text= "-", command=substract, padx=40, pady=40).grid(row=2, column=4)
Multply_Button = Button(root, text= "*", command=multiply, padx=40, pady=40).grid(row=3, column=4)
Devide_button = Button(root, text= "/", command=devide, padx=40, pady=40).grid(row=4, column=4)
Equal_Button = Button(root, text= "=", command=equal_Button, padx=40, pady=40).grid(row=4, column=2)
Clear_Button = Button(root, text= "CE", command= clear, padx=40, pady=40).grid(row=4, column=3)








root.mainloop()



