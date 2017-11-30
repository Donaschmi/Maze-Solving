from PIL import Image
from numpy import *
import argparse
def merge(in1, in2, result):

    im1 = Image.open(in1)
    im2 = Image.open(in2)

    im1arr = asarray(im1)
    im2arr = asarray(im2)

    im1arrF = im1arr.astype('float')
    im2arrF = im2arr.astype('float')
    additionF = (im1arrF+im2arrF)/2
    addition = additionF.astype('uint8')

    resultImage = Image.fromarray(addition)
    resultImage.save(result)

parser = argparse.ArgumentParser()
parser.add_argument("in1")
parser.add_argument("in2")
parser.add_argument("result")
args = parser.parse_args()

merge(args.in1, args.in2, args.result)
