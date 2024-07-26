from tkinter import *
import tkinter.messagebox as tmx
Login_Page = Tk()
Login_Page.title("Login Page")
Login_Page.maxsize(400,400)
Login_Page.minsize(400,400)
def check(event):
    tmx.showinfo("Information","It is not full made yet")
head = Label(Login_Page,text="Login Page Sample",font="monospace 15 bold",
            fg="#00a4f6", bg="#072e42",pady=10)
head.pack(fill='x')
Page = Frame(Login_Page,pady=40,padx=70,bg='black')
Page.pack(fill='x') 

user_name = StringVar()
user_name.set("Enter UserName")
user_password = StringVar()
user_password.set("Enter Password")

usertext = Label(Page,text="UserName",font="monospace 16 ",
                 fg="#747474",bg="black")
usertext.pack(anchor='nw')
user_field = Entry(Page,textvariable=user_name,font="monospace  "
                   ,bg="#072e42",borderwidth=0,fg="#00a4f6"
                   ,highlightbackground="#126690",highlightcolor="#00a4f6",
                   highlightthickness=1,insertbackground="#126690")
user_field.pack(anchor='nw',pady=5)
passtext = Label(Page,text="Password",font="monospace 16 ",
                 fg="#747474",bg="black")
passtext.pack(anchor='nw')
pass_field = Entry(Page,textvariable=user_password,font="monospace"
                   ,fg="#00a4f6",bg="#072e42",borderwidth=0
                   ,highlightbackground="#126690",highlightcolor="#00a4f6",
                   highlightthickness=1,insertbackground="#126690")
pass_field.pack(anchor='nw',pady=5) 

Sumbit = Button(Page,text="SUMBIT",bg="#00a4f6",
                activeforeground="#00a4f6",activebackground="black"
                ,highlightbackground="#072e42",borderwidth= 1
                ,font="13")
Sumbit.pack(anchor="nw",padx=60,pady=30)
Sumbit.bind('<Button-1>',check)

Login_Page.configure(bg='black')
Login_Page.mainloop()
