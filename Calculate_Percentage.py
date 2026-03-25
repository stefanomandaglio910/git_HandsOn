#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Calculate Nucleotide Percentage')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

args = parser.parse_args()

seq = args.seq.upper()
total_length = len(seq)

nucleotides = ["A", "C", "G", "T", "U"]
results = {}

for nucleotide in nucleotides:
    count = seq.count(nucleotide)
    if count > 0:
        percentage = (count / total_length) * 100
        results[nucleotide] = percentage

print(results)


