from FibonacciHeap import FibHeap
from PriorityQueue import FibPQ, HeapPQ, QueuePQ

def solve(maze):
    width = maze.width               # Used for indexing
    total = maze.width * maze.height # Array sizes

    start = maze.start               # Start node
    startPos = start.Position
    end = maze.end                   # End node
    endPos = end.Position

    visited = [False] * total        # True/False wether a node has already been visited

    prev = [None] * total            # Holds a link to the previous node in the path (used for path construction)

    infinity = float("inf")          # Holds the max value of a float.
    distances = [infinity] * total   # Default value of every node in the graph is infinity

    # unvisited = FibHeap()            # We chose the Fibonnaci Heap for Dijkstra

    # Can also be one of the following priority queue
    # unvisited = FibPQ()
    unvisited = HeapPQ()
    # unvisited = QueuePQ()

    nodeIndex = [None] * total      # Holds all priority queue nodes

    distances[start.Position[0] * width + start.Position[1]] = 0 # Position[0] holds Y and Position[1] holds X
    startNode = FibHeap.Node(0, start)
    nodeIndex[start.Position[0] * width + start.Position[1]] = startNode
    unvisited.insert(startNode)

    count = 0         # Zero nodes visited
    completed = False # Not completed yet

    while len(unvisited) > 0:
        count+=1

        n = unvisited.removeMinimum()

        current = n.value
        curPos = current.Position
        curPosIndex = curPos[0] * width + curPos[1]

        if distances[curPosIndex] == infinity:
            break

        if curPos == endPos:
            completed = True
            break


        for v in current.Neighbours:
            if v != None:
                vPos = v.Position
                vPosIndex = vPos[0] * width + vPos[1]

                if visited[vPosIndex] == False:
                    manDist = abs(vPos[0] - curPos[0]) + abs(vPos[1] - curPos[1])

                    newDistance = distances[curPosIndex] + manDist

                    if newDistance < distances[vPosIndex]:
                        vNode = nodeIndex[vPosIndex]

                        if vNode == None:
                            vNode = FibHeap.Node(newDistance, v)
                            unvisited.insert(vNode)
                            nodeIndex[vPosIndex] = vNode
                            distances[vPosIndex] = newDistance
                            prev[vPosIndex] = current

                        else:
                            unvisited.decreaseKey(vNode, newDistance)
                            distances[vPosIndex] = newDistance
                            prev[vPosIndex] = current

        visited[curPosIndex] = True

    from collections import deque

    path = deque()
    current = end
    while current != None:
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
