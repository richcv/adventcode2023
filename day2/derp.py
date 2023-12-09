#!/bin/python3

from collections import namedtuple

# Define the Cube class using namedtuple
Cube = namedtuple("Cube", ["color", "count"])
cubeBag = []
INPUT_FILE="input_small.txt"

# ------------------------------------------------
# MakeCubeBag
# ------------------------------------------------
def MakeCubeBag():

   global cubeBag

   # Create a bag of cubes
   cubeBag = [
      Cube(color="red", count=12),
      Cube(color="green", count=13),
      Cube(color="blue", count=14),
   # Add more cubes as needed
   ]
#end MakeCubeBag


# ------------------------------------------------
# GetIDValue
# ------------------------------------------------
def GetIDValue(inString):
   outVal = 0
   if (':' in inString):
      parts = inString.split(':')
      parts2 = parts[0].split(' ')
      if (len(parts2) > 1):
         outVal = parts2[1]
      #endif
   #endif
   return outVal
#end GetIDValue

# ------------------------------------------------
# GetIDValue
# ------------------------------------------------
def LineIsPossible(inString):
   isPossible = True
   if (':' in inString):
      parts1 = inString.split(':')
      if (len(parts1) > 1):
         parts2 = parts1[1].split(';')
         for chunk in parts2:
            #print (f"Heres a chunk bruv: {chunk}")
            parts3 = chunk.split(',')
            for chunk2 in parts3:
               #print(f"Here's an atomic part bruv {chunk2}")
               parts4 = chunk2.strip().split(' ')
               if (len(parts4) > 1):
                  theColor = parts4[1].strip()
                  theCount = int(parts4[0].strip())
                  #print (f"Count: {theCount}, Color: {theColor}")
                  for cube in cubeBag:
                     if (cube.color.strip().lower() == theColor.lower()):
                        if (int(theCount) > int(cube.count)):
                           #print ("**INVALID!**")
                           isPossible = False

   
   return isPossible
#end GetIDValue

# ------------------------------------------------
# GetIDValue
# ------------------------------------------------
def CubePower(inString):
   thePower = 0
   maxRed = 1
   maxGreen = 1
   maxBlue = 1

   if (':' in inString):
      parts1 = inString.split(':')
      if (len(parts1) > 1):
         parts2 = parts1[1].split(';')
         for chunk in parts2:
            #print (f"Heres a chunk bruv: {chunk}")
            parts3 = chunk.split(',')
            for chunk2 in parts3:
               #print(f"Here's an atomic part bruv {chunk2}")
               parts4 = chunk2.strip().split(' ')
               if (len(parts4) > 1):
                  theColor = parts4[1].strip()
                  theCount = int(parts4[0].strip())
                  #print (f"Count: {theCount}, Color: {theColor}")
                  if (theColor.lower() == "green" and theCount > maxGreen):
                     maxGreen = theCount
                  elif (theColor.lower() == "blue" and theCount > maxBlue):
                     maxBlue = theCount
                  elif (theColor.lower() == "red" and theCount > maxRed):
                     maxRed = theCount
                  
   print (f"{inString} - maxes: red:{maxRed}, green:{maxGreen}, blue{maxBlue}")
   thePower = maxRed * maxGreen * maxBlue
   return thePower
#end CubePower

# ------------------------------------------------
# MAIN
# ------------------------------------------------
MakeCubeBag()
total = 0

with open(INPUT_FILE, "r") as file:
   for line in file:
      theLine = line.strip()
      idVal = int(GetIDValue(theLine))
      total = total + CubePower(theLine)
      #if (LineIsPossible(theLine)):
      #   total = total + idVal
      #endif
   #endfor
#end with

print (f"TOTAL HERE BRO: {total}")

# Accessing cubes in the bag
#for cube in cubeBag:
#    print(f"Color: {cube.color}, Count: {cube.count}")
