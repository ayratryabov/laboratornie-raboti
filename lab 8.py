from tkinter import * 
from tkinter import messagebox
from tkinter import scrolledtext
from random import *

window = Tk()
window.title("Лабораторная работа 8")
window.geometry('800x600')
label_1 = Label(window,text = 'Введите количество вещей').place(x=280,y=10)
label_2 = Label(window,text = 'Пиджаков:').place(x=30,y=45)
label_3 = Label(window,text = 'Галстуков:').place(x=200,y=45)
label_4 = Label(window,text = 'Рубашек:').place(x=370,y=45)
label_5 = Label(window,text = 'Брюк:').place(x=540,y=45)
label_6 = Label(window,text = 'Юноша хранит вещи в разных шкафах,и в каждом шкафе его вещи разделены на 3 части по цветам:черный,белый,синий').place(x=10,y=110)
label_7 = Label(window,text = 'Введите цифру для обозначения цвета,черный-1,синий-2,белый-3').place(x=10,y=150)
label_8 = Label(window,text = 'Введите количество вещей').place(x=280,y=10)
label_9 = Label(window,text = 'Пиджаков:').place(x=30,y=175)
label_10 = Label(window,text = 'Галстуков:').place(x=200,y=175)
label_11 = Label(window,text = 'Рубашек:').place(x=370,y=175)
label_12 = Label(window,text = 'Брюк:').place(x=540,y=175)
output_text = scrolledtext.ScrolledText(window,height=10, width=90)
output_text.place(x=50,y=300)
entry_bruk = Entry(window).place(x=540,y=70)
entry_bruk_qw = Entry(window).place(x=540,y=200)

#----------------------------------------------------------

p = StringVar()
quest_P = StringVar()
g = StringVar()
quest_G = StringVar()
r = StringVar()
quest_R = StringVar()
b = StringVar()
quest_B = StringVar()
P = []
G = []
R = []
B = []
def jacket():
    if int(quest_P.get()) == 0 or int(quest_P.get()) > 3:
        return output_text.insert(INSERT,'Вы ввели некоррекную цифру цвета пиджака ')
        
    black_jak =  int(p.get())//3 #1
    blue_jak = (int(p.get()) - black_jak)//2 #2
    white_jak = (int(p.get()) - black_jak)-blue_jak  #3
    if int(p.get()) == 0:
        return P.append('Пиджаков нет')
    if int(quest_P.get()) == 1:
        for i in range(1,black_jak+1):
            P.append(f'Пиджак{i}')
        if int(p.get()) == 1 or int(p.get()) == 2:
            P.append(f"Пиджак1")
    elif int(quest_P.get())== 2:
        if int(p.get()) == 1:
            P.append('Пиджак1')
        if int(p.get()) == 2:
            P.append('Пиджак2')
        else:
            for i in range(black_jak+1,(black_jak+blue_jak)+1):
                P.append(f'Пиджак{i}')
        
    elif int(quest_P.get()) == 3:
        if int(p.get()) == 1 or int(p.get()) == 2:
            P.append('Пиджак1 ')
        else:
            for i in range((black_jak+blue_jak)+1,black_jak+blue_jak+white_jak+1):
                P.append(f'Пиджак{i} ')

    fasons = ['Классический ','Спортивный ','Френч ','Блейзер ','Смокинг ']
    for i in range(len(P)):
        P[i] = choice(fasons) + P[i]

def galst():
    if int(quest_G.get()) == 0 or int(quest_P.get()) > 3:
        return output_text.insert(INSERT,'Вы ввели некоррекную цифру цвета галстука ')
    
    black_tie =  int(g.get())//3 #1
    blue_tie = (int(g.get()) - black_tie)//2 #2
    white_tie = (int(g.get()) - black_tie)-blue_tie  #3
    if int(g.get()) == 0:
        return G.append('Галстуков нет')
    if int(quest_G.get()) == 1:
        for i in range(1,black_tie+1):
            G.append(f'Галстук{i}   ')
        if int(g.get()) == 1 or int(g.get()) == 2:
            G.append(f"Галстук1")
    elif int(quest_G.get()) == 2:
        if int(g.get()) == 1:
            G.append('Галстук1')
        if int(g.get()) == 2:
            G.append('Галстук2')
        else:
            for i in range(black_tie+1,(black_tie+blue_tie)+1):
                G.append(f'Галстук{i}')
            
    elif int(quest_G.get()) == 3:
        if int(g.get()) == 1 or int(g.get()) == 2:
            G.append('Галстук1')
        else:
            for i in range((black_tie+blue_tie)+1,black_tie+blue_tie+white_tie+1):
                G.append(f'Галстук{i}')
    fasons = ['Бабочка-','Техасский-','Лаварьер-','Регат-','Скинни-', 'Платок-']
    knots = ['Бальтус-узел: ','Виктория-узел: ','Восточный узел: ','Двойной узел: ','Диагональный узел: ','Кент-узел: ','крестовый узел: ','Манхэттен-узел: ','Никки-узел: ','Простой узел: ']
    for i in range(len(G)):
        G[i] = choice(fasons) + G[i]
    for i in range(len(G)):
        G[i] = choice(knots) + G[i]
