class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]

    def __init__(self, im):
        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(0))

        self.start = None
        self.end = None

        topnodes = [None] * width
        count = 0

        for x in range(1, width - 1):
            # Finding the start Node
            if data[x] > 0:
                self.start = Maze.Node((0, x))
                topnodes[x] = self.start
                count += 1
                break

        for y in range(1, height - 1):

            rowoffset = y * width
            rowaboveoffset = rowoffset - width
            rowbelowoffset = rowoffset + width

            prv = False
            cur = False
            nxt = data[rowoffset + 1] > 0

            leftNode = None
            for x in range(1, width - 1):
                prv = cur
                cur = nxt
                nxt = data[rowoffset + x + 1] > 0

                n = None

                if cur == False:
                    # On Wall - No action
                    continue

                if prv == True:
                    if nxt == True:
                        # PATH PATH PATH
                        if data[rowaboveoffset + x] > 0 or data[rowbelowoffset + x] > 0:
                            n = Maze.Node((y, x))
                            leftNode.Neighbours[1] = n
                            n.Neighbours[3] = leftNode
                            leftNode = n
                    else:
                        #PATH PATH WALL
                        n = Maze.Node((y, x))
                        leftNode.Neighbours[1] = n
                        n.Neighbours[3] = leftNode
                        leftNode = None
                else:
                    if nxt == True:
                        #WALL PATH PATH
                        n = Maze.Node((y, x))
                        leftNode = n
                    else:
                        #WALL PATH WALL
                        if data[rowaboveoffset + x] == 0 or data[rowbelowoffset + x] == 0:
                            n = Maze.Node((y, x))

                if n != None:
                    if data[rowaboveoffset + x] > 0:
                        t = topnodes[x]
                        t.Neighbours[2] = n
                        n.Neighbours[0] = t

                    if data[rowbelowoffset + x] > 0:
                        topnodes[x] = n
                    else:
                        topnodes[x] = None

                    count += 1

        rowoffset = (height - 1) * width
        for x in range(1, width - 1):
            # Finding the end Node
            if data[rowoffset + x] > 0:
                self.end = Maze.Node((height - 1, x))
                t = topnodes[x]
                t.Neighbours[2] = self.end
                self.end.Neighbours[0] = t
                count += 1
                break

        self.count = count
        self.width = width
        self.height = height
