#!/usr/local/bin/python3
import sys
import os

total = 0
INPUT_FILE = "input_small.txt"

#class DirectionEntry:
#    def __init__(self, left: str, right: str):
#        self.left = left
#        self.right = right

#directionSet = []
#directionDictionary  = {}

sourceLines = []

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

gotDirections = False
with open(inputFilePath, 'r') as file:
   for line in file:
      theLine = line.strip()
      parts = theLine.split(' ')

      sourceLines.append(parts)
   #endofr
#endwith

for sourceLine in sourceLines:
   masterDiffList = []
   newDiffLine = []
   firstNum = True
   prevNum = 0
   for num in sourceLine:
      if (firstNum == True):
         firstNum = False
      else:
         diff = num - prevNum
         newDiffLine =
      prevNum = num
      #print (f"{num}")