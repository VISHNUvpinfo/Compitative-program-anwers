from collections import deque
# Complete the rotLeft function below.
def rotLeft(a, d):
    a = deque(a)
    a.rotate(-d)
    a = list(a)
    return a
a = "41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51"
d = 10
a= list(map(str,a.strip(" ")))
result = rotLeft(a, d)
print(result)
