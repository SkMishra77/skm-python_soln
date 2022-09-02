try:
    a=int(input())
    b=int(input())
    if ((str(type(a))[8:-2])==(str(type(b))[8:-2])):
        print(a+b)
except:
    print("NOT AN INTEGER")
