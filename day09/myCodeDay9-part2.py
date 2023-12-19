#!/usr/local/bin/python3
import sys
import os

total = 0
INPUT_FILE = "input_large.txt"

#class DirectionEntry:
#    def __init__(self, left: str, right: str):
#        self.left = left
#        self.right = right

#directionSet = []
#directionDictionary  = {}

sourceLines = []

# ---------------------------------------------------
# StillNonZeros
# ---------------------------------------------------
def StillNonZeros(theLine) -> bool:
   notAllZeros = False
   for linePart in theLine:
      if linePart != 0:
         notAllZeros = True
   #print(f"Zero check? {notAllZeros}")
   return notAllZeros

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

toteTotes = 0
for sourceLine in sourceLines:
   #print (f"Here's a line: {sourceLine}")
   theLine = sourceLine

   theStack = []
   currentLine = theLine
   
   while StillNonZeros(currentLine):
      theStack.append(currentLine)
      firstVal = True
      prevVal = 0
      newLine = []
         
      print(f"{currentLine} (length is {len(currentLine)})")
      for val in currentLine:
         #print (f"loop on this value: {val}")

         if firstVal:
            firstVal = False
         else:
            diff = int(val) - int(prevVal)
            newLine.append(diff)
         prevVal = val
      #end for
      currentLine = newLine
   #end while
   theStack.append(currentLine)
   print(f"{currentLine} (length is {len(currentLine)})")
   
   #firstNode = True
   prevVal = 0
   totes = 0
   for thisGuy in reversed(theStack):
      
      #if firstNode:
      #   firstNode = False
      #else:
      #   totes = totes + (int(thisGuy[0]) - prevVal)
      #print(f"  subtracting {prevVal} from {thisGuy[0]}")
      leftVal = int(thisGuy[0]) - prevVal
      #print(f"  LeftVal: {leftVal}")
      prevVal = leftVal
      totes = leftVal

   print (f"LEFT OF SERIES: {totes}")
   toteTotes += totes
   print (" ")
#end
   
print (f"Final total: {toteTotes}")


         
   #     if prevVal not none:
   #        newline.append(val - prevVal)
   #  workingline = newline
   #stack.push(workingline)
   #

   #masterDiffList = []
   #newDiffLine = []
   #firstNum = True
   #prevNum = 0
   #for num in sourceLine:
   #   if (firstNum == True):
   #      firstNum = False
   ##   else:
   #      diff = num - prevNum
   #      newDiffLine =
   #   prevNum = num
   #   #print (f"{num}")