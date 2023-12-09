#!/usr/local/bin/python3
import sys
import os

index = 0
limit = 3
total = 1
INPUT_FILE = "input_small.txt"

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

# ---------------------------------------------------
# Main
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
      #print (f"card: {char}, count: {count}")
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

def RankTheCollection():
   global handCollection
   order = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'K': 11, 'Q': 12, 'A': 13} 
   handCollection.sort(key=lambda x: (x.handtype, [order[c] for c in x.hand], x.hand))

   for i, obj in enumerate(handCollection):
      obj.rank = i

# ---------------------------------------------------
# Main
# ---------------------------------------------------
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
inputFilePath = os.path.join(script_dir, INPUT_FILE)

handCollection = []

with open(inputFilePath, 'r') as file:
   for line in file:
      theLine = line.strip()
      parts = theLine.split(" ")
      if (len(parts) > 1):
         theHand = parts[0]
         theBid = parts[1]
         theHandType = DetermineHandType(theHand)
         handCollection.append(HandClass(theHand, theHandType, theBid, 0))
         #print (f"hand: {parts[0]}, bid: {parts[1]}")
      #endif
   #endofr
#endwith

for hand in handCollection:
   print(f"Hand: {hand.hand}, Bid: {hand.bid}, HandType: {hand.handtype}")

print ("LETS RANK EM")
RankTheCollection()

for hand in handCollection:
   print(f"Hand: {hand.hand}, Bid: {hand.bid}, HandType: {hand.handtype}, Rank: {hand.rank}")

print (f"TOTAL: {total}")