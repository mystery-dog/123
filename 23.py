poker=['H2','H3','H4','H5','H6','H7','H8','C2','C3','C4','C5','C6','C7','C8','Joker']
Play1=list(input().split())
Play2=list(input().split())
Com=list(input().split())
mistake=0
def clean(Play_1):
    Play=[]
    for i in range(len(Play_1)):
        for j in range(len(Play_1)):
            if poker.index(Play_1[i]) == poker.index(Play_1[j])+7 and 14>poker.index(Play_1[i])>6:
                Play.append(Play_1[i])
                Play.append(Play_1[j])
    for i in range(len(Play)):
        Play_1.remove(Play[i])

def Draw(Play_1,Play_2,mistake):
    temp=input()
    if temp in Play_2 and mistake!=1:
        Play_1.append(temp)
        Play_2.remove(temp)
    else:
        return 1


def Clean(Play1,Play2,Com):
    clean(Play1)
    clean(Play2)
    clean(Com)
    
Clean(Play1,Play2,Com)

mistake=Draw(Play1,Play2,mistake)
Clean(Play1,Play2,Com)

mistake=Draw(Play2,Com,mistake)
Clean(Play1,Play2,Com)

mistake=Draw(Com,Play1,mistake)
Clean(Play1,Play2,Com)

if mistake==None:
    print(" ".join(Play1))
    print(" ".join(Play2))
    print(" ".join(Com))
else:
    print('Error')