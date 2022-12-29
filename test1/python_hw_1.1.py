#python course homework file 1.1
import math

for i in (4,9,16,25,36,49,64,81,100,121,144,169,256):
    result = i +2*math.sqrt(i) + 1
    print(f'n = {i} :: result = {result}')
    