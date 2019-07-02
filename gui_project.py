'''import tkinter
root=tkinter.Tk()'''

import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
root=tk.Tk()
root.title('my project')

# if we  import.... from tkinter import *... then there is no need to give the widges as tk or ttk.label we can directly give the Label
# if we write ...from tkinter import tk ....then i have to  use...for eg.. tk.label
#if we use... from tkinter import ttk.... then i have to write ..for eg..ttk.Label

# create the label
name_label=ttk.Label(root,text="Enter the name:")
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(root,text="Enter the age:")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(root,text="Enter the email id :")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(root,text="Enter the gender  :")
gender_label.grid(row=3,column=0,sticky=tk.W)


# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(root,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()     # default the cursor will be on name entry box
age_var=tk.StringVar()
age_entrybox=ttk.Entry(root,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(root,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

# combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(root,width=12,textvariable=gender_var,state='readonly')
gender_combobox['values']=('male','female','other')
gender_combobox.grid(row=3,column=1)
gender_combobox.current(1)   # default value of the combobox will be female which is at position of 1

# radio button
usertype=tk.StringVar()
studentradio=ttk.Radiobutton(root,text="Student",value="student",variable=usertype)
studentradio.grid(row=4,column=0)
teacherradio=ttk.Radiobutton(root,text="Teacher",value="teacher",variable=usertype)
teacherradio.grid(row=4,column=1)

#checkbutton
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(root,text="checked it if details are true  ",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=6)

def action():
    username=name_var.get()
    age = age_var.get()
    email = email_var.get()
    gender=gender_var.get()
    usertypes=usertype.get()
    chkbtn=checkbtn_var.get()
    if chkbtn == 1:
        chkbtn = 'true'
    else:
        chkbtn = "false"

    # if want to print on the terminal
    '''    if chkbtn==0:
        print("details are false")
    else :
        print("details are true ")
    if usertype==studentradio:
        print(" user is student")
    else:
        print("user is teacher")
    print(username)
    print(age)
    print(email)
    print(gender)
    print(usertypes)
# if want to write in txt file 
    with open('file.txt','a') as f:
        f.write(f'{username},{age},{email},{usertypes},{chkbtn}\n')'''

# if want to write in csv file

    with open ('file.csv','a') as f:
        dict_writer=DictWriter(f,fieldnames=['username','userage','useremail','usertype','details','usergender'])
        if os.stat ('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow(
            {
            'username':username,
            'userage':age,
            'useremail':email,
            'usertype':usertypes,
            'details':chkbtn,
            'usergender':gender   }

            )
        name_entrybox.delete(0,tk.END)
        age_entrybox.delete(0,tk.END)
        email_entrybox.delete(0,tk.END)
        name_label.configure(foreground="red")
        email_label.configure(foreground="blue")
        age_label.configure(foreground="yellow")

# create the buttons

submit_button=ttk.Button(root,text="submit",command = action)
submit_button.grid(row=6,column=0)

root.mainloop()
