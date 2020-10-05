n = int(input(""))
for i in range (n):
    no_of_friends = int(input(""))
    friends = list(map(int,input().split()))
    minimum_condition = sum(friends)-no_of_friends+1
    print(minimum_condition)
