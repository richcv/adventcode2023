#!/usr/local/bin/python3
import sys
import os

total = 0
INPUT_FILE = "input_small.txt"

class SolutionEntry:
    def __init__(self, path: str, totalValue: int):
        self.path = path
        self.totalValue = totalValue

class PointEntry:
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y

_solutionList = []
_matrix = []
_rowMax = 0
_colMax = 0
_startPos = []
_endPoint = []

# ---------------------------------------------------
# FindSolutions
# ---------------------------------------------------
def FindSolutions():
   FindNextStep("", 0, PointEntry(0, 0), [])

# ---------------------------------------------------
# FindNextStep
# ---------------------------------------------------
def FindNextStep(pathSoFar, totalSoFar, thisPoint, prevPoints):
   global _solutionList
   print (f"Recursing!  Path So Far: {pathSoFar}, Prev Points: {len(prevPoints)}, This Point: {thisPoint.X},{thisPoint.Y}")
   input ("[Press ENTER to continue]")
   prevPoints.append(thisPoint)
   totalSoFar = totalSoFar + GetMatrixValue(thisPoint)
   if ((thisPoint.X == _colMax) and (thisPoint.Y == _rowMax)):
      #We have reached the end!  Record it!
      print(f"Found solution!  Adding it to the list!"
      _solutionList.append(SolutionEntry(pathSoFar, totalSoFar))
      return
   else:
      #Lets try to go N,E,S,W from here
      #North first
      northPoint = PointEntry(thisPoint.X, thisPoint.Y-1)
      eastPoint = PointEntry(thisPoint.X+1, thisPoint.Y)
      southPoint = PointEntry(thisPoint.X, thisPoint.Y+1)
      westPoint = PointEntry(thisPoint.X-1, thisPoint.Y)
      if (isValidStep("N", northPoint, pathSoFar, prevPoints)):
         #print("  NORTH: Let's GO!")
         pathSoFar=pathSoFar+"N"
         FindNextStep(pathSoFar, totalSoFar, northPoint, prevPoints)
      #else:
      #   print("  NORTH: Can't go there")
      #endif
      if (isValidStep("E", eastPoint, pathSoFar, prevPoints)):
         #print("  EAST : Let's GO!")
         pathSoFar=pathSoFar+"E"
         FindNextStep(pathSoFar, totalSoFar, eastPoint, prevPoints)
      #else:
         #print("  EAST : Can't go there")
      #endif
      if (isValidStep("S", southPoint, pathSoFar, prevPoints)):
         #print("  SOUTH: Let's GO!")
         pathSoFar=pathSoFar+"S"
         FindNextStep(pathSoFar, totalSoFar, southPoint, prevPoints)
      #else:
         #print("  SOUTH: Can't go there")
      #endif
      if (isValidStep("W", westPoint, pathSoFar, prevPoints)):
         #print("  WEST : Let's GO!")
         pathSoFar=pathSoFar+"W"
         FindNextStep(pathSoFar, totalSoFar, westPoint, prevPoints)
      #else:
      #   print("  WEST : Can't go there")
      #endif
   #endif
#end
          

def IsThisPointInPreviousPoints(thisPoint, prevPoints):
   foundIt = False
   for point in prevPoints:
      if ((point.X == thisPoint.X) and (point.Y == thisPoint.Y)):
         foundIt = True
         break
   return foundIt
# ---------------------------------------------------
# isValidStep
# ---------------------------------------------------   
def isValidStep(direction, theProposedPoint, pathSoFar, prevPoints):
   valid = True

   tripleCheck = direction * 3
   if (IsThisPointInPreviousPoints(theProposedPoint, prevPoints)):
      #if (theProposedPoint in prevPoints):
      #print(f"  *INVALID CUZ ITS IN PREV POINTS*")
      valid = False
   else:
      if (pathSoFar.endswith(tripleCheck)):
         #print(f"  *INVALID CUZ ITS THREE IN A ROW*")
         valid = False
      else:
         if (theProposedPoint.X < 0) or (theProposedPoint.X > _colMax):
            valid = False
         else:
            if (theProposedPoint.Y < 0) or (theProposedPoint.Y > _rowMax):
               valid = False
            else:
               if GoingBackwards(direction, pathSoFar):
                  valid = False
            #endif
         #endif
      #endif
   #endif
   return valid

def GoingBackwards(direction, pathSoFar):
   valid = True
   if (len(pathSoFar) > 0):
      prevDir = pathSoFar[len(pathSoFar) - 1]
      if (direction == "N" and prevDir == "S"):
         valid = False
      elif (direction == "E" and prevDir == "W"):
         valid = False
      elif (direction == "S" and prevDir == "N"):
         valid = False
      elif (direction == "W" and prevDir == "E"):
         valid = False
   return not valid  
# ---------------------------------------------------
# GetMatrixValue
# ---------------------------------------------------
def GetMatrixValue(thisPoint) -> int:
   if (thisPoint.X > _colMax) or (thisPoint.Y > _rowMax):
      print(f"**ILLEGAL POSITiON REQUESTED [{thisPoint.X},{thisPoint.Y}]**")
      exit(0)
   return _matrix[thisPoint.Y][thisPoint.X]

# ---------------------------------------------------
# GetMatrixValue
# ---------------------------------------------------
#def GetMatrixValue(xPos, yPos):
#   if (xPos > _colMax) or (yPos > _rowMax):
#      print(f"**ILLEGAL POSITiON REQUESTED [{xPos},{yPos}]**")
#      exit(0)
#   return _matrix[yPos][xPos]

# ---------------------------------------------------
# GetMatrixValue
# ---------------------------------------------------
def ReportBestSolution():
   if (len(_solutionList) > 0):
      bestPath = _solutionList[0]
      for entry in _solutionList:
         if entry.totalValue < bestPath.totalValue:
            bestPath = entry
         #endif
      #endfor
      print (f"Solutions found: {len(_solutionList)}" )
      print (f"Best solution: Value: {bestPath.totalValue}, Path: {bestPath.path}")
   else:
      print ("No solutions found??")
   #endif

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

gotDirections = False
with open(inputFilePath, 'r') as file:
   for line in file:
      row = []
      theLine = line.strip()
      for char in line:
         if char.isdigit():
            row.append(int(char))
      #endfor
      _matrix.append(row)
   #endfor
   
#endwith

if (len(_matrix) > 0):
   _rowMax = len(_matrix) - 1
   _colMax = len(_matrix[0]) - 1
   print(f"Here's the _matrix ({_rowMax},{_colMax})")
   print("_" * (_rowMax + 2))
   for yPos in _matrix:
      outputString = ""
      for xPos in yPos:
         if len(outputString) > 0:
            outputString = outputString + str(xPos)
         else:
            outputString = "|"+outputString + str(xPos)
         #endif
      #endfor
      outputString += "|"
      print (outputString);
   #endfor
   print("-" * (_rowMax + 2))        

   #startPos = [0,0]
   _endPoint = PointEntry(_rowMax, _colMax)
   print(f"Start point is 0,0.  End point is {_endPoint.X},{_endPoint.Y}")

   FindSolutions()

   ReportBestSolution()

#endif