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
currentNodes = []

def CurrentNodesEndWithZs(currentNodes):
   allZs = True
   for node in currentNodes:
      #print (f"check this node: {node}")
      if not (node.endswith('Z')):
         allZs = False
   #print (f"All Zs?  {allZs}")
   return allZs

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
            if (theKey.endswith('A')):
               currentNodes.append(theKey)
            theLeftNode, theRightNode = parts[1].strip("()").split(", ")
            theLeftNode = theLeftNode.replace("(", "").strip()
            theRightNode = theRightNode.replace(")", "").strip()
            directionDictionary[str(theKey)] = DirectionEntry(left=theLeftNode, right=theRightNode)
         #endif
      #endif
   #endofr
#endwith

#print(f"Here's AAA, right: ({directionDictionary['BBB'].right})")

loops = 0

while not CurrentNodesEndWithZs(currentNodes):
#while currentNode != "ZZZ":
   
   for step in directionSet:
      newCurrentNodes = []
      for currentNode in currentNodes:
         #print (f"Doing step {step}")
         if (step.upper() == "L"):
            newCurrentNodes.append(directionDictionary[currentNode].left)
            #print(f"  New node is {currentNode}")
         else:
            newCurrentNodes.append(directionDictionary[currentNode].right)
            #print(f"  New node is {currentNode}")
      loops = loops + 1 
      currentNodes = newCurrentNodes 
      print (f"Step {loops}: Node states: {currentNodes}")
      
print (f"TOTAL LOOPS: {loops}")