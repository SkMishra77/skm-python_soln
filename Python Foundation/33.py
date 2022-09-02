a,b,c=list(map(int,input().split()))
if(a==b or b==c or c==a):
    print(0)
else:
    print(a+b+c)