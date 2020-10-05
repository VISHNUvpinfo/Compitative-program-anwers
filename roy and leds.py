def get_time(T,v):
    temp = [0]*T
    for i in range (v,T,v+v):
        for j in range(v):
            if i+j >= T:
                break
            else:
                temp[i+j]=1
    return temp
T,R,G,B = list(map(int,input().split()))
r_set =get_time(T,R)
g_set =get_time(T,G)
b_set =get_time(T,B)
r,g,b,ye,cy,ma,wh,ba =0,0,0,0,0,0,0,0
for i in range (T):
    if   r_set[i]==1 and g_set[i]==1 and b_set[i]==1:
        wh = wh+1
        continue
    elif r_set[i]==0 and g_set[i]==0 and b_set[i]==0:
        ba = ba+1
        continue
    elif r_set[i]==0 and g_set[i]==0 and b_set[i]==1:
        b = b+1
        continue
    elif r_set[i]==0 and g_set[i]==1 and b_set[i]==0:
        g=g+1
        continue
    elif r_set[i]==1 and g_set[i]==0 and b_set[i]==0:
        r=r+1
        continue
    elif r_set[i]==1 and g_set[i]==1 and b_set[i]==0:
        ye=ye+1
        continue
    elif r_set[i]==0 and g_set[i]==1 and b_set[i]==1:
        cy=cy+1
        continue
    elif r_set[i]==1 and g_set[i]==0 and b_set[i]==1:
        ma=ma+1
        continue
result ="{} {} {} {} {} {} {} {}".format(r,g,b,ye,cy,ma,wh,ba)
print(result)