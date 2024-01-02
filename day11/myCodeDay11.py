import os
import sys
from pathlib import Path
import numpy as np

INPUT_FILE = "input_small.txt"

class PointEntry:
   def __init__(self, X: str, Y: str):
      self.X = X
      self.Y = Y

   def GetNorth(self):
      return PointEntry(self.X - 1, self.Y)
   def GetSouth(self):
      return PointEntry(self.X + 1, self.Y)
   def GetWest(self):
      return PointEntry(self.X, self.Y - 1)
   def GetEast(self):
      return PointEntry(self.X, self.Y + 1)
   

#end class

_pointPath = []

# ---------------------------------------------------
# GetPointValue
# ---------------------------------------------------   
def GetPointValue(thePoint):
   theVal = "?"
   if (thePoint.X >= 0) and (thePoint.X < len(_matrix[0])) and (thePoint.Y >= 0) and (thePoint.Y < len(_matrix)):
      theVal = _matrix[thePoint.X][thePoint.Y]
   return theVal
#end

# ---------------------------------------------------
# PointsAreEqual
# ---------------------------------------------------   
def PointsAreEqual(point1, point2) -> bool:
   return (point1.X == point2.X) and (point1.Y == point2.Y)

# ---------------------------------------------------
# insertRow
# ---------------------------------------------------   
def insertRow(arr, row_num):
    new_row = np.full((1, arr.shape[1]), '.')
    return np.insert(arr, row_num, new_row, axis=0)

# ---------------------------------------------------
# insertColumn
# ---------------------------------------------------   
def insertColumn(arr, col_num):
    new_col = np.full((arr.shape[0], 1), '.')
    return np.insert(arr, col_num, new_col, axis=1)

# ---------------------------------------------------
# ExpandUniverse
# ---------------------------------------------------   
def ExpandUniverse():
   global _matrix
   emptyRows = []
   emptyCols = []
   maxCol = len(_matrix)
   maxRow = len(_matrix[0])

   rowIndex = 0
   for duh in _matrix:
      isEmpty = True
      for char in duh:
         if char != '.':
            isEmpty = False
            break
         #endif
      #endfor
      if (isEmpty):
         emptyRows.append(rowIndex)
      #endif
      rowIndex += 1
   #endfor
   
   for colIndex in range(0, maxCol):
      isEmpty = True
      colCumulative = ""
      for rowIndex in range(0, maxRow):
         theVal = GetPointValue(PointEntry(rowIndex, colIndex))
         colCumulative += theVal
         if (theVal != "."):
            isEmpty = False
         #endif
      #endfor
      #print (f"Col {colIndex} is: {colCumulative}")
      if (isEmpty):
         #print ("  and its empty!")
         emptyCols.append(colIndex)
      #endif
   #endfor
         
   print(f"Empty Rows: {emptyRows}")
   print(f"Empty Cols: {emptyCols}")

   reversed_numbers = emptyRows[::-1]
   for newRow in reversed_numbers:
      print(f"Inserting a new row at position {newRow}")
      _matrix = insertRow(np.array(_matrix), newRow)

   reversed_numbers = emptyCols[::-1]
   for newCol in reversed_numbers:
      print(f"Inserting a new col at position {newCol}")
      _matrix = insertColumn(np.array(_matrix), newCol)

# ---------------------------------------------------
# Main
# ---------------------------------------------------   
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
FILE = os.path.join(script_dir, INPUT_FILE)

with open(FILE) as f:
    _matrix = [list(line.strip()) for line in f]

for duh in _matrix:
   print (f"{duh}")

ExpandUniverse()

for duh in _matrix:
   print (f"{duh}")

#critterLocation = FindTheCritter()
#_pointPath.append(critterLocation)
#print(f"Critter: {GetPointValue(critterLocation)}")

#keepOnTruckin = True
#while keepOnTruckin:
#   nextLocation = FindNextLocation()
#   print(f"Next Loc: {GetPointValue(nextLocation)}")
#   if GetPointValue(nextLocation) == 'S':
#      keepOnTruckin = False
#_pointPath.pop()

#halfway = int(int(len(_pointPath)) / int(2))
#quarter = int(int(halfway) / int(2))
#print (f"Total: {len(_pointPath)}, halfway: {halfway}, farthest: {quarter}")

#nextLocation = FindNextLocation()
#print(f"Next Loc: {GetPointValue(nextLocation)}")

#print (f"Found the critter at {critterLocation.X}/{critterLocation.Y}")

#print (f"{_matrix[critterLocation.X][critterLocation.Y]}")

#data = Path(FILE).read_text()
#matrix = for line in data.splitlines()]

#print ("YO")
#print (f"Matrix: {matrix}")