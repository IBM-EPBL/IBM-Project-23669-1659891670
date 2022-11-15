# importing
import tkinter
from distutils import command
from tkinter import Tk, Menu, Label, Toplevel, Canvas, BOTH, messagebox
from PIL import ImageTk, Image

# calling Tk() method
root = Tk()

# title() method is used to change the title
root.title("My PROJECT")
root.iconbitmap('images/pill1.ico')

# set center screen window with following coordination
MyLeftPos = int(root.winfo_screenwidth() - 600) / 2
myTopPos = int(root.winfo_screenheight() - 450) / 2
root.geometry("%dx%d+%d+%d" % (500, 400, MyLeftPos, myTopPos))

# Disable the resizable Property
root.resizable(False, False)

def open_reg_window():
    # messagebox.showinfo('ChandanSir', 'FUNCTION CALLED')
    import register
    r1 = Toplevel()
    register.registration_window(r1)

def open_log_window():
    # messagebox.showinfo('ChandanSir', 'FUNCTION CALLED')
    import login
    r1 = Toplevel()
    login.Login()


# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)




admin_menu = Menu(menubar, tearoff=0)

# add menu items to the File menu
admin_menu.add_command(label='LOGIN', command=open_log_window)
admin_menu.add_command(label='EXIT', command=root.destroy)
admin_menu.add_separator()

menubar.add_cascade(label="ADMIN", menu=admin_menu)
menubar.add_cascade(label="REGISTER", command=open_reg_window)
menubar.add_cascade(label="EXIT", command=root.destroy)



my_img = ImageTk.PhotoImage(Image.open("images/icon.jpg"))
# Create a canvas
canvas=Canvas(root, width=400, height=450)
canvas.pack(expand=True, fill=BOTH)
# Add the image in the canvas
canvas.create_image(0, 0, image=my_img, anchor="nw")

# Add a text in canvas
canvas.create_text(260, 180, text="WELCOME TO \nPHARMACY MANAGEMENT SYSTEM", font= ('Courier 20 bold'), justify='center')

# mainloop() is used to load the GUI Window
root.mainloop()