import io
import shutil
import os
import codecs
import re
    
  
def updateFileContent(file, text):
  #print("file: " + file)
  #print("text: " + text)
  with open(file, 'w', encoding='utf8') as f:
    f.write(text)

def getFileContent(file):
  with open(file, encoding='utf8') as f:
    text = f.read().strip()
    return text


def updateString(inputString, position, numCharactersToRemove, stringToInsert):
  return inputString[:position] + stringToInsert + inputString[position + numCharactersToRemove:]

def searchKey(text, key):
  iterator = re.finditer(key, text)
  numItems = 0
  foundItem = 0
  
  for x in iterator:
    numItems += 1
    foundItem = x
    #print(x)

  if numItems == 0:
    return [False]
  
  if numItems == 1:
    return [True, foundItem]

  if numItems > 1:
    print("found more than one item")
    return [True, foundItem]


rootDir = "../"
#rootDir = "sandbox"
key = r"\\def\ *\\E.*bf"
keyConflict = r"\\def\ *\\E.*cal"
beforeConflict = r"\E"
afterConflict = r"\EE"

def isWordCharacter(char):
  return (
    char >= "a" and char <= "z" or
    char >= "A" and char <= "Z")
      

def updateIndexFile(indexFile):
  indexFileContentOriginal = getFileContent(indexFile)
  indexFileContent = indexFileContentOriginal
  position = 0
  while True:
    foundPosition = indexFileContent.find(beforeConflict, position)
    if foundPosition < 0:
      break

    position = foundPosition + 1
    nextChar = indexFileContent[foundPosition + len(beforeConflict)]
    if not isWordCharacter(nextChar):
      indexFileContent = updateString(indexFileContent, foundPosition, len(beforeConflict), afterConflict)
      position += (len(afterConflict) - len(beforeConflict))
      print(indexFile + " " + str(foundPosition))
  
  if not indexFileContent == indexFileContentOriginal:
    updateFileContent(indexFile, indexFileContent)
  

def updateIndexFileIfNecessary(texFile, indexFile):
  #print(texFile)
  texString = getFileContent(texFile)
  foundKey = searchKey(texString, key)
  foundKeyConflict = searchKey(texString, keyConflict)
  
  if foundKey[0] and foundKeyConflict[0]:
    raise Exception("Two conflict defs found")
  
  if foundKeyConflict[0]:
    print(foundKeyConflict[1])
    updateIndexFile(indexFile)

for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    if file.endswith("tex"):
      texFile = os.path.join(subdir, file)
      indexFile = os.path.join(subdir, "index.html")
      updateIndexFileIfNecessary(texFile, indexFile)

        
      
    


  
  
  
  
  
  
  
  
  
  
  
