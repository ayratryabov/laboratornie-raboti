from tkinter import *
from tkinter import font
from random import *
from tkinter import messagebox
game = Tk()
game.title('Крестики-нолики')
game.geometry('350x255')
game.resizable(False, False)
butts = [Button(width=12,height=4  ,bg = 'green' ,font = ('Arial', 12),command = lambda i=i : click(i))for i in range(9)]
row = 1
cul = 0
gm = [None]*9
for i in range(9):
    butts[i].grid(row=row,column=cul)
    cul += 1
    if cul == 3:
        row +=1
        cul = 0
c = 0
t = None
win_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def win_man():
    cn = 0
    for i in win_comb:
        for j in i:
            if gm[j] == 'X':
                cn += 1
                
                if cn == 3:
                    return True
                    break
        cn = 0        
a = [] 
def win_comp():
    cn = 0
    
    for i in win_comb:
        for j in i:
            if gm[j] == 'O':
                cn += 1
                
                if cn == 3:
                    return True
                    
                
        cn = 0        

def restart():
    global gm
    gm = [None]*9 
    a = []
    for but in butts:
        but.config(text=' ',bg = 'Green',state = 'normal')


def bot():
    ind = None
    if ind is None:
        z = []
        if gm.count(None) == 8 and gm[4] == None:
            ind = 4
            gm[ind] = 'O'
            butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
        elif gm.count(None) == 8 and gm[4] == 'X':
            z = [0,2,6,8]
            ind = choice(z)
            gm[ind] = 'O'
            butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
    if ind is None:
        for i in win_comb:
            var = [gm[i[0]],gm[i[1]],gm[i[2]]]
            if var.count('O') == 2 and var.count(None) == 1:
                ind = i[var.index(None)]
                gm[ind] = 'O'
                butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
                break
        
    if ind is None:
        for i in win_comb:
            var = [gm[i[0]],gm[i[1]],gm[i[2]]]
            if var.count('X') == 2 and var.count(None) == 1:
                ind = i[var.index(None)]
                gm[ind] = 'O'
                butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
                break
       
    if ind is None:
        for i in win_comb:
            var = [gm[i[0]],gm[i[1]],gm[i[2]]]
            if var.count('O') == 1 and var.count(None) == 2:
                ind = i[var.index(None)]
                gm[ind] = 'O'
                butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
                break
        
    if ind is None:
        for i in win_comb:
            var = [gm[i[0]],gm[i[1]],gm[i[2]]]
            if var.count('X') == 1 and var.count(None) == 2:
                ind = i[var.index(None)]
                gm[ind] = 'O'
                butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
                break
       
    if ind is None:
        if gm[4] == None:
            ind = 4
            gm[ind] == 'O'
            butts[4].config(text='O',width=12,height=4 ,bg='white',state='disabled',)
            
        
    if ind is None:
        inds = []
        for i in gm:
            if i is None:
                ind = gm.index(i)
                inds.append(ind)
        if len(inds) == 0:
            messagebox.showinfo('Конец игры','Ничья!')
            restart()
        else:
            ind = choice(inds)
            gm[ind] = 'O'
            butts[ind].config(text='O',width=12,height=4 ,bg='white',state='disabled')
        

            
    if win_comp() == True:
        messagebox.showinfo('Конец игры','Компьютер победил!')
        restart()
    if win_man() == True:
        messagebox.showinfo('Конец игры','Вы победили!')
        restart()
    

def click(b):
    gm[b] = 'X'

    butts[b].config(text='X',width=12,height=4 ,bg='white',state='disabled',)
    bot()
    
game.mainloop()






















