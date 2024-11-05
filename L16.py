def Error(l,K,p):
    Z=0
    z=0
    for y in range(len(K)):
        if K[y] not in '23456789AJKQT' or p[y] not in 'CDHS':
            Z+=1
        else:
            for x in range(y+1,len(l)):
                if l[y]==l[x]:
                    z+=1
    if Z>0:
        return 1
    elif z>0:
        return -1

def card(l,k,p,N,F):
    if len(N)==5 and len(F)==1:
        Straight_flush(N,F)
    elif len(N)==2 and len(F)==4:
        Three_of_a_kind(sorted(k),sorted(p))
    elif len(N)==2:
        Three_of_a_kind(sorted(k),sorted(p))
    elif len(N)==5:
        Straight(N,F)
    elif len(N)==3:
        Three_of_a_kind(sorted(k),sorted(p))
    else:
        print('2')

def Straight1(N:list,F:list):
    n=0
    if N==[2,11,12,13,14] or N==[2,3,12,13,14] or N==[2,3,4,13,14] or N==[2,3,4,5,14]:
        return 4
    else:
        for i in range(1,len(N)):
            if int(N[i-1])+1==int(N[i]):
                n+=1
            else:
                n=0
        return n

def Straight_flush(N:list,F:list):
    n=Straight1(N,F)
    if n==4:
        print('9')
    else:
        print('6')

def Straight(N:list,F:list):
    n=Straight1(N,F)
    if n==4:
        print('5')
    else:
        print('1')
    
def Three_of_a_kind(k:list,p:list):
    o=[]
    O=[]
    for i in range(len(k)):
        if k[i] in o:
            O.append(k[i])
        else:
            o.append(k[i])
    O=list(set(O))
    o=list(set(o))
    if len(O)==1 and len(o)==2:
        print('8')
    elif len(O)==2 and len(o)==2:
        print('7')
    elif len(O)==1:
        print('4')
    else:
        print('3')

l=[]
K=[]
k=[]
p=[]
N=[]
F=[]
l=(input()).split()
b=True
for i in range(len(l)):
    m=l[i]
    if len(m)==3:
        if m[0]=='1' and m[1]=='0':
            m='T'+m[2]
        else:
            print('Error input')
            b=False
            break
    K.append(m[0])
    k.append(m[0])
    p.append(m[1])
        
    for q in range(len(k)):
        if k[q] == 'J':
            k[q]='11'
        elif k[q] == 'Q':
            k[q]='12'
        elif k[q] == 'K':
            k[q]='13'
        elif k[q] == 'T':
            k[q]='10'
        elif k[q] == 'A':
            k[q]='14'
            
    N=sorted(list(set(int(I) for I in k)))
    F=sorted(list(set(p)))

if b:
    if Error(l,K,p)==1:
        print('Error input')
    elif Error(l,K,p)==-1:
        print('Duplicate deal')
    else:
        card(l,k,p,N,F)