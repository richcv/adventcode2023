#!/usr/local/bin/python3
import sys
import os

index = 0
limit = 3
total = 0
INPUT_FILE = "input_large.txt"

class TableEntry:
    def __init__(self, destRangeStart: int, sourceRangeStart: int, rangeLength: int):
        self.destRangeStart = destRangeStart
        self.sourceRangeStart = sourceRangeStart
        self.rangeLength = rangeLength

_seeds= []
_seedToSoilMap = []
_soilToFertilizerMap = []
_fertilizerToWaterMap = []
_waterToLightMap = []
_lightToTemperatureMap = []
_temperatureToHumidityMap= []
_humidityToLocationMap = []

# ---------------------------------------------------
# GetOutputFromTable
# ---------------------------------------------------
def GetOutputFromTable(theInput, theMap, debug=False):
   theOutput = int(theInput)

   inputNum = int(theInput)
   for mapEntry in theMap:
      lowerLimit = int(mapEntry.sourceRangeStart)
      upperLimit = lowerLimit + int(mapEntry.rangeLength)
      if (debug == True):
         print(f"   Is {inputNum} between {lowerLimit} and {upperLimit}?")
      if (inputNum >= lowerLimit) and (inputNum <= upperLimit):
         if (debug == True):
            print(f"      YES!")
         offset = inputNum - int(mapEntry.sourceRangeStart)
         theOutput = int(mapEntry.destRangeStart) + offset
         break
   return theOutput

# ---------------------------------------------------
# Main
# ---------------------------------------------------
inputFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), INPUT_FILE)

activeTable = None
with open(inputFilePath, 'r') as file:
   for line in file:
      theLine = line.strip()
      #print(f"Line: {theLine}")
      if (theLine.startswith("seeds:")):
         theParts = theLine.split(' ')
         index = 0
         StartingSeedNum = 0
         for part in theParts:
            if index > 0:
               if index % 2 == 1:
                  #Odd num, must be start num
                  StartingSeedNum = int(part)
               else:
                  #Even num, must be range
                  for seedNum in range(StartingSeedNum, StartingSeedNum + int(part)):
                     print(f"Adding seed {seedNum}")
                     _seeds.append(seedNum)
                  #endfor
               #endif
            #endif
            index += 1
         #endfor
      elif (theLine.startswith("seed-to-soil")):
         activeTable = _seedToSoilMap
      elif (theLine.startswith("soil-to-fertilizer")):
         activeTable = _soilToFertilizerMap
      elif (theLine.startswith("fertilizer-to-water")):
         activeTable = _fertilizerToWaterMap
      elif (theLine.startswith("water-to-light")):
         activeTable = _waterToLightMap
      elif (theLine.startswith("light-to-temperature")):
         activeTable = _lightToTemperatureMap
      elif (theLine.startswith("temperature-to-humidity")):
         activeTable = _temperatureToHumidityMap
      elif (theLine.startswith("humidity-to-location")):
         activeTable = _humidityToLocationMap
      elif (len(theLine) > 0):
         theParts = theLine.split(' ')
         if (len(theParts) == 3):
            activeTable.append(TableEntry(theParts[0], theParts[1], theParts[2]))
         else:
            print("** ERROR?  WHAT THIS?")
         #endif
      #endif
   #end for
#end with

#print("TEST DUMP temperature-to-humidity")
#for derp in _temperatureToHumidityMap:
#   print (f"   1: {derp.destRangeStart}, 2: {derp.sourceRangeStart}, 3: {derp.rangeLength}")

#print("TEST DUMP water-to-light")
#for derp in _waterToLightMap:
#   print (f"   1: {derp.destRangeStart}, 2: {derp.sourceRangeStart}, 3: {derp.rangeLength}")
index = 0
lowestLocation = 0
for seed in _seeds:
   #print(f"Alright, lets figure out seed: {seed}")
   soil = GetOutputFromTable(seed, _seedToSoilMap)
   fertilizer = GetOutputFromTable(soil, _soilToFertilizerMap)
   water = GetOutputFromTable(fertilizer, _fertilizerToWaterMap)
   light = GetOutputFromTable(water, _waterToLightMap)
   temperature = GetOutputFromTable(light, _lightToTemperatureMap)
   humidity = GetOutputFromTable(temperature, _temperatureToHumidityMap)
   location = GetOutputFromTable(humidity, _humidityToLocationMap)
   print(f"Seed: {seed}, Soil: {soil}, Fert: {fertilizer}, Water: {water}, Light: {light}, Temp: {temperature}, Humidity: {humidity}, Location: {location}")
   
   if (index == 0):
      lowestLocation = location
   if (location < lowestLocation):
      lowestLocation = location
   index += 1
   #print("--------------------------------------")
print (f"Lowest location: {lowestLocation}")