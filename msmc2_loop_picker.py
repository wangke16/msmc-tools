#!/usr/bin/env python3

import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("loopfile", help="Input file whatever_prefix.msmc2.loop.txt, output will be - whatever_prefix.msmc2.final.txt")
args = parser.parse_args()

cn = 0
recbs = []
logLs = []
times = []
lambdas = []

f = open(args.loopfile, "r")
for line in f:
    fields = line.strip().split()
    recb = fields[0]
    logL = fields[1]
    time = fields[2]
    lamb = fields[3]
    recbs.append(recb)
    logLs.append(logL)
    times.append(time)
    lambdas.append(lamb)
    cn = cn + 1

length = len(times[-1].split(","))
tlefts = times[-1].split(",")[:-1]
trights = times[-1].split(",")[1:]

ofn = args.loopfile.replace('loop','final')

of = open('./'+ofn, "wt")
of.write("time_index\tleft_time_boundary\tright_time_boundary\tlambda\n")

for i, tl, tr, lamb in zip(range(0,32), tlefts, trights, list(lambdas[-1].split(","))):
    of.write(str(i) +"\t"+ tl +"\t"+ tr +"\t"+ lamb +"\n")
of.close()
