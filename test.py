from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image


root = Tk()
root.geometry("750x500")
root.title("Conway's Game of Life")

wel_lbl = Label(root, text="Welcome to Conway's Game of Life")
wel_lbl.config(font=("Helvetica", 30))

wel_lbl.pack()



ran_or_dr_frame = LabelFrame(root, text="Random Positioning or Draw Position", labelanchor=N)
ran_or_dr_frame.pack()

dec_var = IntVar()
dec_var.set(1)


ran_radio_btn = ttk.Radiobutton(ran_or_dr_frame, text="Random Positioning",variable= dec_var, value=1)
ran_radio_btn.pack(side="left", padx=100, pady=10)


dr_radio_btn = ttk.Radiobutton(ran_or_dr_frame, text="Draw Position", variable= dec_var, value=2)
dr_radio_btn.pack(side="right", padx=100, pady=10)


size_lbl = Label(root, text="Size: ")
size_lbl.pack()


size_spinbox = ttk.Spinbox(root, from_=12, to= 20)
size_spinbox.pack()

row_lbl = Label(root, text="Rows: ")
row_lbl.pack()


row_spinbox = ttk.Spinbox(root, from_=12, to= 20)
row_spinbox.pack()


col_lbl = Label(root, text="Columns: ")
col_lbl.pack()


col_spinbox = ttk.Spinbox(root, from_=12, to= 20)
col_spinbox.pack()


color_theme_lbl = Label(root, text="Color Theme: ")
color_theme_lbl.pack()

col_th_cbbox = ttk.Combobox(root, state="readonly")
col_th_cbbox.pack()


speed_lbl = Label(root, text="Speed: ")
speed_lbl.pack()

speed_spinbox = ttk.Spinbox(root, from_=5, to= 25)
speed_spinbox.pack()


sub_btn = ttk.Button(root, text="Submit")
sub_btn.pack()


root.mainloop()