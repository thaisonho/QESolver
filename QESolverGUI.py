from tkinter import *
from math import *
from tkinter import messagebox as ms
import unicodedata as un
from pathlib import Path


# Set path and put path as a variable to access files for the program
# Get the parrent folder of this Python script
# Ex: C:/SomeFold3r/QES_GUI
getParrentFolder = Path(__file__).parent
# Change directory to C:/SomeFold3r/QES_GUI/Files
getFileFolder = getParrentFolder / Path("./Files")

# Define fuction to get the needed file directory
# Ex: getFileDirectory("Somefiles.txt") => 'C:/Somefold3r/QES_GUI/Files/Somefiles.txt
def getFileDirectory(path: str):
    return getFileFolder / Path(path)


# Check if input is number or not
def is_Number(string):
    # Case 1: if the input is ASCII character
    try:
        float(string)
        return True
    except ValueError:
        pass
    # Case 2: if the input is Unicode character
    try:
        un.numeric(string)
        return True
    except (TypeError, ValueError):
        pass
    return False


# Check if input is a valid input type or not
def is_Valid(string1, string2, string3):
    if len(string1) == 0 or len(string2) == 0 or len(string3) == 0:
        return 1
    elif is_Number(string1) == False or is_Number(string2) == False or is_Number(string3) == False:
        return 2


# Giving all the roots and errors might have 
def SolveButtonClick():
    entryOfNumberA = txtBar_InsertA.get()
    entryOfNumberB = txtBar_InsertB.get()
    entryOfNumberC = txtBar_InsertC.get()

    if is_Valid(entryOfNumberA, entryOfNumberB, entryOfNumberC) == 1:
        ms.showwarning("Warning", "All blanks should be filled in")
    elif is_Valid(entryOfNumberA, entryOfNumberB, entryOfNumberC) == 2:
        ms.showerror("ERROR", "You should insert real numbers")
    else:
        num1 = float(entryOfNumberA)
        num2 = float(entryOfNumberB)
        num3 = float(entryOfNumberC)

        if num1 == 0:
            ms.showerror("MATH ERROR", "Number A must be different from 0")
        else:
            delta = num2 * num2 - 4 * num1 * num3
            if delta == 0:
                x = round(-num2/(2 * num1), 4)
                ms.showinfo("Answer", "The Equation have 1 root: " + str(x))
            elif delta > 0:
                x1 = round((-num2 + sqrt(delta)) / (2 * num1), 4)
                x2 = round((-num2 - sqrt(delta)) / (2 * num1), 4)
                ms.showinfo("Answer", "The Equation have 2 roots:\n\nx1 = " + str(x1) + "\nx2 = " + str(x2))
            elif delta < 0:
                firstPart = str(round(-num2 / (2 * num1), 4))
                secondPart = str(round(sqrt(abs(delta)) / (2 * num1), 4)) + 'i'
                x1 = firstPart + ' + ' + secondPart
                x2 = firstPart + ' - ' + secondPart
                ms.showinfo( "Answer", "The Equation have 2 roots:\n\nx1 = " + x1 + "\nx2 = " + x2)


# Clear all the textbox content
def ClearButtonClick():
    txtBar_InsertA.delete(0, END)
    txtBar_InsertB.delete(0, END)
    txtBar_InsertC.delete(0, END)


window = Tk()


# Window configuation
window.geometry("730x518")
window.configure(bg="#52688F")
window.title("Quadratic Equation Solver - By Thai Son")
window.iconbitmap(getFileDirectory("calculator.ico"))


# Add canvas
canvas = Canvas(
    window,
    bg="#52688F",
    height=518,
    width=730,
    bd=0,
    highlightthickness=0,
)
canvas.place(x=0, y=0)

# Add header
image_Header = PhotoImage(file=getFileDirectory("Header.png"))
Header = canvas.create_image(
    364.8,
    40,
    image=image_Header
)

# Add note
image_Note= PhotoImage(file=getFileDirectory("Note.png"))
Note = canvas.create_image(
    365.0,
    178.0,
    image=image_Note
)


# Add insert box (a, b, c)
image_BoxNumberA = PhotoImage(file=getFileDirectory("BoxInsertA.png"))
BoxNumberA = canvas.create_image(
    159.0,
    305.0,
    image=image_BoxNumberA
)

image_BoxNumberB = PhotoImage(file=getFileDirectory("BoxInsertB.png"))
BoxNumberB = canvas.create_image(
    364.0,
    305.0,
    image=image_BoxNumberB
)

image_BoxNumberC = PhotoImage(file=getFileDirectory("BoxInsertC.png"))
BoxNumberC = canvas.create_image(
    570.0,
    305.0,
    image=image_BoxNumberC
)


# add textbox for a, b, c
image_InsertA = PhotoImage(file=getFileDirectory("InsertEntry.png"))
Put_InsertA_Image = canvas.create_image(
    159.0,
    364.5,
    image=image_InsertA
)
txtBar_InsertA = Entry(
    bd=0,
    bg="#E3E7F1",
)
txtBar_InsertA.place(
    x=89.5,
    y=347.0,
    width=139.0,
    height=33.0
)

image_InsertB = PhotoImage(file=getFileDirectory("InsertEntry.png"))
Put_InsertB_Image = canvas.create_image(
    364.5,
    364.5,
    image=image_InsertB
)
txtBar_InsertB = Entry(
    bd=0,
    bg="#E3E7F1"
)
txtBar_InsertB.place(
    x=294.5,
    y=347.0,
    width=140.0,
    height=33.0
)


image_InsertC = PhotoImage(file=getFileDirectory("InsertEntry.png"))
Put_InsertC_Image = canvas.create_image(
    570.0,
    364.5,
    image=image_InsertC
)
txtBar_InsertC = Entry(
    bd=0,
    bg="#E3E7F1",
)
txtBar_InsertC.place(
    x=500.5,
    y=347.0,
    width=139.0,
    height=33.0
)


# Add Button
buttonImg = PhotoImage(file=getFileDirectory("SolveButton.png"))
SolveButton = Button(
    image=buttonImg,
    borderwidth=0,
    command=SolveButtonClick,
)
SolveButton.place(
    x=323.0,
    y=403.0,
    width=84.0,
    height=36.3,
)

Clear_Image = PhotoImage(file=getFileDirectory("ClearButton.png"))
ClearButton = Button(
    image=Clear_Image,
    borderwidth=0,
    command=ClearButtonClick
)
ClearButton.place(
    x=323,
    y=450,
    width=84.0,
    height=36.3
)

# Run Script
window.resizable(False, False)
window.mainloop()