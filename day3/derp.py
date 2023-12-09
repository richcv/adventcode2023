#!/bin/python3

from collections import namedtuple

# Define the Cube class using namedtuple
Cube = namedtuple("Cube", ["color", "count"])
cubeBag = []
INPUT_FILE="input_large.txt"

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
# GetIDValue
# ------------------------------------------------
def GetValueOfDisconnectedNums(lineIndex, prevLine, currLine, nextLine):
   returnVal = 0
   #print(f"PrevLine: {prevLine}")
   #print(f"CurrLine: {currLine}")
   #print(f"NextLine: {nextLine}")

   symbolLocations = []

   #Get symbol line positions for all 3 lines
   linePos = 0
   for char in prevLine:
      linePos = linePos + 1
      if (not char.isdigit()) and (char != "."):
         symbolLocations.append(linePos)
   linePos = 0
   for char in currLine:
      linePos = linePos + 1
      if (not char.isdigit()) and (char != "."):
         symbolLocations.append(linePos)
   linePos = 0
   for char in nextLine:
      linePos = linePos + 1
      if (not char.isdigit()) and (char != "."):
         symbolLocations.append(linePos)
   
   #for positions in symbolLocations:
   #   print ("Postion " + str(positions))
   numberCollection = []
   buffer = ''

   linePos = 0
   for char in currLine:   
      linePos = linePos + 1
      if char.isdigit():
         buffer = buffer + char
      else:
         if (buffer != ''):
            numberCollection.append((int(buffer), linePos - len(buffer)))
         buffer = ''
      #endif
   #endfor
   if (buffer != ''):
      numberCollection.append((int(buffer), linePos - len(buffer)))
   buffer = ''

   for num, position in numberCollection:
      #print(f"Number: {num}, Start Position {position}")
      isFound = False
      for symPosition in symbolLocations:
         if (symPosition >= position - 1) and (symPosition <= position + len(str(num))):
            isFound = True
      if (isFound == False):
         print (f"**{num} IS NOT CONNECTED (Line {lineIndex})***")
      else:
         returnVal = returnVal + num

  
   #Get Connected numbers on current line (start, stop)
   #Foreach connectedNumber
   #  IsTouching = false
   #  For each symbol postion
   #    If that position is touching
   #       IsTOuching = true
   #  End
   #  If IsTouching == False
   #     returnVal = returnVal + connectedNumber.vaue  

   return returnVal
#end def

# ------------------------------------------------
# MAIN
# ------------------------------------------------
total = 0
defaultLine = "......................................................................................................................................"
lineIndex = 0

prevLine = defaultLine
nextLine = "*ERROR*"

file = open(INPUT_FILE, "r")
lines = file.readlines()  # Read all lines into a list
for line in lines:
   lineIndex = lineIndex + 1
   
   currLine = line.strip()
   if (lineIndex >= len(lines)):
      nextLine = defaultLine
   else:
      nextLine = lines[lineIndex]

   total = total + GetValueOfDisconnectedNums(lineIndex, prevLine.strip(), currLine.strip(), nextLine.strip())
   prevLine = currLine

   #print ("")
#endfor
file.close()

print (f"TOTAL HERE BRO: {total}")
