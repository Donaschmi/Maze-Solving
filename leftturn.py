from collections import deque

def solve(maze):

    path = deque([maze.start])

    current = maze.start.Neighbours[2]

    if current == None:
        return path

    heading = 2

    turn = 1

    startpos = maze.start.Position
    endpos = maze.end.Position

    count = 1

    completed = False

    while True:
        path.append(current)
        count+=1
        position = current.Position
        if position == startpos or position == endpos:
            if position == endpos:
                completed = True
            break

        n = current.Neighbours

        if n[(heading - turn) % 4] != None:
            heading = (heading - turn) % 4
            current = n[heading]
            continue

        if n[heading] != None:
            current = n[heading]
            continue

        if n[(heading + turn) % 4] != None:
            heading = (heading + turn) % 4
            current = n[heading]
            continue

        if n[(heading + 2) % 4] != None:
            heading = (heading + 2) %4
            current = n[heading]
            continue

        completed = False
        break

    return [path, [count, len(path), completed]]
