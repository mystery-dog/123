all=[]
D=input()
N=list(input().split())
A=input().split(D)
for i in range(1,len(A)):
    for j in range(len(N)):
        if N[j] in A[i]:
            all.append(A[i][:-3])
all=sorted(all,key=lambda x:(len(x),x))
if all!=[]:
    for i in all:
        print(i)
else:
    print('No gene')