def M():
    temp=0
    temp2=0
    N=['5','8','1','2']
    M=list(input())
    for i in range(4):
        if N[i]==M[i]:
            temp+=1
        elif N[i] in M:
            temp2+=1
    return temp,temp2
while True:
    temp,temp2=M()
    print(temp,'A',temp2,'B')
    if temp==4:
        break