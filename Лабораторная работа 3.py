#27.Формируется матрица F следующим образом: если в Е сумма чисел по периметру области 1 больше,чем количество нулей по периметру области 4, то поменять в С симметрично области 1 и 3 местами, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:((К*AT)*А)-K*FT . Выводятся по мере формирования А, F и все матричные операции последовательно.
import random
n,k = int(input('Введите число n: ')) , int(input('Введите число k: '))
matrix = [[0]*n for _ in range (n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = random.randint(-10,10)
#Создали исходную матрицу
if n%2 != 0:
    B = []
    for i2 in matrix:
        B.append(i2[:(n//2)+1])
    print()
    B1 = B[:(n//2)+1] # подматрица В
    D1 = B[(n//2):] # подматрица  D
    C= []
    for i3 in matrix:
        C.append(i3[(n//2):])
    C1 = C[:(n//2)+1] # подматрица C
    E1 = C[(n//2):] # подматрица E
    s1_main = []
    s2_pob = []
    s3_osn = []
    for i5 in range((n//2)+1):
        for j5 in range((n//2)+1):
            if i5 == j5:
                s1_main.append(E1[i5][j5])
    z = n//2 #4
    s1 = s1_main[:(z-1)] #первая сторона области 1
    for i6 in range((n//2)+1):
        s2_pob.append(E1[i6][(z+1) - i6 - 1])
    s2 = s2_pob[(z-1):] #вторая сторона области 1
    for i7 in E1:
        s3_osn.append(i7[0])
    s3 = s3_osn[1:-1] #третья сторона области 1
    total_E_1 = sum(s1)+sum(s2)+sum(s3)#Сумма чисел периметра стороны 1
    s4 = s2_pob[(z-2):]
    s5 = s1_main[(z-1):]
    s6 = E1[z][1:-1]
    s456 = s4+s5+s6
    count = 0
    for g in s456:
        if g == 0:
            count += 1
    if total_E_1 > count:
        for ii in range(z+1):
            for jj in range(z+1):
                if ii >= jj and ii <= (z+1)-jj-1:
                    x = C1[ii][(z+1)-jj-1]
                    C1[ii][(z+1)-jj-1] = C1[ii][jj]
                    C1[ii][jj] = x
        BC = []
        for i9 in range(z+1):
            B1[i9] = B1[i9][:-1]+C1[i9]
        print()
        for i99 in range(z+1):
            D1[i99] = D1[i99][:-1]+E1[i99]
        F = B1+D1[1:]
        print('Матрица А:')
        for i1 in matrix:
            print(i1,end='\n')
        print()
        print('Матрица F:')
        for iii3 in F:
            print(iii3,end='\n')
    else:
        for i12 in range(z+1):
            E1[i12] = E1[i12]+C1[i12][1:]
        for i13 in range(z+1):
            D1[i13] = D1[i13]+B1[i13][:-1]
        F = E1+D1[1:]
        print('Матрица А:')
        for i14 in matrix:
            print(i14,end='\n')
        print()
        print('Матрица F:')
        for iii6 in F:
            print(iii6,end='\n')

else:
    BD = []
    CE = []
    for i1 in matrix:
        BD.append(i1[:n // 2])

    for i2 in matrix:
        CE.append(i2[n // 2:])

    B = BD[:n // 2]
    D = BD[n // 2:]
    C = CE[:n // 2]
    E = CE[n // 2:]

    main = []
    pob = []
    for i3 in range((n // 2)):
        for j3 in range((n // 2)):
            if i3 == j3:
                main.append(E[i3][j3])

    for i4 in range((n // 2)):
        pob.append(E[i4][(n // 2) - i4 - 1])
    st1 = []
    st1_3 = []
    st1_1 = main[:((n // 2) // 2) + 1]

    st1_2 = pob[(((n // 2) // 2) + 1):]

    for i5 in E:
        st1_3.append(i5[0])
    st1_3 = st1_3[1:-1]

    st1 = st1_1 + st1_2 + st1_3  # oblast 1 v E

    st4 = []
    st4_1 = pob[((n // 2) // 2):]
    st4_2 = main[((n // 2) // 2) + 1:]
    st4_3 = E[-1][1:-1]

    st4 = st4_1 + st4_2 + st4_3
    summ = sum(st1)
    count = 0
    for i6 in st4:
        if i6 == 0:
            count += 1
    z = n // 2
    if summ > count:
        for ii in range(z):
            for jj in range(z):
                if ii >= jj and ii <= (z) - jj - 1:
                    x = C[ii][(z) - jj - 1]
                    C[ii][(z) - jj - 1] = C[ii][jj]
                    C[ii][jj] = x

        for i7 in range(z):
            B[i7] = B[i7] + C[i7]
        for i8 in range(z):
            D[i8] = D[i8] + E[i8]

        F = B + D
        print('Матрица А:')
        for ii1 in matrix:
            print(ii1,end='\n')
        print()
        print('Матрица F:')
        for iii3 in F:
            print(iii3, end='\n')
    else:
        for i9 in range(z):
            E[i9] = E[i9] + C[i9]
        for i10 in range(z):
            D[i10] = D[i10] + B[i10]
        F = E + D
        print('Матрица А:')
        for i14 in matrix:
            print(i14,end='\n')
        print()
        print('Матрица F:')
        for iii6 in F:
            print(iii6, end='\n')

A_T = [[0 for z in range(n)] for zz in range(n)]
for l in range(n):
    for ll in range(n):
        A_T[ll][l] = matrix[l][ll]
F_T = [[0 for v in range(n)] for vv in range(n)]
for l1 in range(n):
    for ll1 in range(n):
        F_T[ll1][l1] = F[l1][ll1]
for i_ in range(n):
    for j_ in range(n):
        A_T[i_][j_] = A_T[i_][j_]*k
print()
print('Матрица А транспонированная умноженная на k:')
for u in A_T:
    print(u,end='\n')
print()
AxA = [[0 for z1 in range(n)] for zz1 in range(n)]
for i15 in range(n):
    for j15 in range(n):
        for p15 in range(n):
            AxA[i15][j15] += (A_T[i15][p15]*matrix[p15][j15])
print('Матрица А транспонированная умноженная на k умноженная на исходную матрицу A:')
for qq in AxA:
    print(qq,end='\n')
KxFT = [[0 for v1 in range(n)] for vv1 in range(n)]
for i__ in range(n):
    for j__ in range(n):
        KxFT[i__][j__] = A_T[i__][j__]*k
print()
print('Матрица F транспонированная умноженная на k:')
for w in KxFT:
    print(w,end='\n')
result_matrix = [[0 for z3 in range(n)] for zz3 in range(n)]
for e in range(n):
    for ee in range(n):
        result_matrix[e][ee] = AxA[e][ee]-KxFT[e][ee]
print()
print('Конечное выражение :((К*AT)*А)-K*FT):')
for __ in result_matrix:
    print(__,end='\n')





















