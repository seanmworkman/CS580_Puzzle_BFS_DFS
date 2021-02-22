import time
import sys
import random
rows = 3
columns = 3
initial = [
    [9, 24, 3, 5, 17],
    [6, 0, 13, 19, 10],
    [11, 21, 12, 1, 20],
    [16, 4, 14, 12, 15],
    [8, 18, 23, 2, 7]
]
quiet = False
def printState(state):
    print('------------')
    for i in state:
        print(i)
    print('------------')

def generateInitial():
    values = random.sample(range(0, (rows * columns)), (rows * columns))
    valuesIndex = 0
    result = []
    print(initial)
    for i in range(rows):
        list1 = []
        for j in range(columns):
            list1.append(values[valuesIndex])
            valuesIndex += 1
        result.append(list1)
        if not quiet:
            print(list1)
    return result

start_time = time.time()
initial = generateInitial()
printState(initial)
print(sys.argv[1])
quiet = False
if len(sys.argv) >= 3:
    if sys.argv[2] == "--quiet":
        quiet = True
print(quiet)
elapsed_time = time.time() - start_time
print('Breadth First Search finished in {}'.format(elapsed_time))
