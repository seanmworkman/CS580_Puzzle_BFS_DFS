#!/usr/bin/env python3
from Queue import Queue
from Stack import Stack
from copy import deepcopy
import time
import sys
import random

rows = 5
columns = 5
goal = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 0]
]
# initial = [
#     [9, 24, 3, 5, 17],
#     [6, 0, 13, 19, 10],
#     [11, 21, 12, 1, 20],
#     [16, 4, 14, 12, 15],
#     [8, 18, 23, 2, 7]
# ]
# rows = 3
# columns = 3
# goal = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]

initial = []

# initial = [
#     [2, 1, 4],
#     [0, 6, 8],
#     [3, 5, 7]
# ]

quiet = False

# Helper function to determine if the current state matches the goal state
def goalTest(state):
    failCount = 0
    for i in range(rows):
        for j in range(columns):
            if state[i][j] != goal[i][j]:
                failCount += 1
    
    if failCount > 0:
        return False
    else:
        return True

# Helper function to get coordinates of empty space
def getEmptySpace(state):
    emptySpace = ()
    for i in range(rows):
        for j in range(columns):
            if state[i][j] == 0:
                emptySpace = (i, j)
                break
    return emptySpace

# Helper function to gather coordinates of neighbors of empty space
def getNeighbors(state):
    neighbors = []
    emptySpace = getEmptySpace(state)

    # Neighbor below
    if emptySpace[0] + 1 < rows:
        neighbors.append((emptySpace[0] + 1, emptySpace[1]))

    # Neighbor left
    if emptySpace[1] - 1 >= 0:
        neighbors.append((emptySpace[0], emptySpace[1] - 1))

    # Neighbor right
    if emptySpace[1] + 1 < columns:
        neighbors.append((emptySpace[0], emptySpace[1] + 1))

    # Neighbor above
    if emptySpace[0] - 1 >= 0:
        neighbors.append((emptySpace[0] - 1, emptySpace[1]))
    
    # print(neighbors)
    return neighbors

# Helper function to build options based on neighbors
def buildOptions(state):
    neighbors = getNeighbors(state)
    emptySpace = getEmptySpace(state)
    # print(emptySpace)
    options = []
    for i in neighbors:
        tempState = []
        tempState = deepcopy(state)
        tempElement = tempState[i[0]][i[1]]
        # print(i)
        tempState[emptySpace[0]][emptySpace[1]] = tempElement
        tempState[i[0]][i[1]] = 0
        options.append(tempState)
        # print(state)
    return options

# Helper funciton to determine if two states are the same
def areEqualStates(a, b):
    failCount = 0
    for i in range(rows):
        for j in range(columns):
            if a[i][j] != b[i][j]:
                failCount += 1
                break

    if failCount > 0:
        return False
    else:
        return True

# Helper function to determine if subject is in the queue
def isInQueue(q, subject):
    tempQ = Queue()
    tempQ = q
    while q.size() > 0:
        a = tempQ.removefromq()
        if areEqualStates(a, subject):
            return True
    return False

# Helper function to check is a neighbor is in a list 
def neighborInExplored(neighbor, explored):
    failCount = 0
    matches = False
    for exploredList in explored:
        for i in range(rows):
            for j in range(columns):
                if exploredList[i][j] != neighbor[i][j]:
                    failCount += 1
        
        if failCount == 0:
            matches = True
            break
    return matches

# Helper funciton to print the state in a readable order
def printState(state):
    print('------------')
    for i in state:
        print(i)
    print('------------')

# Helper function to generate initial state
def generateInitial():
    values = random.sample(range(0, (rows * columns)), (rows * columns))
    valuesIndex = 0
    result = []
    for i in range(rows):
        list1 = []
        for j in range(columns):
            list1.append(values[valuesIndex])
            valuesIndex += 1
        result.append(list1)
    return result


# Breadth First Search
# Queue: FIFO
def bfs(initial):
    # Create frontier queue
    frontier = Queue()
    explored = []
    frontierList = []

    # Add initial state to frontier
    frontier.addtoq(initial)
    frontierList.append(initial)

    # Go through the queue until it is empty
    while frontier.size() > 0:
        # Pop the element from the queue
        state = frontier.removefromq()

        # Add it to explored
        explored.append(state)

        if not quiet:
            printState(state)

        # Check if the current state is the goal state
        if goalTest(state):
            return "Success"

        # Get options from current state and neighbors
        options = buildOptions(state)

        for neighbor in options:
            tempFrontier = Queue()
            tempFrontier = deepcopy(frontier)
            if not neighborInExplored(neighbor, explored) and not neighborInExplored(neighbor, frontierList):
            # if neighbor not in explored:
                frontier.addtoq(neighbor)
                frontierList.append(neighbor)       
    return False

# Depth First Search
# Stack: LIFO
def dfs(initial):
    # Create frontier stack
    frontier = Stack()
    explored = []
    frontierList = []
    # Add initial state to frontier
    frontier.add(initial)
    frontierList.append(initial)
    # Go through the stack until it is empty 
    while frontier.size() > 0:
        # Pop the element from the stack
        state = frontier.remove()

        # Add it to explored
        explored.append(state)

        printState(state)

        # Check if the current state is the goal state
        if goalTest(state):
            return "Success"

        # Get options from current state and neighbors
        options = buildOptions(state)
        
        for neighbor in options:
            if not neighborInExplored(neighbor, explored) and not neighborInExplored(neighbor, frontierList):
                # print("ADDED TO STACK")
                frontier.add(neighbor)
                frontierList.append(neighbor)
    return False

def runSearch(mode):
    if mode.lower() == "bfs":
        start_time = time.time()
        print(bfs(initial))
        elapsed_time = time.time() - start_time
        print('Breadth First Search finished in {}'.format(elapsed_time))
    else:
        start_time = time.time()
        print(dfs(initial))
        elapsed_time = time.time() - start_time
        print('Depth First Search finished in {}'.format(elapsed_time))

initial = generateInitial()
quiet = False
if len(sys.argv) >= 3:
    if sys.argv[2] == "--quiet":
        quiet = True
runSearch(sys.argv[1])