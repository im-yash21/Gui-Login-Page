from tkinter import *
import tkinter.messagebox as tmx
Login_Page = Tk()
Login_Page.title("Login Page")
Login_Page.maxsize(400,400)
Login_Page.minsize(400,400)
head = Label(Login_Page,text="Login Page Sample",font="monospace 15 bold",
            fg="#00a4f6", bg="#072e42",pady=10)
head.pack(fill='x')
Page = Frame(Login_Page,pady=40,padx=70,bg='black')
Page.pack(fill='x') 

#for valid user name
def usernametrue():
    _len_ = len(user_name.get())
    if(user_name.get().isidentifier() and (_len_ >= 4 and _len_ <=10)):
            for i in user_name.get():
                if( i>='A' and i<='Z'):
                    return False
            return True  
    
#for checking username      
def checking_username():
    try:
        f = open('Login_Page.txt','r').read().split('\n')
        for i in f:
            for j in i.split(":"):
                if j == user_name.get():
                    tmx.showinfo("Already"
                                 ,"username is already in use")
                    return False        
        return usernametrue()           
    except:
        return usernametrue()
    
#for checking password
def checking_pass():
    _len_ = len(user_password.get())
    flag = 0
    if(0 < user_password.get().find(' ')):
        return False
    for i in user_password.get():
        if (i.isnumeric()):
            flag += 1
    if not (flag):
        return False        
    if( _len_ >= 6 and _len_ <=12):
        return False if(user_password.get().isalnum()) else True

#main function (button click action)
def check(event):
    flag_1 = checking_username()
    flag_2 = checking_pass()
    if(flag_1 and flag_2):
        flag = tmx.askyesno('Log In'
                            ,"Do you want to save username and Password in text file")
        if(flag):
            text = f"username:{user_name.get()}\npassword:{user_password.get()}\n"
            f = open('Login_Page.txt','a')
            f.write(text)
            f.close()
            tmx.showinfo(message="Succesfully Save in Login_Page.txt File")
        else:
            tmx.showinfo('Delete'
                            ,f"Username :{user_name.get()}\nis deleted now because you not save it")    
    else:
        if not flag_1:
            tmx.showwarning('UserName'
                          ,'Username does not contain\nAnyspace\nUpperCase character\nmust be unique')
        if not flag_2:
            tmx.showwarning("Password",
                          "Password does not contain \nAnyspace,\nlength 6<= password >=12,\natleast one number\nand special charactar")
#for storing username and password        
user_name = StringVar().set("enter username")
user_password = StringVar().set("enter password")

#for username
usertext = Label(Page,text="UserName",font="monospace 16 ",
                 fg="#747474",bg="black").pack(anchor='nw')
user_field = Entry(Page,textvariable=user_name,font="monospace  "
                   ,bg="#072e42",borderwidth=0,fg="#00a4f6"
                   ,highlightbackground="#126690",highlightcolor="#00a4f6",
                    highlightthickness=1
                    ,insertbackground="#126690").pack(anchor='nw',pady=5)

#for password
passtext = Label(Page,text="Password",font="monospace 16 ",
                 fg="#747474",bg="black").pack(anchor='nw')
pass_field = Entry(Page,textvariable=user_password,font="monospace"
                   ,fg="#00a4f6",bg="#072e42",borderwidth=0
                   ,highlightbackground="#126690",highlightcolor="#00a4f6",
                   highlightthickness=1
                   ,insertbackground="#126690").pack(anchor='nw',pady=5)

#For Sumbit handle
Sumbit = Button(Page,text="SUMBIT",bg="#00a4f6",
                activeforeground="#00a4f6",activebackground="black"
                ,highlightbackground="#072e42",borderwidth= 1
                ,font="13")
Sumbit.pack(anchor="nw",padx=60,pady=30)
Sumbit.bind('<Button-1>',check)

Login_Page.configure(bg='black')
Login_Page.mainloop()
