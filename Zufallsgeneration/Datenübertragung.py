import random
import math
from numpy import normal

# alles in ms als Einheit
takt = 20
ankunftsdaten = normal(loc = 20, scale= 7, size= 200)

numb_exp = 1000000
hit = 0

r1 = random.unirform(-1, 7) * 8

for l in range(1, numb_exp):
    l1 = 20 - Abw + (2 * Abw) * random.uniform(0, 1)
    l2 = 20 - Abw + (2 * Abw) * random.uniform(0, 1)
    l3 = 20 - Abw + (2 * Abw) * random.uniform(0, 1)

    sum = l1 + l2 + l3

    if(abs(sum - 6) > tlz):
        hit += 1
    
print(float(hit/numb_exp))
