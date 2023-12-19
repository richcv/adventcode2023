import os
import sys
from pathlib import Path
INPUT_FILE = "input_large.txt"

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
# FindNextLocation
# ---------------------------------------------------   
def FindNextLocation() -> PointEntry:
   currentPoint = _pointPath[len(_pointPath) - 1]
   currentVal = GetPointValue(currentPoint)
   nextPoint = PointEntry(0, 0)
   
   # Start point
   if (currentVal == "S"):
      #OK, so we're going to search NESW from here.  Two of them should match, but we'll take the first
      #check north first
      northPoint = currentPoint.GetNorth()
      northPointVal = GetPointValue(northPoint)
      #print(f"North is {northPointVal}")

      eastPoint = currentPoint.GetEast()
      eastPointVal = GetPointValue(eastPoint)
      #print(f"East is {eastPointVal}")

      southPoint = currentPoint.GetSouth()
      southPointVal = GetPointValue(southPoint)
      #print(f"South is {southPointVal}")

      westPoint = currentPoint.GetWest()
      westPointVal = GetPointValue(westPoint)
      #print(f"West is {westPointVal}")

      if northPointVal == "|" or northPointVal == "7" or northPointVal == "F":
         #print("North is good")
         nextPoint = northPoint
      elif eastPointVal == "-" or eastPointVal == "7" or eastPointVal == "J":
         #print("East is good")
         nextPoint = eastPoint
      elif southPointVal == "|" or southPointVal == "L" or northPointVal == "J":
         #print("south is good")
         nextPoint = southPoint
      elif westPointVal == "-" or westPointVal == "L" or westPointVal == "F":
         #print("west is good")
         nextPoint = westPoint

   else:
      prevPoint = _pointPath[len(_pointPath) - 2]
      match currentVal:
         case "|":
            if (PointsAreEqual(prevPoint, currentPoint.GetNorth())):
               nextPoint = currentPoint.GetSouth()
            else:
               nextPoint = currentPoint.GetNorth()
         case "-":
            if (PointsAreEqual(prevPoint, currentPoint.GetWest())):
               nextPoint = currentPoint.GetEast()
            else:
               nextPoint = currentPoint.GetWest()
         case "L":
            if (PointsAreEqual(prevPoint, currentPoint.GetNorth())):
               nextPoint = currentPoint.GetEast()
            else:
               nextPoint = currentPoint.GetNorth()
         case "J":
            if (PointsAreEqual(prevPoint, currentPoint.GetWest())):
               nextPoint = currentPoint.GetNorth()
            else:
               nextPoint = currentPoint.GetWest()
         case "7":
            if (PointsAreEqual(prevPoint, currentPoint.GetWest())):
               nextPoint = currentPoint.GetSouth()
            else:
               nextPoint = currentPoint.GetWest()
         case "F":
            if (PointsAreEqual(prevPoint, currentPoint.GetEast())):
               nextPoint = currentPoint.GetSouth()
            else:
               nextPoint = currentPoint.GetEast()
         case "S":
            print("DONE")
            exit(0)

   _pointPath.append(nextPoint)   
   return nextPoint

# ---------------------------------------------------
# FindTheCritter
# ---------------------------------------------------   
def FindTheCritter() -> PointEntry:
   
   currentRow = 0
   currentCol = 0
   critterLocation = None

   for row in _matrix:
      currentRow = 0
      for colVal in row:
         if colVal == 'S':
            #print ("FOUND IT!")
            critterLocation = PointEntry(currentCol, currentRow)
            break
         currentRow += 1
      currentCol += 1
   return critterLocation

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


critterLocation = FindTheCritter()
_pointPath.append(critterLocation)
print(f"Critter: {GetPointValue(critterLocation)}")

keepOnTruckin = True
while keepOnTruckin:
   nextLocation = FindNextLocation()
   print(f"Next Loc: {GetPointValue(nextLocation)}")
   if GetPointValue(nextLocation) == 'S':
      keepOnTruckin = False
_pointPath.pop()

halfway = int(int(len(_pointPath)) / int(2))
quarter = int(int(halfway) / int(2))
print (f"Total: {len(_pointPath)}, halfway: {halfway}, farthest: {quarter}")

#nextLocation = FindNextLocation()
#print(f"Next Loc: {GetPointValue(nextLocation)}")

#print (f"Found the critter at {critterLocation.X}/{critterLocation.Y}")

#print (f"{_matrix[critterLocation.X][critterLocation.Y]}")

#data = Path(FILE).read_text()
#matrix = for line in data.splitlines()]

#print ("YO")
#print (f"Matrix: {matrix}")