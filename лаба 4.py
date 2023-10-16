import random
import numpy as np
import matplotlib.pyplot as plt 
n,k = int(input('Введите число n: ')) , int(input('Введите число k: '))
matrix = np.array([[0]*n]*n)

for i in range(n):
    for j in range(n):
        matrix[i][j] = random.randint(-10,10)

print(*matrix,sep = '\n')
print()
if n%2 == 0:
    BC = matrix[:n//2]
    

    B = []
    for ii in BC:
        B.append(ii[:n//2])

    
    C = []
    for i1 in BC:
        C.append(i1[(n//2):])
    
    DE =  matrix[n//2:]
    
    D = []
    E = []
    for i3 in DE:
        D.append(i3[:n//2])
    
    for i4 in DE:
        E.append(i4[n//2:])
    
else:
    BC = matrix[:(n//2)+1]
    

    B = []
    for ii in BC:
        B.append(ii[:(n//2)+1])

    
    C = []
    for i1 in BC:
        C.append(i1[(n//2):])
    
    DE =  matrix[n//2:]
    
    D = []
    E = []
    for i3 in DE:
        D.append(i3[:(n//2)+1])
    
    for i4 in DE:
        E.append(i4[n//2:])
    
total_per_E = []
for i6 in E[0][1:-1]:
    total_per_E.append(i6)
for i7 in E[-1][1:-1]:
    total_per_E.append(i7)
for i5 in E:
    total_per_E.append(i5[0])
    total_per_E.append(i5[-1])

count_zero = total_per_E.count('0')

if sum(total_per_E) > count_zero:
    if n%2 != 0:
        C_1 = []
        for i8 in C:
            C_1.append(i8[1:])
        B_fl = np.flip(B,1)
        C_fl = np.flip(C_1,1)
        F1 = np.hstack([C_fl,B_fl])
        F = np.vstack([F1,DE])
    else:
        B_fl = np.flip(B,1)
        C_fl = np.flip(C,1)
        F1 = np.hstack([C_fl,B_fl])
        F = np.vstack([F1,DE])
    
else:
    if n%2 != 0:
        C_1 = []
        for ii in C:
            C_1.append(ii[1:])
        E_C = np.hstack([E,C_1])
        B_1 = []
        for ii1 in B:
            B_1.append(ii1[:-1])
        D_B = np.hstack([D,B_1])
        F = np.vstack([E_C,D_B])
    else:
        E_C = np.hstack([E,C])
        B_1 = []
        
        D_B = np.hstack([D,B])
        F = np.vstack([E_C,D_B])

pob = np.fliplr(F).diagonal(0)
main = F.diagonal(0)
if n%2 != 0:
    main = np.delete(main,n//2)
    diagg = np.hstack([main,pob])
else:
    diagg = np.hstack([main,pob])

matrix_T = np.transpose(matrix)
print(matrix)
plt.plot(matrix)
plt.show()

print()
print(F)
print()
plt.plot(F)
plt.show()
if np.linalg.det(matrix) > sum(diagg):
    M_MT = np.dot(matrix,matrix_T)
    print(M_MT)
    print()
    kF = np.dot(k,F) 
    res = M_MT-kF
    print(res)
    print()
    plt.plot(res)
    plt.show()
else:
    obr_mat = np.linalg.inv(matrix)
    obr_F = np.linalg.inv(F)
    G = np.tril(matrix)
    GF = G-obr_F
    print(GF)
    print()
    Q = obr_mat +GF
    print(Q)
    print()
    res = np.dot(k,Q)
    print(res)
    plt.plot(res)
    plt.show()
