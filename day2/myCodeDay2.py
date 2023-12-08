#!/usr/local/bin/python3
import sys
import os

index = 0
limit = 3
total = 0

def GetIDNum(theLine):
   gameNumber = 0
   words = theLine.split()
   if len(words) > 1 and words[0] == "Game":
      try:
         parseThis = words[1].rstrip(":")
         gameNumber = int(parseThis)
      except:
         print ("*** PROBLEM ***")
      #end
   #end
   return gameNumber
#endif

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, 'input_small.txt')
with open(inputFilePath, 'r') as file:
   for line in file:
      index = index + 1
      line = line.rstrip("\n")
      
      print(f"{index}. Hey heres a line --> " + line)
      if (line.startswith("Game")):
          idValue = GetIDNum(line)
      #newNum = str(GetFirstNumber(line)) + str(GetLastNumber(line))
      #print (f"Here: {newNum}")
      total = total + int(idValue)

print (f"TOTAL: {total}")