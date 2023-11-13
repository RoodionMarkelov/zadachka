from multiprocessing import Pool
import random
import math
import sys

def count_pi(number):
    count_in = 0
    for i in range(0, number):
        x = random.random()
        y = random.random()
        if math.sqrt(pow(x, 2) + pow(y, 2)) < 1:
            count_in += 1
    return 4 * (count_in / number)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('нет параметров')
    else:
        print(
            f'передано {len(sys.argv) - 1} параметров: {sys.argv[1:]}')
    n= len(sys.argv)
    value = []
    for i in range(1, n):
        value.append(int(sys.argv[i]))
    with Pool(10) as p:
        print(p.map(count_pi, value))