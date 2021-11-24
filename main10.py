from tkinter import *
# from PIL import ImageTk,Image
root=Tk()
root.geometry("553x453")
def myFunc():
    print("My Application is Running")

def getvals():
    print("Submitting form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")

Label(root, text="WELCOME TO FITNESS POINT", font="comicsansms 13 bold", pady=15,fg="white",bg="orange",borderwidth=3).grid(row=0, column=3)

#Text for our form
name = Label(root,text="Name",font="comicsansms 10 bold",fg="blue",bg="yellow").grid(row=4,column=2)
phone = Label(root,text="Phone",font="comicsansms 10 bold",fg="blue",bg="yellow").grid(row=5,column=2)
gender = Label(root,text="Gender",font="comicsansms 10 bold",fg="blue",bg="yellow").grid(row=6,column=2)
emergency = Label(root,text="Emergency Contact No",font="comicsansms 10 bold",fg="blue",bg="yellow").grid(row=7,column=2)
paymentmode = Label(root,text="Payment Mode",font="comicsansms 10 bold",fg="blue",bg="yellow").grid(row=8,column=2)



# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root,textvariable = namevalue)
nameentry.grid(row=4,column=3)
phoneentry = Entry(root,textvariable = phonevalue).grid(row=5,column=3)
genderentry = Entry(root,textvariable = gendervalue).grid(row=6,column=3)
emergencyentry = Entry(root,textvariable = emergencyvalue).grid(row=7,column=3)
paymententry = Entry(root,textvariable = paymentmodevalue).grid(row=8,column=3)



#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=9, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to fitness point ", command=getvals,bg="green").grid(row=11, column=3)
photo=PhotoImage(file="PNG.png")
label=Label(image=photo)

label.grid(row=12,column=10)



mainmenu = Menu(root)
m1= Menu(mainmenu,tearoff=0)
m1.add_command(label="New Project",command=myFunc)
m1.add_command(label="Save",command=myFunc)
m1.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)


m2= Menu(mainmenu,tearoff=0)
m2.add_command(label="New Project",command=myFunc)
m2.add_command(label="Save",command=myFunc)
m2.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3= Menu(mainmenu,tearoff=0)
m3.add_command(label="New Project",command=myFunc)
m3.add_command(label="Save",command=myFunc)
m3.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="View",menu=m3)

m4= Menu(mainmenu,tearoff=0)
m4.add_command(label="New Project",command=myFunc)
m4.add_command(label="Save",command=myFunc)
m4.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Navigate",menu=m4)


m5= Menu(mainmenu,tearoff=0)
m5.add_command(label="New Project",command=myFunc)
m5.add_command(label="Save",command=myFunc)
m5.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Code",menu=m5)


m6= Menu(mainmenu,tearoff=0)
m6.add_command(label="New Project",command=myFunc)
m6.add_command(label="Save",command=myFunc)
m6.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Run",menu=m6)

m7= Menu(mainmenu,tearoff=0)
m7.add_command(label="New Project",command=myFunc)
m7.add_command(label="Save",command=myFunc)
m7.add_command(label="Print",command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Tools",menu=m7)

mainmenu.add_cascade(label="Exit",menu=8,command=quit)



root.mainloop()