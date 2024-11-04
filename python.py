import numpy as np

def A(N,D,l):
    for i in range(1,N*N+1):
        l.append(i)
    matrix=np.reshape(l,(N,N))
    MD(matrix,D)
    
def MD(matrix,D):
    if D==1:
        matrix_1=np.rot90(matrix,1)
        M(matrix_1)
    elif D==2:
        matrix_2=np.rot90(matrix,-1)
        M(matrix_2)
    elif D==3:
        matrix_3=np.flipud(matrix)
        M(matrix_3)
    elif D==4:
        matrix_4=np.fliplr(matrix)
        M(matrix_4)
    
def M(matrix):
    for i in matrix:
        print(''.join(f"{num:3d}"for num in i))

def main():
    N=int(input())
    D=int(input())
    l=[]
    A(N,D,l)
main()