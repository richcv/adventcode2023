#!/usr/local/bin/python3
import sys
import os

index = 0
limit = 3
total = 0
INPUT_FILE = "input_large.txt"

#HANDTYPES:
# 0: Highcard
# 1: OnePair
# 2: TwoPair
# 3: Three of a kind
# 4: Full House
# 5: Four of a kind
# 6: Five of a kind

class HandClass:
    def __init__(self, hand: str, handtype: int, bid: int, rank: int):
        self.hand = hand
        self.handtype = handtype
        self.bid = bid
        self.rank = rank
handCollection = []

# ---------------------------------------------------
# DetermineHandType
# ---------------------------------------------------
def DetermineHandType(inHandString):
   theHandType = 0
   cardCount = {}

   for char in inHandString:
      if char not in cardCount:
         cardCount[char] = 1
      else:
         cardCount[char] += 1

   #print(cardCount)
   for char, count in cardCount.items():
      #print (f"   card: {char}, count: {count}")
      if count == 2:
         if theHandType == 0:
            theHandType = 1
         elif theHandType == 1:
            theHandType = 2
         elif theHandType == 3:
            theHandType = 4
      elif count == 3:
         if theHandType == 1:
            theHandType = 4
         elif theHandType < 3:
            theHandType = 3
      elif count == 4:
         theHandType = 5
      elif count == 5:
         theHandType = 6

   return theHandType

# ---------------------------------------------------
# CompareEm
# ---------------------------------------------------
def CompareEm(obj):
   sortKey = obj.handtype

   extraSort = ""
   transmog = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13} 
   for char in obj.hand.strip():
      #print(f"  convert {char}")
      extraSort = extraSort + str(transmog[char]).zfill(2)
   print (f"{obj.hand} extra sort key is {extraSort}")
   extraSort = str(sortKey) + extraSort
   
   return int(extraSort)

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

with open(inputFilePath, 'r') as file:
   for line in file:
      theLine = line.strip()
      parts = theLine.split(" ")
      if (len(parts) > 1):
         theHand = parts[0]
         theBid = parts[1]
         #print(f"Determine hand type for {theHand}")
         theHandType = DetermineHandType(theHand)
         handCollection.append(HandClass(theHand, theHandType, theBid, 0))
         #print (f"hand: {parts[0]}, bid: {parts[1]}")
      #endif
   #endofr
#endwith

for hand in handCollection:
   print(f"Hand: {hand.hand}, Bid: {hand.bid}, HandType: {hand.handtype}")

print ("LETS RANK EM")
sortedCollection = sorted(handCollection, key=CompareEm)

rankIndex = 0
for hand in sortedCollection:
   rankIndex += 1
   hand.rank = rankIndex
   theValue = int(hand.rank) * int(hand.bid)
   print(f"Hand: {hand.hand}, Bid: {hand.bid}, HandType: {hand.handtype}, Rank: {hand.rank}, Value: {theValue}")
   total = total + theValue

print (f"TOTAL: {total}")