from random import *
class All_elem_kostums:
    def __init__(self,n,lot,qw):
        self.n = n
        self.lot = lot
        self.qw = qw
        self.LIST = []
   
        
        
    def method(self):
        
        self.black = self.lot //3 
        self.blue = (self.lot - self.black)//2 #2
        self.white = (self.lot - self.black)-self.blue
        if self.qw == 1:
            if self.lot == 1 or self.lot == 2:
                self.LIST.append(f"{self.n}1")
            else:
                for i in range(1,self.black+1):
                    self.LIST.append(f'{self.n}{i}')
                    
        elif self.qw == 2:
            if self.lot == 1:
                self.LIST.append(f'Cиний {self.n} отсутствует')
            if self.lot == 2:
                self.LIST.append(f'{self.n} 2')
            else:
                for i in range(self.black+1,(self.black+self.black)+1):
                    self.LIST.append(f'{self.n}{i}')
        elif self.qw == 3:
            if self.lot == 1 or self.lot == 2:
                self.LIST.append(f'Белый {self.n} отсутствует')
            else:
                for i in range((self.black+self.black)+1,self.black+self.black+self.black+1):
                    self.LIST.append(f'{self.n}{i}')
       


#k1 = Kostums('Пиджак',int(input('Введите количество пиджаков: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
#k1.method()
#k2 = Kostums('Галстук',int(input('Введите количество галстуков: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
#k2.method()
k1 = All_elem_kostums('Пиджак',int(input('Введите количество пиджаков: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
k2 = All_elem_kostums('Галстук',int(input('Введите количество галстуков: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
k3 = All_elem_kostums('Брюки',int(input('Введите количество брюк: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
k4 = All_elem_kostums('Рубашка',int(input('Введите количество рубашек: ')),int(input("Выберите цвет: 1-черный,2-синий,3-белый ")))
k1.method()
k2.method()
k3.method()
k4.method()


ALL = []
def all():
    ol = []
    for i in k1.LIST:
        for q in k2.LIST:
            for w in k3.LIST:
                for ii in k4.LIST:
                    ol.append(i)
                    ol.append(q)
                    ol.append(w)
                    ol.append(ii)
                    ALL.append(ol)
                    ol = []
all()

def price():
    count = 0
    for i in ALL:
        for j in i:
            if j[-1].isdigit() == True:
                if 1<=int(j[-1])<=3:
                    count += randint(5,15)
                elif 3<=int(j[-1])<=6:
                    count += randint(15,25)
                else:
                    count += randint(25,50)
                
            else:
                count += 0
        i.append(f'Цена костюма {count}$')
        count = 0
        print(*i,end='\n')
price()