def rub():
    if int(quest_R.get()) == 0 or int(quest_P.get()) > 3:
        return output_text.insert(INSERT,'Вы ввели некоррекную цифру цвета рубашек ' )
    black_t =  int(r.get())//3 #1
    blue_t = (int(r.get()) - black_t)//2 #2
    white_t = (int(r.get()) - black_t)-blue_t  #3
    if int(r.get()) == 0:
        return R.append('Рубашек нет')
    if int(quest_R.get()) == 1:
        for i in range(1,black_t+1):
            R.append(f'Рубашка{i}')
        if int(r.get()) == 1 or int(r.get()) == 2:
            R.append(f"Рубашка1")
    elif int(quest_R.get()) == 2:
        if int(r.get()) == 1:
            R.append('Рубашка1')
        if int(r.get()) == 2:
            R.append('Рубашка2')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                R.append(f'Рубашка{i} ')
    elif int(quest_R.get()) == 3:
        if int(r.get()) == 1 or int(r.get()) == 2:
            R.append('Рубашка1')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                R.append(f'Рубашка{i}')
    fasons = ['Свободного фасона ','Классического фасона ','Приталенного фасона ','Современного фасона ']
    for i in range(len(R)):
        R[i] = choice(fasons) + R[i]

def bruk():
    if int(quest_R.get()) == 0 or int(quest_P.get()) > 3:
        return output_text.insert(INSERT,'Вы ввели некоррекную цифру цвета брюк ')
    black_t =  int(b.get())//3 #1
    blue_t = (int(b.get()) - black_t)//2 #2
    white_t = (int(b.get()) - black_t)-blue_t  #3
    if int(b.get()) == 0:
        return B.append('Брюк нет')
    if int(quest_B.get()) == 1:
        for i in range(1,black_t+1):
            B.append(f'Брюки{i}')
        if int(b.get()) == 1 or int(b.get()) == 2:
            B.append(f"Брюки1")
    elif int(quest_B.get()) == 2:
        if int(b.get()) == 1:
            B.append('Брюки1')
        if int(b.get()) == 2:
            B.append('Брюки2')
        else:
            for i in range(black_t+1,(black_t+blue_t)+1):
                B.append(f'Брюки{i}')
    elif int(quest_B.get()) == 3:
        if int(b.get()) == 1 or int(b.get()) == 2:
            B.append('Брюки1')
        else:
            for i in range((black_t+blue_t)+1,black_t+blue_t+white_t+1):
                B.append(f'Брюки{i}')
    fasons = ['Классические ','Чинос ','Карго ','Джлггеры ','Бананы ','Скинни ']
    for i in range(len(B)):
        B[i] = choice(fasons) + B[i]

kost_ob = []
 
def result():
    global kost_ob
    kost = []
    for ii in P:
        for jj in G:
            for hh in R:
                for gg in B:
                    kost.append(ii)
                    kost.append(jj)
                    kost.append(hh)
                    kost.append(gg)
                    kost_ob.append(kost)
                    
                    kost = []

def price():
    count = 0
    for i in kost_ob:
        for j in i:
            if j.rstrip()[-1].isdigit() == True:
                if 1<=int(j.rstrip()[-1])<=5:
                    count += randint(5,15)
                elif 5<=int(j.rstrip()[-1])<=15:
                    count += randint(15,25)
                else:
                    count += randint(25,50)
                
            else:
                count += 0
        i.append(f'Цена костюма {count}$')
        count = 0
    res  = '\n'.join(map(str,kost_ob))
    return output_text.insert(INSERT,res)

def zero():
    global P
    global G
    global R
    global B
    global kost_ob
    P = []
    G = []
    R = []
    B = []
    kost_ob = []
def zero1():
    output_text.delete(1.0,END)
      
button = Button(window,text='Поиск',command=lambda:[zero1(),jacket(),galst(),rub(),bruk()
    ,result(),price(),zero()]).place(x=280,y=250)
entry_pidj = Entry(window,textvariable=p).place(x=30,y=70)
entry_pidj_qw = Entry(window,textvariable=quest_P).place(x=30,y=200)
entry_gals = Entry(window,textvariable=g).place(x=200,y=70)
entry_gals_qw= Entry(window,textvariable=quest_G).place(x=200,y=200)
entry_rub = Entry(window,textvariable=r).place(x=370,y=70)
entry_rub_qw = Entry(window,textvariable=quest_R).place(x=370,y=200)
entry_bruk = Entry(window,textvariable=b).place(x=540,y=70)
entry_bruk_qw = Entry(window,textvariable=quest_B).place(x=540,y=200)
window.mainloop()
