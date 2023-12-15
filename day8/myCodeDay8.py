#!/usr/local/bin/python3
import sys
import os

total = 0
INPUT_FILE = "input_large.txt"

class DirectionEntry:
    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

directionSet = []
directionDictionary  = {}

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
      
      if (gotDirections == False):
         for char in theLine:
            directionSet.append(char)
         gotDirections = True
      else:
         if (len(theLine)):
            #print(f"HEY NOW: {theLine}")
            parts = theLine.split("=")
            theKey = parts[0].strip()
            theLeftNode, theRightNode = parts[1].strip("()").split(", ")
            theLeftNode = theLeftNode.replace("(", "").strip()
            theRightNode = theRightNode.replace(")", "").strip()
            directionDictionary[str(theKey)] = DirectionEntry(left=theLeftNode, right=theRightNode)
         #endif
      #endif
   #endofr
#endwith

#print(f"Here's AAA, right: ({directionDictionary['BBB'].right})")
currentNode = "AAA"
loops = 0

while currentNode != "ZZZ":
   
   for step in directionSet:
      #print (f"Doing step {step}")
      if (step.upper() == "L"):
         currentNode = directionDictionary[currentNode].left
      else:
         currentNode = directionDictionary[currentNode].right
      loops = loops + 1   

print (f"TOTAL LOOPS: {loops}")