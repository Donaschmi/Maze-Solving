from PIL import Image
import time
from mazes import Maze
from factory import SolverFactory

import argparse


def solve(factory, method, input_file, output_file):
    # Load Image
    print "Loading Image"
    im = Image.open(input_file)

    # Create maze
    print "Creating maze"
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print "Node Count:", maze.count
    total = t1 - t0
    print "Time elapsed:", total, "\n"

    # Create and run solver
    [title, solver] = factory.createSolver(method)
    print "Starting solving"
    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1 - t0

    print "Nodes explored:", stats[0]
    if stats[2]:
        print "Path found, length :", stats[1]
    else:
        print "No path found"
    print "Time elapsed: ", total, "\n"

    # Create and save output image

    print "Saving Image"
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)
    print float(1)/length

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        #Blue -> Red
        r = (float(i) / length) * 255.0
        px = (int(r), 0, 255 - int(r))


        if a[0] == b[0]:
            # Same Y -- horizontal line
            for x in range(min(a[1], b[1]), max(a[1], b[1])):
                impixels[x, a[0]] = px
        elif a[1] == b[1]:
            # Same X -- vertical line
            for y in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                impixels[a[1], y] = px

    im.save(output_file)



def main():
    sf = SolverFactory()
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", nargs='?', const=sf.Default, default=sf.Default, choices=sf.Choices)
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    solve(sf, args.method, args.input_file, args.output_file)

if __name__ == "__main__":
    main()
