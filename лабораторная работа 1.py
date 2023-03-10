#Шеснадцатиричные нечетные числа, не превышающие 409610 и содержащие более К цифр. Вывести числа и их количество. Минимальное число вывести прописью.
slovar = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять','A':'десять','B':'одиннадцать','C':'двенадцать','D':'тринадцать','E':'четырнадцать','F':'пятнадцать','a':'десять','b':'одиннадцать','c':'двенадцать','d':'тринадцать','e':'четырнадцать','f':'пятнадцать'}
a=[]
b=[]
dig_10 = []
buffer_len = 1
work = ''
with open('text.txt' , 'r') as file:
    buffer = file.read(buffer_len)

    while buffer:
            work += buffer
            buffer = file.read(buffer_len)

a = work.split()
for i in a:
    for g in i:
        if g.isdigit() == False:
            if g not in 'abcdefABCDEF':
                i = i.replace(g, ' ')
    b.append(i)



w = ' '.join(b)

b = w.split()

b_itog = []
k = int(input('Введите  колво цифр : '))
count = 0
for i1 in b:
    for g1 in i1:
        if g1.isdigit():
            count += 1
    if count > k and int(i1,16) < 4096 and int(i1,16)%2 !=0:
        b_itog.append(i1)
    count = 0

d_max = 5000
for i2 in b_itog:
    if int(i2,16) < d_max:
        d_max = int(i2,16)
        d__max = i2

for i3 in b_itog:
    print(i3,end='\n')
print()
print(f'Минимальное число:{d__max}')
for ii in d__max:
    print(slovar[ii])
