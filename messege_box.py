import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

window =tk.Tk()

#label fram
Label_frame= ttk.LabelFrame(window,text="user information")
Label_frame.grid(row=0,column=1,padx=40,pady=10)
#label

name_label=ttk.Label(Label_frame,text="Enter your name:-", font=('Helvetica',15))
age_label=ttk.Label(Label_frame,text="Enter your age:-", font=('Helvetica',15))

#label grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)

#entry variable

name_var=tk.StringVar()
age_var=tk.StringVar()

#entry box
name_entry_box=ttk.Entry(Label_frame,width=36,textvariable=name_var)
age_entry_box=ttk.Entry(Label_frame,width=36,textvariable=age_var)

#grid
name_entry_box.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
age_entry_box.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

#button

def submit():
    name =name_var.get()
    age=age_var.get()
    if name!="":
    
        if age !="":
            try:
                age =int(age)
            except ValueError:
                m_box.showerror('title','Only digits are allowed in age field')
            else:
                if age<18:
                    m_box.showerror("Warning","you are not 18")
                else:
                    print(f"\nYour name is {name}\nYour age is {age}")

        else:
         m_box.showerror("Error","Please fill the age.")
    else:
         m_box.showerror("Error","Please fill the a name.")

submit_button=ttk.Button(window,text="Submit",command=submit)
submit_button.grid(row=1,columnspan=2,padx=40)


window.mainloop()
