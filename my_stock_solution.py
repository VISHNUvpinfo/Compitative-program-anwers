def out(b,s):
    if b == s:
        pass
    else:
        t ="({} {})".format(b,s)
        print(t,end=" ")
n= int(input())
for i in range(1,n+1):
    d = input()
    pr = list(map(int,input().split()))
    b = pr.index(min(pr[0],pr[1]))
    s=0
    p =pr[1:]
    pp =iter(p) 
    if min(pr[0],pr[1])>=max(p):
        print("No Profit")
    else:
        ne = 0
        for index, obj in enumerate(p):
            if index < (len(p) - 1):
                ne = p[index + 1]
                if obj>ne :
                        s = index+1
                        out(b,s)
                        b=s+1
            else:
                s=len(p)
                out(b,s)
    print()
                
            