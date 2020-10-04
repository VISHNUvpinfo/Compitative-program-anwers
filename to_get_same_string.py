from collections import *    
a = Counter('fcrxzwscanmligyxyvym')
b = Counter('jxwtrhvujlmrpdoqbisbwhmgpmeoke')
c = a - b
d = b - a
e = c + d
print(len(list(e.elements())))