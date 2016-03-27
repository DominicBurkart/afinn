''' AFINN file encoder! takes an input file and appends AFINN scores to it! '''

import csv
import os
from afinn import *

inputfiledir = input("data file directory: ")
tw_content_indx = int(input("tweet text index in input file (usually 10): "))
print("\n")

listnames = ("AFINN positive","AFINN negative","AFINN sum")

afinn = Afinn()

#opens our input and output files
indoc = open(inputfiledir, encoding = "utf-8")
outdoc= csv.writer(open("no_emoji_out.csv", mode = "w", encoding = "utf-8"), lineterminator ="\n")

def encode(line):
    txt = line[tw_content_indx]
    score_list = afinn.score(txt)
    line.extend(score_list)
    outdoc.writerow(line)

#iterates through the input file and calls encode for each line:
inheader = True 
for line in csv.reader(indoc):
    if inheader: 
        line.extend(listnames)
        outdoc.writerow(line)
        print("populating output file, please wait.")
        inheader = False
    else: #to count words + ratios for each tweet and then write those values to out :)
        encode(line)
print("\nencoding complete.")

