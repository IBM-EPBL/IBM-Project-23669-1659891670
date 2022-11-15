from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem():
    def __init__(self,root):
         self.root=root
         self.root.title("Pharmacy Managment System")
         self.root.geometry("1550x800+0+0")

          #=========Add variables===============
         self.addmed_var=StringVar()
         self.refMed_var=StringVar()

         #===============Text variable===============
         self.ref_var=StringVar()
         self.cmpName_var=StringVar()
         self.typeMed_var=StringVar()
         self.medName_var = StringVar()
         self.issuedate_var = StringVar()
         self.expdate_var = StringVar()
         self.uses_var = StringVar()
         self.dosage_var = StringVar()
         self.price_var = StringVar()
         self.product_var = StringVar()
         self.totalprice_var=StringVar()

         lbltitle=Label(self.root, text="PHARAMACY MANAGEMENT SYSTEM ", bd=15, relief=RIDGE, bg='white', fg='darkgreen', font=("times new roman", 40, "bold"),)
         lbltitle.pack(side=TOP, fill=X)

         img1=Image.open('images/logo.png')
         img1=img1.resize((60,60),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         b1=Button(self.root,image=self.photoimg1,borderwidth=0)
         b1.place(x=50,y=15)
 #=============================DATA FRAME ====================
         DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
         DataFrame.place(x=0,y=100,width=1280,height=300)

         DataFrameleft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("Arial",12,"bold"))
         DataFrameleft.place(x=0, y=5, width=750, height=250)

 #=================== BUTTTONSFRAME=========================================
         ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=5)
         ButtonFrame.place(x=0, y=400, width=1280, height=65)

 #=================== MAIN BUTTTONS=========================================
         btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("Arial",12,"bold"),bg="darkgreen",fg='white')
         btnAddData.grid(row=0,column=0)

         btnupdateMed = Button(ButtonFrame,command=self.Update, text="UPDATE", font=("Arial", 12, "bold"),width=12,bg="darkgreen",fg='white')
         btnupdateMed.grid(row=0, column=1)

         btnDeleteMed = Button(ButtonFrame,command=self.delete, text="DELETE", font=("Arial", 12, "bold"),width=12, bg="darkgreen", fg='white')
         btnDeleteMed.grid(row=0, column=2)

         btnRestMed = Button(ButtonFrame,command=self.reset, text="RESET", font=("Arial", 12, "bold"), width=12, bg="darkgreen",fg='white')
         btnRestMed.grid(row=0, column=3)

         btnExitMed = Button(ButtonFrame,command=root.destroy, text="EXIT", font=("Arial", 12, "bold"), width=12, bg="darkgreen", fg='white')
         btnExitMed.grid(row=0, column=4)
#
# #=================SEARCH BY ==============
         lblSearch = Button(ButtonFrame, text="Search by",font=("Arial", 12, "bold"), bg="red", fg='white')
         lblSearch.grid(row=0, column=5,sticky=W)

         self.search_var=StringVar()
         search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",12,"bold"),state="readonly")
         search_combo["values"]=("ref","medname","Lot")
         search_combo.grid(row=0,column=6)
         search_combo.current(0)

         self.searchTxt_var=StringVar()

         txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",12,"bold"))
         txtSearch.grid(row=0,column=7)

         searchbtn = Button(ButtonFrame, text="Search", font=("Arial", 12, "bold"), width=12, bg="darkgreen",fg='white')
         searchbtn.grid(row=0, column=8)

         showAll = Button(ButtonFrame,command=self.fetch_data, text="SHOW ALL", font=("Arial", 12, "bold"), width=12, bg="darkgreen",fg='white')
         showAll.grid(row=0, column=9)

