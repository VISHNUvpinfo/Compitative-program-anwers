ashima = input()
gf_ash = list(ashima)
n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    if gf_ash[(a-1)%len(ashima)] == gf_ash[(b-1)%len(ashima)]:
        print("Yes")
    else:
        print("No")