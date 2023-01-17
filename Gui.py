import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv
from tkinter import filedialog


class Courses:
    def __init__(self,root):
        FilepathLbl=Label(root,width=15)
        FilepathLbl.config(text="Provide data path",bg="skyblue")
        FilepathLbl.grid(row=0,column=1,padx=(5,10),pady=(20,0))


        self.PathEntry= Entry(root)
        self.PathEntry.grid(row=0,column=2,padx=(0,0),pady=(20,0),columnspan=4,sticky= W+E)
        

        YrLbl=Label(root,width=15)
        YrLbl.config(text="Year",bg="skyblue")
        YrLbl.grid(row=1,column=0,padx=(5,10),pady=(20,0),sticky=W+E)
        n=tk.StringVar ()
        self.YrBox=ttk.Combobox(root,width=5,textvariable=n)
        self.YrBox['values']=('1','2','3','4','5')
        self.YrBox.grid(column=1,row=1,padx=(5,10),pady=(20,0),sticky=W+E)
        self.YrBox.current()

        DepLbl=Label(root)
        DepLbl.config(text="Department",bg="skyblue")
        DepLbl.grid(row=1,column=5,padx=(5,10),pady=(20,0),sticky=W+E)

        self.DpEntry=Entry(root)
        self.DpEntry.grid(row=1,column=7,padx=(10,10),pady=(20,0),sticky=W)

        DspBtn=Button(root,command=self.enter_file_dir)
        DspBtn.config(text="Display",bg="skyblue")
        DspBtn.grid(row=2,column=2,sticky=E,padx=(0,10),pady=(50,0))

        ClrBtn=Button(root)
        ClrBtn.config(text="Clear",bg="skyblue",command=self.delete_items)
        ClrBtn.grid(row=2,column=3,sticky=W+E,padx=(0,10),pady=(50,0))

        SvBtn=Button(root)
        SvBtn.config(text="Save",bg="skyblue")
        SvBtn.grid(row=2,column=4,sticky=W+E,padx=(0,10),pady=(50,0))

        SelCrsLbl=Label(root)
        SelCrsLbl.config(text="Selected courses:",bg="skyblue")
        SelCrsLbl.grid(row=5,column=0,columnspan=12,padx=(10,0),pady=(50,0),ipadx=5,sticky=W)

        self.SelCrsLbx=Listbox(root,width=20)
        self.SelCrsLbx.grid(row=6,column=0,columnspan=12,padx=(10,0),pady=(15,0),sticky=W)

        CrsLbl=Label(root)
        CrsLbl.config(text="Courses",bg="skyblue")
        CrsLbl.grid(row=5,column=3,columnspan=12,padx=(0,0),pady=(50,0),sticky=W+E)

        self.CrsLbx=Listbox(root,width=50)
        self.CrsLbx.grid(row=6,column=3,columnspan=12,padx=(0,0),pady=(15,0),sticky=W+E)
        self.CrsLbx.bind("<<ListboxSelect>>",self.onSelect)
    #C:\\Users\\HP\\Downloads\\sampledata(2).csv   
    def enter_file_dir(self):
        filepath=self.PathEntry.get()
        with open (filepath,"r",encoding="utf-8",errors="ignore")as file:
            for i in file:
                self.CrsLbx.insert("end",i)
    def delete_items(self):
        self.CrsLbx.delete(0,END) 
        self.SelCrsLbx.delete(0,END)   

    def onSelect(self,val):
        sender=val.widget
        idx=sender.curselection()
        value=sender.get(idx)
        print(value)
        self.SelCrsLbx.insert("end",value)
        #self.var.set(value)
    # file_=open(str(filepath)),'r',encoding="utf8", errors="ignore")
        # yy=file_.read()    

        #self.CrsLbx.insert("end",yy)

root=Tk()      
root.resizable(0,0) #disable window size 
root.geometry("645x500+400+200") #size of the window  
root.wm_title(" " * 50 + "Projekti Python") #to set a title  of the window
root.configure(background='darkcyan') #background color
Courses(root)
root.mainloop()






