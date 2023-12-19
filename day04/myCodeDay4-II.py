#!/usr/local/bin/python3
import sys
import os

total = 0
INPUT_FILE = "input_small.txt"

# ---------------------------------------------------
# GetWinners
# ---------------------------------------------------
def GetWinners(inString):
   theWinners = []
   #print (f"Anybody got these?? {inString}")
   theWinners = inString.split(' ')

   return theWinners
#end GetWinners

# ---------------------------------------------------
# CalcWinningEntries
# ---------------------------------------------------
def CalcWinningEntries(winners, allEntries):
   winnerCount = 0

   theEntries = allEntries.split(' ')

   for entry in theEntries:
      #print (f"Look for {entry}")
      filteredEntry = entry.strip()
      if (len(filteredEntry) > 0):
         if entry in winners: 
            #
            winnerCount = winnerCount + 1
            if winnerCount > 2:
               winnerCount = (winnerCount - 1) * 2
            print(f"  winner <{entry}> - points: {winnerCount}")

   return winnerCount

#end CalcWinningEntries

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

winnerCollection = []
distanceCollection = []

index = 0
with open(inputFilePath, 'r') as file:
   for line in file:
      index = index + 1
      print(f"Parsing line {index}")
      theLine = line.strip()
      if theLine.startswith("Card"):
         afterColon = theLine.split(":")[1].strip()

         pipeSplits = afterColon.split("|")

         winnerCollection = GetWinners(pipeSplits[0].strip())
         total = total + CalcWinningEntries(winnerCollection, pipeSplits[1])

print (f"TOTAL: {total}")