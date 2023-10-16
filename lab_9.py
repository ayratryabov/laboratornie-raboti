from tkinter import * 
from tkinter import messagebox
from functools import partial



baza = [[0,0]]
#------------------------------------------------------------------------------
def click():
    register = Toplevel(login)
    register.title('Регистрация')
    register.geometry('300x300')
    register.resizable(False, False)
    
    label_1 = Label(register,text = 'Придумайте логин').place(x=80,y=60)
    label_2 = Label(register,text = 'Придумайте пароль').place(x=80,y=120)
    label_3 = Label(register,text = 'Повторите пароль').place(x=80,y=180)
    
    def registr(Log,Pass,Pass2):
        data = []    
        log = Log.get() 
        pas = Pass.get()
        pas1 = Pass2.get()
        if pas == pas1:
            data.append(log)
            data.append(pas)
            baza.append(data)
            messagebox.showinfo('','Регистрация завершена')
            register.destroy()
            
        else:
            messagebox.showwarning('Внимательнее!','Пароли не совпадают!')
            register.focus()
            
    Log = StringVar()
    Pass = StringVar()
    Pass2 = StringVar()
    registr = partial(registr,Log,Pass,Pass2)
    button4 = Button(register,text='Зарегестрироваться',command = registr).place(x=80,y=240)
    entry_log = Entry(register,textvariable=Log).place(x=80,y=80)
    entry_pass = Entry(register,textvariable=Pass).place(x=80,y=140)
    entry_pass1 = Entry(register,textvariable=Pass2).place(x=80,y=200)
    
login = Tk()
login.title('Вход')
login.geometry('300x300')
login.resizable(False, False)
label_5 = Label(login,text = 'Введите логин').place(x=80,y=60)
label_6 = Label(login,text = 'Введите пароль').place(x=80,y=120)

but1 = Button(text='Регистрация',command=click).place(x=40,y=200)
but2 = Button(text='   Вход   ',).place(x=190,y=200)

def click_2(Log1,Pas_1):
   
    log = Log1.get()
    pas = Pas_1.get()
    
    c = 0
    for i in range(len(baza)):        
        if log == baza[i][0] and pas == baza[i][1]:
            game = Toplevel(login)
            game.title('Игра')
            game.geometry('500x500')
            c += 1
    if c == 0:
        messagebox.showwarning('Предупреждение','Данные не найдены,попробуйте снова или зарегистрируйтесь')

            
Log1 = StringVar()
Pas_1 = StringVar()
click_2 = partial(click_2,Log1,Pas_1)
but2 = Button(text='   Вход   ',command=click_2).place(x=190,y=200)

entry_log1 = Entry(textvariable=Log1).place(x=80,y=80)
entry_pass1 = Entry(textvariable=Pas_1).place(x=80,y=140)
login.mainloop()

