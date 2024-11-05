player1=list(input().split())
player2=list(input().split())
player=player1+player2
def Error(player,player1,player2):
    for i in range(len(player1)):
        if player[i][0] not in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            if player[i][0]=='1' and player[i][1]=='0':
                return poker(player1,player2)
            else:
                print('Error input')
                break
        elif player[i][1] not in ['S','H','D','C']:
            print('Error input')
            break
        else:
            if len(player)!=len(set(player)):
                print('Duplicate deal')
                break
            else:
                return poker(player1,player2)

def poker_number(player):
    _poker_=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    Ntemp=[]
    for i in player:
        Ntemp.append(_poker_.index(i[:-1])+1)
    return pokerset(player,Ntemp)

def poker(player1,player2):
    P1=0
    P2=0
    P1=poker_number(player1)
    P2=poker_number(player2)
    print(max(P1,P2))

def pokerset(player,Ntemp):
    four=0
    Three=0
    pair=0
    if len(set(Ntemp))==5:
        return Straight(player,Ntemp)
    else:
        for i in Ntemp:
            if Ntemp.count(i)==2:
                pair+=1
            if Ntemp.count(i)==3:
                Three+=1
            if Ntemp.count(i)==4:
                four+=1
        if four==1:
            return 8
        elif pair==2 and Three==1:
            return 7
        elif Three==1:
            return 4
        elif pair==2:
            return 3
        elif pair==1:
            return 2

def Straight(player,Ntemp):
    num=[]
    Ftemp=[]
    for i in range(len(player)):
        Ftemp.append(player([i][1]))
        num.append(Ntemp[i]-Ntemp[i-1])
    if sorted(list(set(num))) == [1,9] and len(set(Ftemp))==1:
        return 9
    elif sorted(list(set(num))) == [1,9]:
        return 5
    elif len(set(Ftemp))==1:
        return 6
    else:
        return 1

Error(player,player1,player2)