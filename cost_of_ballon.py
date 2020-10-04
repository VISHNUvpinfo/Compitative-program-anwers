n = int(input(""))
for i in range(n):
    cost = list(map(int,input().split()))
    low_price = min(cost)
    high_price = max(cost)
    m = int(input())
    green =[]
    purple =[]
    for i in range (m):
        temp = list(map(int,input().split()))
        g = temp[0]
        p = temp[1]
        green.append(g)
        purple.append(p)
    if sum(green) <= sum(purple):
        total = ((sum(green)*high_price) + (sum(purple)*low_price))
        print(total)
    else:
        total =((sum(purple)*high_price) + (sum(green)*low_price))
        print(total)
    