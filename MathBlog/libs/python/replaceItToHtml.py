import io
import shutil
import os
import codecs
    
  
def updateFileContent(file, text):
  #print("file: " + file)
  #print("text: " + text)
  with open(file, 'w', encoding='utf8') as f:
    f.write(text)

def getFileContent(file):
  with open(file, encoding='utf8') as f:
    text = f.read().strip()
    return text

def searchCloseKey(fileContent, openKey, closeKey, startPosition):
  sum = 0
  for idx in range(startPosition, len(fileContent)):
    if (fileContent[idx]==openKey):
      sum += 1
    if (fileContent[idx]==closeKey):
      sum -= 1
    if (sum == -1):
      return idx
  
  print("Cannot find close idx")  
    
      
  
rootDir = "../"
searchKey = "\it"

def updateString(inputString, position, numCharactersToRemove, stringToInsert):
  return inputString[:position] + stringToInsert + inputString[position + numCharactersToRemove:]

def convertToHTMLStyle(fileContent, searchStartIdx):
  openKeyIdx = fileContent.find(searchKey, searchStartIdx)
  result = fileContent
  nextIdxToStart = len(fileContent)

  if (openKeyIdx >= 0):
    print (openKeyIdx)
    closeKeyIdx = searchCloseKey(fileContent, "{", "}", openKeyIdx)
    print (searchCloseKey(fileContent, "{", "}", openKeyIdx))
    result = updateString(fileContent, closeKeyIdx, 1, "</i>")
    if result[openKeyIdx - 1] != "{":
      print("Error: expect { before \it")
    result = updateString(result, openKeyIdx - 1, 4, "<i>")
    nextIdxToStart = closeKeyIdx + (4 + 3 - 1 - 4)
  
  return [nextIdxToStart, result]

for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    if file.endswith("html"):
      filePath = os.path.join(subdir, file)
      print(filePath)
      fileContent = getFileContent(filePath)
      converted = "";
      startIdx = 0;
      needToUpdateFlag = False;
      while True:
        [startIdx, converted] = convertToHTMLStyle(fileContent, startIdx)
        if converted == fileContent:
          break
        fileContent = converted
        needToUpdateFlag = True;
      
      #print(fileContent)     
      if needToUpdateFlag:
        updateFileContent(filePath, fileContent)      
        
        
      
    


  
  
  
  
  
  
  
  
  
  
  
