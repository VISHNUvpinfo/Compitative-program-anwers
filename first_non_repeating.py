def fi(my_string):
  for c in my_string:
    if my_string.index(c) == my_string.rindex(c):
      return c
  return "-1"
s="zxvczbtxyzvy"
print(fi(s))