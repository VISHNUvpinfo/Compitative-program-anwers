n = int(input())
for i in range(n):
    list_values = list(map(int,input().split()))
    N = list_values[0]
    M = list_values[1]
    A = list_values[2]
    B = list_values[3]
    C = list_values[4]
    max_value_a = ((N*A) + (M*B))
    if(N>M):
        max_value_b = 2*M*C+(N-M)*A
    else:
        max_value_b = 2*N*C +(M-N)*B
    print(max(max_value_a,max_value_b))