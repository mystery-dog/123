n=list(input())
N=int(input())
a=b=0
def main():
    for i in range(len(n)):
        for j in range(i,len(n)):
            if int(n[i])+int(n[j])==N:
                return n[i],n[j]
a,b=main()
print(a,b)