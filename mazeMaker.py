# Random Maze Generator using Depth-first Search
# http://en.wikipedia.org/wiki/Maze_generation_algorithm
# FB - 20121214
import random
from PIL import Image
import numpy as np
from numpy.random import random_integers as rand
import argparse

def mazeMaker(mx, my, output_file):
    mx = int(mx)
    my = int(my)
    imgx = mx+1; imgy = my+1
    image = Image.new("RGB", (imgx+1, imgy+1))
    pixels = image.load()
    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
    color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
    # start the maze from a random cell
    stack = [(random.randint(0, mx - 1), random.randint(0, my - 1))]

    while len(stack) > 0:
        (cx, cy) = stack[-1]
        maze[cy][cx] = 1
        # find a new cell to add
        nlst = [] # list of available neighbors
        for i in range(4):
            nx = cx + dx[i]; ny = cy + dy[i]
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                for j in range(4):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                        if maze[ey][ex] == 1: ctr += 1
                if ctr == 1: nlst.append(i)
        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            cx += dx[ir]; cy += dy[ir]
            stack.append((cx, cy))
        else: stack.pop()

            # paint the maze
    for ky in range(1,imgy):
        for kx in range(1,imgx):
            pixels[kx, ky] = color[maze[my * ky / imgy][mx * kx / imgx]]
    rand1 = random.randint(1, imgx - 1)
    rand2 = random.randint(1, imgx - 1)
    pixels[rand1, 0] = pixels[rand2, imgy] = color[1]
    image.save(output_file)


def mazeMaker_(width, height, complexity, density, output_file):
    height = int(height)
    width = int(width)

    image = Image.new("RGB", (width, height))
    pixels = image.load()
    color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze

    Z = np.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    for ky in range(1,height-1):
        for kx in range(1,width-1):
             pixels[kx, ky] = color[1] if Z[kx, ky] == 0 else color[0]
    image.save(output_file)

def blogMaze(output_file):
    A = [[0,0,0,1,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,1,0,1,0],
    [0,1,1,0,1,1,1,1,1,0],
    [0,0,1,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,1,1,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,1,0,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,1,0,0,0]]
    image = Image.new("RGB",( 10, 10))
    pixels = image.load()
    color = [(0,0, 0), (255, 255, 255)] # RGB colors of the maze

    for i in range(10):
        for j in range(10):
            if A[i][j] == 0:
                pixels[j, i] = color[0]
            else:
                pixels[j, i] = color[1]
    image.save(output_file)

parser = argparse.ArgumentParser()
parser.add_argument("dim")
parser.add_argument("result")
args = parser.parse_args()

#mazeMaker_(args.dim, args.dim, .1000, .75, args.result)
#mazeMaker(args.dim, args.dim, args.result)
blogMaze(args.result)
