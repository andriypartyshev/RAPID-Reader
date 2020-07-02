import argparse


import csv
import os
import re




old_path= "C:/Users/avpar/Documents/Unity Projects/ZP"
new_path="C:/Users/avpar/Documents/Unity Projects/archive"
StartCommands=[ "MoveJ",
                "ArcLStart",
                "ArcLEnd",
                "MoveL",
                "ArcL",
                "\tMoveJ",
                "\tArcLStart",
                "\tArcLEnd",
                "\tMoveL",
                "\tArcL",
                "PROC",
                "ENDPROC"
                ]


def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def read_RAPID(filename,savefile):
    regex =r'[\n\r\;\ \,\[\]\'\(\)]+'
    with open(savefile, "w") as save:
        csv.writer(save)
        with open(filename, encoding='utf-8-sig') as rapidFile:
            Lines=rapidFile.readlines()
            j = 1
            for row in Lines:
                split = re.split(regex, row)
                if len(split) <2:
                    continue
                firstWord = split[0]
                is_command=False
                for n in StartCommands:
                    if n==firstWord:
                        is_command=True

                if is_command:

                    b=True
                    if firstWord == "PROC":
                        save.write(firstWord+ " "+split[1]+"\n")
                        continue
                    elif firstWord == "ENDPROC":
                        save.write(firstWord + "\n")
                        continue
                    print(str(j) + ": \t " + firstWord + " " + split[1] + " " + split[2] + " " + split[3])
                    for i in range(1,3):
                        if not is_float(split[i]):
                            b=False
                            break
                    if b:
                        save.write(str(j)+","+firstWord + ","+split[1] + "," + split[2] + ","+split[3]+"\n")
                j+=1




    return





read_RAPID("M_178.mod","record.csv")