#=================label and entry ==================
         lblrefno=Label(DataFrameleft,font=("arial",10,"bold"),text="Reference no.",padx=2)
         lblrefno.grid(row=0,column=0,sticky=W)

         ref_combo=ttk.Combobox(DataFrameleft,width=23,font=("arial",10,"bold"),state="readonly")
         ref_combo = Entry(DataFrameleft,textvariable=self.ref_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         ref_combo.grid(row=0,column=1)
         
         lblCmpName = Label(DataFrameleft,font=("arial",10,"bold"),text="Company Name:",padx=2,pady=5)
         lblCmpName.grid(row=1,column=0,sticky=W)
         txtCmpName=Entry(DataFrameleft,textvariable=self.cmpName_var, font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=25)
         txtCmpName.grid(row=1,column=1)

         lblTypeofMedicine = Label(DataFrameleft, font=("arial", 10, "bold"), text="Type of Medicine", padx=2, pady=5)
         lblTypeofMedicine.grid(row=2, column=0, sticky=W)

         comTypeofMedicine=ttk.Combobox(DataFrameleft,textvariable=self.typeMed_var,state="readonly",font=("arial",10,"bold"),width=23)
         comTypeofMedicine['value']=("Tablet","Liquid","capsules","Topical Medicines","Drops","Inhales","Injection")
         comTypeofMedicine.current(0)
         comTypeofMedicine.grid(row=2,column=1)

#===================addmedicine================
         lblMedicineName = Label(DataFrameleft, font=("arial", 10, "bold"), text="Medicine Name", padx=2, pady=5)
         lblMedicineName.grid(row=3,column=0,sticky=W)

         '''conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata", port="3306")
         my_cursor = conn.cursor()
         my_cursor.execute("select Medicine_Name from pharma")
         med=my_cursor.fetchall()'''

         comMedicineName = ttk.Combobox(DataFrameleft,textvariable=self.medName_var,width=23, font=("arial",10,"bold"),state="readonly")
         comMedicineName = Entry(DataFrameleft,textvariable=self.medName_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         comMedicineName.grid(row=3,column=1)

         lblIssueDate = Label(DataFrameleft, font=("arial", 10, "bold"), text="Issue Date:", padx=2, pady=5)
         lblIssueDate.grid(row=4, column=0, sticky=W)
         txtIssueDate = Entry(DataFrameleft,textvariable=self.issuedate_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtIssueDate.grid(row=4, column=1)

         lblExpDate = Label(DataFrameleft, font=("arial", 10, "bold"), text="Expiry Date:", padx=2, pady=5)
         lblExpDate.grid(row=5, column=0, sticky=W)
         txtExpDate = Entry(DataFrameleft,textvariable=self.expdate_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtExpDate.grid(row=5, column=1)

         lblUses = Label(DataFrameleft, font=("arial", 10, "bold"), text="Uses:", padx=15)
         lblUses.grid(row=6, column=0, sticky=W)
         txtUses = Entry(DataFrameleft,textvariable=self.uses_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtUses.grid(row=6, column=1)

         lblDosage = Label(DataFrameleft, font=("arial", 10, "bold"), text="Dosage:", padx=15, pady=5)
         lblDosage.grid(row=0, column=2, sticky=W)
         txtDosage = Entry(DataFrameleft,textvariable=self.dosage_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtDosage.grid(row=0, column=3)

         lblPrice = Label(DataFrameleft, font=("arial", 10, "bold"), text="Price:", padx=15, pady=5)
         lblPrice.grid(row=1, column=2, sticky=W)
         txtPrice = Entry(DataFrameleft,textvariable=self.price_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtPrice.grid(row=1, column=3)

         lblProductQt = Label(DataFrameleft, font=("arial", 10, "bold"), text="Product Qt:", padx=15, pady=5)
         lblProductQt.grid(row=2, column=2, sticky=W)
         txtProductQt = Entry(DataFrameleft,textvariable=self.product_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=25)
         txtProductQt.grid(row=2, column=3)

         lbltotalPrice = Label(DataFrameleft, font=("arial", 10, "bold"), text="Total Price:", padx=15, pady=5)
         lbltotalPrice.grid(row=3, column=2, sticky=W)
         txttotalPrice = Entry(DataFrameleft, textvariable=self.totalprice_var, font=("arial", 10, "bold"), bg="white",
                              bd=2, relief=RIDGE, width=25)
         txttotalPrice.grid(row=3, column=3)

         #==========images================
         img2 = Image.open('images/tablet.jpg')
         img2 = img2.resize((120, 75), Image.ANTIALIAS)
         self.photoimg2 = ImageTk.PhotoImage(img2)
         b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
         b1.place(x=1120, y=138)

         lblhome = Label(DataFrameleft, font=("arial", 15, "bold"), text="Stay Home Stay Safe", padx=20, pady=5,bg="red",fg="white")
         lblhome.grid(row=6, column=3, sticky=W)

         #=========DataframeRight===========

         DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Billing Department", fg="darkgreen",
                                font=("Arial", 12, "bold"))
         DataFrameRight.place(x=775, y=5, width=450, height=250)

         lblrefno = Label(DataFrameRight, font=("arial", 10, "bold"), text="Quantity:", padx=0, pady=5)
         lblrefno.place(x=0, y=25)
         txtrefno = Entry(DataFrameRight, textvariable=self.refMed_var, font=("arial", 10, "bold"), bg="white", bd=2,relief=RIDGE, width=20)
         txtrefno.place(x=120, y=30)

         lblmedName = Label(DataFrameRight, font=("arial", 10, "bold"), text="Medicine Name:", padx=0, pady=5)
         lblmedName.place(x=0, y=0)
         txtmedName = Entry(DataFrameRight,textvariable=self.addmed_var, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=20)
         txtmedName.place(x=120, y=5)
        #=============sideframe=============
         side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE,bg="white")
         side_frame.place(x=0, y=70, width=270, height=140)

         sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
         sc_x.pack(side=BOTTOM,fill=X)
         sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
         sc_y.pack(side=RIGHT, fill=Y)

         self.medicine_table = ttk.Treeview(side_frame,column=("ref","medicine"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

         sc_x.config(command=self.medicine_table.xview)
         sc_y.config(command=self.medicine_table.yview)

         self.medicine_table.heading("ref",text="Ref")
         self.medicine_table.heading("medicine",text="Medicine Name")

         self.medicine_table["show"]="headings"
         self.medicine_table.pack(fill=BOTH,expand=1)

         self.medicine_table.column("ref",width=100)
         self.medicine_table.column("medicine",width=100)

         self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #==========medicine add buttons===================
         down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
         down_frame.place(x=290,y=78,width=95,height=132)

         btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",8,"bold"),width=11,bg="lime",fg="white",pady=4)
         btnUpdatemed.grid(row=1,column=0)

         btnAddmed = Button(down_frame, text="ADD", font=("arial", 8, "bold"), width=11, bg="purple", fg="white",pady=4)
         btnAddmed.grid(row=0, column=0)

         btnDeletemed = Button(down_frame, text="DELETE", font=("arial", 8, "bold"), width=11, bg="red", fg="white",pady=4)
         btnDeletemed.grid(row=2, column=0)

         btnClearmed = Button(down_frame, text="Clear", font=("arial", 8, "bold"), width=11, bg="orange", fg="white",pady=4)
         btnClearmed.grid(row=3, column=0)

         btnPrint = Button(down_frame,command=self.Print, text="Print", font=("arial", 8, "bold"), width=11, bg="orange", fg="white",pady=4)
         btnPrint.grid(row=3, column=0)

         #=========Frame Details===========
         Framedetails = Frame(self.root,bd=15,relief= RIDGE)
         Framedetails.place(x=0,y=465,width=1280,height=190)

        #==========table frame================
         Table_frame = Frame(self.root, bd=15, relief=RIDGE)
         Table_frame.place(x=0, y=465, width=1270, height=180)

         scroll_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
         scroll_x.pack(side=BOTTOM, fill=X)
         scroll_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
         scroll_y.pack(side=RIGHT, fill=Y)

         self.pharmacy_table = ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","issuedate",
                                                                "expdate","uses","dosage","price","productqt","totalPrice")
                                                                 ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


         scroll_x.config(command=self.pharmacy_table.xview)
         scroll_y.config(command=self.pharmacy_table.yview)

         self.pharmacy_table["show"]="headings"
         self.pharmacy_table.pack(fill=BOTH, expand=1)

         self.pharmacy_table.heading("reg",text="Reference No")
         self.pharmacy_table.heading("companyname", text="Company Name")
         self.pharmacy_table.heading("type", text="Type of Medicine")
         self.pharmacy_table.heading("tabletname", text="Mediicine Name")
         #self.pharmacy_table.heading("lotno", text="Lot No")
         self.pharmacy_table.heading("issuedate", text="Issue Date")
         self.pharmacy_table.heading("expdate", text="Exp Ddate")
         self.pharmacy_table.heading("uses", text="Uses")
         #self.pharmacy_table.heading("sideeffect", text="Side Effect")
         #self.pharmacy_table.heading("warning", text="Prec&Warning")
         self.pharmacy_table.heading("dosage", text="Dosage")
         self.pharmacy_table.heading("price", text="Price")
         self.pharmacy_table.heading("productqt", text="Product Qts")
         self.pharmacy_table.heading("totalPrice", text="Total Price")

         self.pharmacy_table["show"] = "headings"
         self.pharmacy_table.pack(fill=BOTH, expand=1)


         self.pharmacy_table.column("reg",width=90)
         self.pharmacy_table.column("companyname", width=90)
         self.pharmacy_table.column("type", width=95)
         self.pharmacy_table.column("tabletname", width=90)
         #self.pharmacy_table.column("lotno", width=90)
         self.pharmacy_table.column("issuedate", width=90)
         self.pharmacy_table.column("expdate", width=90)
         self.pharmacy_table.column("uses", width=90)
         #self.pharmacy_table.column("sideeffect", width=90)
         #self.pharmacy_table.column("warning", width=90)
         self.pharmacy_table.column("dosage", width=90)
         self.pharmacy_table.column("price", width=90)
         self.pharmacy_table.column("productqt", width=90)
         self.pharmacy_table.column("totalPrice", width=90)
         self.fetch_dataMed()
         self.fetch_data()
         self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

#=========================Add medicine functionality declaration========================
    def AddMed(self):
              conn=mysql.connector.connect(host="localhost",user="root", password="Sarth0310", database="mydata")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into pharma(Reference_No,Medecine_Name) values(%s,%s)",(
                                                                 self.refMed_var.get(),
                                                                 self.addmed_var.get()

                                                                  ))
              conn.commit()
              self.fetch_dataMed()
              conn.close()
              messagebox.showinfo("success","Medicine Added.")
              self.Medget_cursor()

    def fetch_dataMed(self):
              conn=mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
              my_cursor= conn.cursor()
              my_cursor.execute("SELECT * FROM pharma")
              rows = my_cursor.fetchall()
              if len(rows)!=0:
                   self.medicine_table.delete(*self.medicine_table.get_children())
                   for i in rows:
                        self.medicine_table.insert("",END,values=i)
                   conn.commit()
              conn.close()

#==============================MedGetCursor===============================
    def Medget_cursor(self,event=""):
         cursor_row=self.medicine_table.focus()
         content = self.medicine_table.item(cursor_row)
         row = content["values"]
         self.refMed_var.set(row[0])
         self.addmed_var.set(row[1])

#=========================Update function ====================================
    def UpdateMed(self):
         if self.refMed_var.get()=="" or self.addmed_var.get()=="":
              messagebox.showerror("Error","All fields are Required")
         else:
              conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
              my_cursor = conn.cursor()
              my_cursor.execute("update pharma set Medecine_Name=%s where Reference_No=%s",(
                                                                            self.addmed_var.get(),
                                                                            self.refMed_var.get(),
                                                                            ))
              conn.commit()
              self.fetch_dataMed()
              conn.close()

              messagebox.showinfo("Success","Medicine has been updated.")

#===================Delete medicine==================================
    def DeleteMed(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
         my_cursor = conn.cursor()

         sql="delete from pharma where Reference_No=%s"
         val=(self.refMed_var.get(),)
         my_cursor.execute(sql,val)

         conn.commit()
         self.fetch_dataMed()
         conn.close()

#===============Print function========================
    def Print(self):
         self.refMed_var.set("")
         self.addmed_var.set("")
         messagebox.showinfo("Print","Bill has been printed")

#================== Main table=================================================

    def add_data(self):
               conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
               my_cursor = conn.cursor()

               my_cursor.execute("insert into pharma values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.ref_var.get(),
                                                                                        self.cmpName_var.get(),
                                                                                        self.typeMed_var.get(),
                                                                                        self.medName_var.get(),
                                                                                        self.issuedate_var.get(),
                                                                                        self.expdate_var.get(),
                                                                                        self.uses_var.get(),
                                                                                        self.dosage_var.get(),
                                                                                        self.product_var.get(),
                                                                                        self.price_var.get(),
                                                                                        self.totalprice_var.get()
                                                                                        ))

               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Data has been inserted")

    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
         my_cursor = conn.cursor()
         my_cursor.execute("SELECT * FROM pharma")
         row=my_cursor.fetchall()
         if len(row)!=0:
              self.pharmacy_table.delete(*self.pharmacy_table.get_children())
              for i in row:
                   self.pharmacy_table.insert("",END,values=i)
              conn.commit()
         conn.close()

    def get_cursor(self,ev=""):
         cursor_row = self.pharmacy_table.focus()
         content = self.pharmacy_table.item(cursor_row)
         row = content["values"]
         self.ref_var.set(row[0])
         self.cmpName_var.set(row[1])
         self.typeMed_var.set(row[2])
         self.medName_var.set(row[3])
         self.issuedate_var.set(row[4])
         self.expdate_var.set(row[5])
         self.uses_var.set(row[6])
         self.dosage_var.set(row[7])
         self.price_var.set(row[8])
         self.product_var.set(row[9])
         self.totalprice_var.set(row[10])

    def Update(self):
         if self.ref_var.get()=="":
              messagebox.showerror("Error","All fields are Required")
         else:
              conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
              my_cursor = conn.cursor()
              my_cursor.execute("update pharma set Company_Name=%s, Types_of_Medicine=%s, Medicine_Name=%s, issu_date=%s, Exp_Date=%s, Uses=%s, Dosage=%s, Product_QT=%s, Tablets_Price=%s, Total_Price=%s where Reference_No=%s",(
                                                                                                                           self.cmpName_var.get(),
                                                                                                                           self.typeMed_var.get(),
                                                                                                                           self.medName_var.get(),
                                                                                                                           self.issuedate_var.get(),
                                                                                                                           self.expdate_var.get(),
                                                                                                                           self.uses_var.get(),
                                                                                                                           self.dosage_var.get(),
                                                                                                                           self.product_var.get(),
                                                                                                                           self.price_var.get(),
                                                                                                                           self.totalprice_var.get(),
                                                                                                                           self.ref_var.get(),
                                                                                                                                             ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Medicine has been updated.")

    def delete(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
         my_cursor = conn.cursor()

         sql = "delete from pharma where Reference_No=%s"
         val = (self.ref_var.get(),)
         my_cursor.execute(sql, val)

         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("Delete", "Information deleted successfully")

    def reset(self):
         #self.ref_var.set("")
         self.cmpName_var.set("")
         #self.typeMed_var.set("")
         #self.medName_var.set("")
         #self.lot_var.set("")
         self.issuedate_var.set("")
         self.expdate_var.set("")
         self.uses_var.set("")
         self.sideffect_var.set("")
         self.warning_var.set("")
         self.dosage_var.set("")
         self.price_var.set("")
         self.product_var.set("")
         self.totalprice_var.set("")

    def search_data(self):
         conn = mysql.connector.connect(host="localhost", user="root", password="Sarth0310", database="mydata")
         my_cursor = conn.cursor()

         my_cursor.execute('''"select * from pharmacy where "+str(self.search_var.get())+"LIKE"+str(self.searchTxt_var.get())+"%"''')

         rows= my_cursor.fetchall()
         if len(rows)!=0:
              self.pharmacy_table.delete(*self.pharmacy_table.get_children())
              for i in rows:
                   self.pharmacy_table.insert("",END,values=i)
              conn.comit()
         conn.close()


if __name__ == '__main__':
    root = Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()