from random import *
class All_elem_kostums:
    def __init__(self,n,lot):
        self.n = n
        self.lot = lot
        self.LIST = []
        
    
    def input_color(self):
        global qw
        qw = int(input('Выберите цвет: 1-черный,2-синий,3-белый '))
        if qw > 3 or qw == 0:
            print('Вы ввели неккоректную цифру,попробуйте еще раз!')
            self.input_color()

    def method(self):
        if self.lot == 0:
            return self.LIST.append(f'{self.n} нет')
        self.input_color() 
        self.black = self.lot //3 
        self.blue = (self.lot - self.black)//2 #2
        self.white = (self.lot - self.black)-self.blue
        if qw == 1:
            if self.lot == 1 or self.lot == 2:
                self.LIST.append(f"{self.n}1  ")
            else:
                for i in range(1,self.black+1):
                    self.LIST.append(f'{self.n}{i}  ')
                    
        elif qw == 2:
            if self.lot == 1:
                self.LIST.append(f'{self.n}1   ')
            if self.lot == 2:
                self.LIST.append(f'{self.n}2   ')
            else:
                for i in range(self.black+1,(self.black+self.black)+1):
                    self.LIST.append(f'{self.n}{i}   ')
        elif qw == 3:
            if self.lot == 1 or self.lot == 2:
                self.LIST.append(f'{self.n}1   ')
            else:
                for i in range((self.black+self.black)+1,self.black+self.black+self.black+1):
                    self.LIST.append(f'{self.n}{i}   ')
        
       
        


k1 = All_elem_kostums('Пиджак',int(input('Введите количество пиджаков: ')))
k1.method()

k2 = All_elem_kostums('Галстук',int(input('Введите количество галстуков: ')))
k2.method()

k3 = All_elem_kostums('Брюки',int(input('Введите количество брюк: ')))
k3.method()

k4 = All_elem_kostums('Рубашка',int(input('Введите количество рубашек: ')))
k4.method()


fasons1 = ['Классический ','Спортивный ','Френч ','Блейзер ','Смокинг ']
if len(k1.LIST) > 1 or (len(k1.LIST) == 1 and k1.LIST[0].rstrip()[-1].isdigit() == True):
    for i in range(len(k1.LIST)):
        k1.LIST[i] = choice(fasons1) + k1.LIST[i]
else:
    k1.LIST[0] = 'Пиджаков нет  '

        
fasons2 = ['Бабочка-','Техасский-','Лаварьер-','Регат-','Скинни-', 'Платок-']
knots = ['Бальтус-узел: ','Виктория-узел: ','Восточный узел: ','Двойной узел: ','Диагональный узел: ','Кент-узел: ','крестовый узел: ','Манхэттен-узел: ','Никки-узел: ','Простой узел: ']
if len(k2.LIST) > 1 or (len(k2.LIST) == 1 and k2.LIST[0].rstrip()[-1].isdigit() == True):
    for i in range(len(k2.LIST)):
        k2.LIST[i] = choice(fasons2) + k2.LIST[i]
    for i in range(len(k2.LIST)):
        k2.LIST[i] = choice(knots) + k2.LIST[i]
else:
    k2.LIST[0] = 'Галстуков нет  '
fasons3 = ['Классические ','Чинос ','Карго ','Джоггеры ','Бананы ','Скинни ']
if len(k3.LIST) > 1 or (len(k3.LIST) == 1 and k3.LIST[0].rstrip()[-1].isdigit() == True):
    for i in range(len(k3.LIST)):
        k3.LIST[i] = choice(fasons3) + k3.LIST[i]
else:
    k3.LIST[0] = 'Брюк нет  '
fasons4 = ['Свободного фасона ','Классического фасона ','Приталенного фасона ','Современного фасона ']
if len(k4.LIST) > 1 or (len(k4.LIST) == 1 and k4.LIST[0].rstrip()[-1].isdigit() == True):
    for i in range(len(k4.LIST)):
        k4.LIST[i] = choice(fasons4) + k4.LIST[i]
else:
    k4.LIST[0] = 'Рубашек нет  '
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
            if j.rstrip()[-1].isdigit() == True:
                if 1<=int(j.rstrip()[-1])<=3:
                    count += randint(5,15)
                elif 3<=int(j.rstrip()[-1])<=6:
                    count += randint(15,25)
                else:
                    count += randint(25,50)
                
            else:
                count += 0
        i.append(f'Цена костюма {count}$')
        count = 0
        print(*i,end='\n')
price()
