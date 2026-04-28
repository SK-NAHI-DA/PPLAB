from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("300x300")

# Labels
Label(root, text="Name").pack()
Entry(root).pack()

Label(root, text="Gender").pack()

# Radio Buttons
gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

Label(root, text="Courses").pack()

# Check Buttons
Checkbutton(root, text="Python").pack()
Checkbutton(root, text="Java").pack()
Checkbutton(root, text="C++").pack()

Button(root, text="Submit").pack()

root.mainloop()
