#!/bin/python3
import os

INPUT_FILE="input_large.txt"

# ------------------------------------------------
# GetValueOfDoubleConnectedSymbols
# ------------------------------------------------
def GetValueOfDoubleConnectedSymbols(lineIndex, prevLine, currLine, nextLine):
   returnVal = 0
   #print(f"PrevLine: {prevLine}")
   #print(f"CurrLine: {currLine}")
   #print(f"NextLine: {nextLine}")

   #PSUEDOCODE
   #Get Connected numbers on current line (start, stop)
   #Foreach connectedNumber
   #  IsTouching = false
   #  For each symbol postion
   #    If that position is touching
   #       IsTOuching = true
   #  End
   #  If IsTouching == False
   #     returnVal = returnVal + connectedNumber.vaue  

   symbolLocations = []
   numberCollection = []

   #Get number positions for all 3 lines
   linePos = 0
   for char in currLine:
      linePos = linePos + 1
      if (not char.isdigit()) and (char != "."):
         symbolLocations.append(linePos)
      #endif
   #endfor

   buffer = ''

   #PrevLine
   linePos = 0
   for char in prevLine:   
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

   #Line
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

   #NextLine
   linePos = 0
   for char in nextLine:   
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

   #Now loop thru the symbols and see if theres at least two numbers nearby

   for symPosition in symbolLocations: 
      connectionsFound = 0
      numProduct = 1
      for num, position in numberCollection:
         if (symPosition >= position - 1) and (symPosition <= position + len(str(num))):
            connectionsFound = connectionsFound + 1
            numProduct = numProduct * num
         #endif
      #endfor
      if (connectionsFound > 1):
         returnVal = returnVal + numProduct


   #for num, position in numberCollection:
   #   #print(f"Number: {num}, Start Position {position}")
   #   isFound = False
   #   for symPosition in symbolLocations:
   #      if (symPosition >= position - 1) and (symPosition <= position + len(str(num))):
   #         isFound = True
   #   if (isFound == False):
   #      print (f"**{num} IS NOT CONNECTED (Line {lineIndex})***")
   #   else:
   #      returnVal = returnVal + num
   
   return returnVal
#end GetValueOfDoubleConnectedSymbols

# ------------------------------------------------
# MAIN
# ------------------------------------------------
total = 0
defaultLine = "......................................................................................................................................"
lineIndex = 0

prevLine = defaultLine
nextLine = "*ERROR*"

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

file = open(inputFilePath, "r")
lines = file.readlines()  # Read all lines into a list
for line in lines:
   lineIndex = lineIndex + 1
   
   currLine = line.strip()
   if (lineIndex >= len(lines)):
      nextLine = defaultLine
   else:
      nextLine = lines[lineIndex]

   total = total + GetValueOfDoubleConnectedSymbols(lineIndex, prevLine.strip(), currLine.strip(), nextLine.strip())
   prevLine = currLine

   #print ("")
#endfor
file.close()

print (f"TOTAL HERE BRO: {total}")
