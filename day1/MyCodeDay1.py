#!/usr/local/bin/python3
import sys
import os

print("WHATUP DAWG")

def JustNums(theLine):
   justNums = ""
   
   theLength = len(theLine)
   
   for theNum in range(theLength):
      if (theLine[theNum].isdigit()):
         justNums = justNums + theLine[theNum]
      else:
         if (theLine.startswith("one", theNum)):
            justNums = justNums + "1"
         elif (theLine.startswith("two", theNum)):
            justNums = justNums + "2"
         elif (theLine.startswith("three", theNum)):
            justNums = justNums + "3"
         elif (theLine.startswith("four", theNum)):
            justNums = justNums + "4"
         elif (theLine.startswith("five", theNum)):
            justNums = justNums + "5"
         elif (theLine.startswith("six", theNum)):
            justNums = justNums + "6"
         elif (theLine.startswith("seven", theNum)):
            justNums = justNums + "7"
         elif (theLine.startswith("eight", theNum)):
            justNums = justNums + "8"
         elif (theLine.startswith("nine", theNum)):
            justNums = justNums + "9"

   
   return justNums

def GetFirstNumber(theLine):
   match = "?"
   for char in theLine:
      if (char.isdigit()):
         match = char
         break
   return match
#end GetFirstNumber

def GetLastNumber(theLine):
   match = "?"
   for char in reversed(theLine):
      if (char.isdigit()):
         match = char
         break
   return match

index = 0
limit = 3
total = 0

with open('input.txt', 'r') as file:
   for line in file:
      line = line.rstrip("\n")
      index = index + 1
      #if (index > limit):
      #   print("**DONE**")
      #   break
      print(f"{index}. Hey heres a line --> " + line)
      line = JustNums(line)
      print(f"  Or.. {line}")
      newNum = str(GetFirstNumber(line)) + str(GetLastNumber(line))
      #print("First num is : " + str(GetFirstNumber(line)))
      #print("Last number is: " + str(GetLastNumber(line)))
      print (f"Here: {newNum}")
      total = total + int(newNum)

print (f"TOTAL: {total}")