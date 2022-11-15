from tkinter import*
from tkinter import ttk, messagebox
from PIL import ImageTk, Image   # pip3 install pillow


def registration_window(root):
        root.title("Registration Window")  # For Title of the page
        MyLeftPos = int(root.winfo_screenwidth() - 500) / 2
        myTopPos = int(root.winfo_screenheight() - 450) / 2
        root.geometry("%dx%d+%d+%d" % (500, 450, MyLeftPos, myTopPos))
        #root.iconbitmap('ai.ico')
        root.resizable(False, False)
        root['background'] = '#D2E3EF'

        title = Label(root, text="Register Here", font=("times new roman", 20, "bold"), fg="green").place(x=170, y=30)

        # --------First Row
        l_name = Label(root, text="Full Name", font=("times new roman", 15, "bold"),fg="blue").place(x=50, y=100)
        txt_name = Entry(root, font=("times new roman", 15)).place(x=180, y=100, width=250)

        # --------Second Row
        l_email = Label(root, text="Email Id", font=("times new roman", 15, "bold"), fg="blue").place(x=50, y=140)
        txt_email = Entry(root, font=("times new roman", 15,)).place(x=180, y=140, width=250)

        # --------3rd Row

        l_mobile = Label(root, text="Mobile No", font=("times new roman", 15, "bold"), fg="blue").place(x=50, y=180)
        txt_mobile = Entry(root, font=("times new roman", 15)).place(x=180, y=180, width=250)

        # ---------4th Row

        l_password = Label(root, text="Password", font=("times new roman", 15, "bold"), fg="blue").place(x=50, y=220)
        txt_password = Entry(root, show="*", font=("times new roman", 15)).place(x=180, y=220, width=250)

        # -------5th Row
        l_gender = Label(root, text="Gender", font=("times new roman", 15, "bold"), fg="blue").place(x=50, y=260)
        r1_gender = Radiobutton(root, text='Male', value=1, font=("times new roman", 15)).place(x=180, y=260)
        r2_gender = Radiobutton(root, text='Female', value=2, font=("times new roman", 15)).place(x=260, y=260)

        # -------6th Row
        country = StringVar()
        l_country = Label(root, text="Country", font=("times new roman", 15, "bold"), fg="blue").place(x=50, y=300)
        country_list = ['INDIA', 'Philippines', 'Japan', 'Korea', 'China', 'Singapore', 'Hong kong']
        droplist_country = OptionMenu(root, country, *country_list).place(x=180, y=300, width=220)
        country.set(country_list[0])

        btn = Button(root, text='REGISTER', padx=20, pady=5, fg="Green", font=("times new roman", 15, "bold")).place(x=180, y=360)

        def clear_data():
            txt_name.delete(0,END)
            txt_email.delete(0, END)
            txt_mobile.delete(0, END)
            txt_password.delete(0, END)
            droplist_country.current(0)
            r1_gender.deselect()
            r2_gender.deselect()


if __name__ == '__main__':
    root = Tk()
    obj=registration_window(root)
    root.mainloop()