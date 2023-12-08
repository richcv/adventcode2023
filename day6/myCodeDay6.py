#!/usr/local/bin/python3
import sys
import os

index = 0
limit = 3
total = 1
INPUT_FILE = "input_large.txt"

# ---------------------------------------------------
# is_int
# ---------------------------------------------------
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# ---------------------------------------------------
# def GetValidSolutionCount(time, distanceRecord):
# ---------------------------------------------------
def GetValidSolutionCount(time, distanceRecord):
   maxHit = 0
   print(f"Check time {time} and distance {distanceRecord}...")

   for currentIndex in range(time):
      #print(f"Check button pressed for {currentIndex}...")
      dist = currentIndex * (time - currentIndex)
      
      if (dist > distanceRecord):
         print(f"   Button pressed for {currentIndex}ms and accelerating for {time-currentIndex} - so distance is {dist} *HIT*")
         #print("record hit!")
         maxHit = maxHit + 1
      else:
         print(f"   Button pressed for {currentIndex}ms and accelerating for {time-currentIndex} - so distance is {dist}")
   print (f"Records Beat #: {maxHit}")
   return maxHit

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

timeCollection = []
distanceCollection = []
bigTime = ""
bigDist = ""
with open(inputFilePath, 'r') as file:
   for line in file:
      #print (f"HEY LINE {line}")


      theLine = line.strip()
      if theLine.startswith("Time:"):
         times = theLine.split(" ")
         for timeAtomic in times:
            #print (f"DERP {timeAtomic}")
            if is_int(timeAtomic):
               bigTime = bigTime + str(timeAtomic)
               #timeCollection.append(int(timeAtomic))
      if theLine.startswith("Distance:"):
         times = theLine.split(" ")
         for distAtomic in times:
            if (distAtomic.isdigit()):
               bigDist = bigDist + str(distAtomic)
               #distanceCollection.append(int(distAtomic))

print(f"bigtime: {bigTime}, bigdist: {bigDist}")
timeCollection.append(int(bigTime))
distanceCollection.append(int(bigDist))

index = 0
for derp in timeCollection:
   #print(f"hey here's a time: {derp}")
   total = total * GetValidSolutionCount(derp, distanceCollection[index])
   index = index + 1
#for derp in distanceCollection:
#   print(f"hey here's a dist: {derp}")

#newNum = str(GetFirstNumber(line)) + str(GetLastNumber(line))
#print (f"Here: {newNum}")
#total = total + int(idValue)

print (f"TOTAL: {total}")