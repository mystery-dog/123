def Print(i,a,y,temp,allsum,c):
    if i+1<=c:
        print(i+1,a,y,0)
    else:
        print(i+1,a,y,temp[i-c])

def M(n,y,allsum,c,d):
    a=0
    stop=n*(1-d)
    for i in range(m):
        allsum+=int(y)
        temp.append(int(y))
        if allsum<int(stop):
            if i+1<=c:
                a=a+int(y)
                if a>=stop:
                    d=1
            else:
                a=a+int(y)-temp[i-c]
                d=d+temp[i-c]/n
                if d>1 or a>=stop:
                    d=1
        else:
            if a+int(y)>=int(stop):
                y=int(stop)-a
                a=int(stop)
            if i+1>c:
                a-=temp[i-c]
            d=1
        Print(i,a,int(y),temp,allsum,c)
        x=(b/c)*(1-d)
        y=a*x
        if a+int(y)>=int(stop):
                y=int(stop)-a
    print(int(allsum))

n=int(input())
m=int(input())
a=int(input())
b=float(input())
c=int(input())
d=float(input())
allsum=0
temp=[]
x=0
y=a
M(n,y,allsum,c,d)
