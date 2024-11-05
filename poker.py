player1=list(input().split())
player2=list(input().split())
player=player1+player2
def Error(player):
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

def poker(player1,player2):
    P1=pokerset(player1)
    P2=pokerset(player2)

def pokerset(player)
    Ntemp=[]
    Ftemp=[]
    for i in range(len(player)):
        Ntemp.append(player([i][0]))
        Ftemp.append(player([i][1]))
        if len(set(Ntemp))==5:
            if len(set(Ftemp))==1:
                return Straight_flush(player)
            else:
                return Straight(player)
        elif len(set(Ntemp))==4:
            return 1
        elif len(set(Ntemp))==3:
            if Ntemp 
            for i in player:
                if player.count(i)==2:
                    
Ans=Error(player)
print(Ans)