M=input()
temp2=0
asum=0
while M!="-1":
    asum=int(M,2)
    for _ in range(8):
        if asum==1 or asum==0:
            break
        elif asum%2==0:
                asum=asum//2
                temp2+=1
        else:
            asum=(asum+1)//2
            temp2+=1
    print(bin(temp2)[2:].zfill(4))
    asum=0
    temp2=0
    M=input()
    