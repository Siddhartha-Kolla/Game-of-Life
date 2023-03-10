from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

def configure_window():


    root = Tk()
    root.geometry("750x500")
    root.title("Conway's Game of Life")

    photo = PhotoImage(file = "logo.png")
    root.iconphoto(False, photo)

    wel_lbl = Label(root, text="Welcome to Conway's Game of Life")
    wel_lbl.config(font=("Helvetica", 30))

    wel_lbl.pack()



    ran_or_dr_frame = LabelFrame(root, text="Random Positioning or Draw Position", labelanchor=N)
    ran_or_dr_frame.pack()

    dec_var = IntVar()
    dec_var.set(2)


    ran_radio_btn = ttk.Radiobutton(ran_or_dr_frame, text="Random Positioning",variable= dec_var, value=1)
    ran_radio_btn.pack(side="left", padx=100, pady=10)


    dr_radio_btn = ttk.Radiobutton(ran_or_dr_frame, text="Draw Position", variable= dec_var, value=2)
    dr_radio_btn.pack(side="right", padx=100, pady=10)


    size_lbl = Label(root, text="Size: ")
    size_lbl.pack()


    size_spinbox = ttk.Spinbox(root, from_=12, to= 20)
    size_spinbox.set(15)
    size_spinbox.pack()

    row_lbl = Label(root, text="Rows: ")
    row_lbl.pack()


    def change_size(event):
        screen_width = int(root.winfo_screenwidth())
        screen_height = int(root.winfo_screenheight())
        width = int(size_spinbox.get())
        row_spinbox.config(from_=10, to=screen_height//width-10)
        col_spinbox.config(from_=10, to=(screen_width-200)//width-5)

    row_spinbox = ttk.Spinbox(root, from_=10, to= 50)
    row_spinbox.set(25)
    row_spinbox.bind("<Button-1>", change_size)

    row_spinbox.pack()


    col_lbl = Label(root, text="Columns: ")
    col_lbl.pack()


    col_spinbox = ttk.Spinbox(root, from_=10, to= 50)
    col_spinbox.set(25)
    col_spinbox.pack()
    col_spinbox.bind("<Button-1>", change_size)


    color_theme_lbl = Label(root, text="Color Theme: ")
    color_theme_lbl.pack()

    col_th_cbbox = ttk.Combobox(root, state="readonly", values=["Grey - Yellow","Black - White","Black- Red","Green - Purple"])
    col_th_cbbox.set("Grey - Yellow")
    col_th_cbbox.pack()


    speed_lbl = Label(root, text="Speed: ")
    speed_lbl.pack()

    speed_spinbox = ttk.Spinbox(root, from_=5, to= 25)
    speed_spinbox.set(20)
    speed_spinbox.pack()

    def submit():
        r_or_d = dec_var.get()
        size = int(size_spinbox.get())
        row = int(row_spinbox.get())
        col = int(col_spinbox.get())
        color_theme = col_th_cbbox.get()
        speed = int(speed_spinbox.get())	
        if r_or_d == 1:
            r_or_d = "Random"
        elif r_or_d == 2:
            r_or_d = "Draw"
        if size < 12 or size > 20:
            err_lbl.config(text="Size must be between 12 and 20")
            return None
        screen_width = int(root.winfo_screenwidth())
        screen_height = int(root.winfo_screenheight())
        width = int(size_spinbox.get())
        if row < 10 or row > screen_height//width-10:
            err_lbl.config(text="Row must be between 10 and " + str(screen_height//width-10))
            return None
        if col < 10 or col > (screen_width-200)//width:
            err_lbl.config(text="Column must be between 10 and " + str((screen_width-200)//width))
            return None
        if speed < 5 or speed > 25:
            err_lbl.config(text="Speed must be between 5 and 25")
            return None
        global list_of_configurations
        list_of_configurations = {"r_or_d":r_or_d,"size":size,"row":row,"col":col,"color_theme":color_theme,"speed":speed}

        root.destroy()
        root.quit()
        

    sub_btn = ttk.Button(root, text="Submit", command=submit)
    sub_btn.pack(padx=20, pady=10)

    err_lbl = Label(root, text="")
    err_lbl.pack(padx=20, pady=10)



    root.mainloop()

    return list_of_configurations