import random
import math

tlz = 0.016
Abw = 0.01

numb_exp = 1000000
hit = 0

for l in range(1, numb_exp):
    l1 = 2 - Abw + (2 * Abw) * random.uniform(0, 1)
    l2 = 2 - Abw + (2 * Abw) * random.uniform(0, 1)
    l3 = 2 - Abw + (2 * Abw) * random.uniform(0, 1)

    sum = l1 + l2 + l3

    if(abs(sum - 6) > tlz):
        hit += 1
    
print(float(hit/numb_exp))
