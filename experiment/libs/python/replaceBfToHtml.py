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
searchKey = r"\bf"

def updateString(inputString, position, numCharactersToRemove, stringToInsert):
  return inputString[:position] + stringToInsert + inputString[position + numCharactersToRemove:]

def convertToHTMLStyle(fileContent, searchStartIdx):
  openKeyIdx = fileContent.find(searchKey, searchStartIdx)
  result = fileContent
  newIdx = searchStartIdx

  if (openKeyIdx >= 0):
    closeKeyIdx = searchCloseKey(fileContent, "{", "}", openKeyIdx)
    if (result[openKeyIdx - 11:openKeyIdx-1] == "centerline"):
      result = updateString(result, openKeyIdx, 3, "")
      newIdx = idx - 3
      return [result, newIdx]
      

    result = updateString(fileContent, closeKeyIdx, 1, "</b>")
    if result[openKeyIdx - 1] != "{":
      print("Error: expect { before \bf")
      return 123
    result = updateString(result, openKeyIdx - 1, 4, "<b>")
    newIdx = idx + 4 + 3 - 4 - 1
  
  return [result, newIdx]
  
def isDollar(fileContent, idx):
  if idx < len(fileContent) - 1:
    return (fileContent[idx] == "$" and fileContent[idx + 1] != "$" and
      fileContent[idx - 1] != "$")
  if idx == len(fileContent) - 1:
    return fileContent[idx] == "$" and fileContent[idx - 1] != "$"

def isDoubleDollar(fileContent, idx):
  if idx < len(fileContent) - 1:
    return fileContent[idx] == "$" and fileContent[idx + 1] == "$"
  if idx == len(fileContent) - 1:
    return False
    
def isOnKey(fileContent, idx, searchKey):
  if idx + len(searchKey) > len(fileContent):
    return False
  else:
    res = True
    for i in range(0, len(searchKey)):
      res = res and fileContent[idx + i] == searchKey[i]
    return res   
    

for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    if file.endswith("html"):
      filePath = os.path.join(subdir, file)
      print(filePath)
      fileContent = getFileContent(filePath)
      idx = 0
      isInDoubleDollar = False;
      isInDollar = False;

      while (idx < len(fileContent)):
        if isDollar(fileContent, idx):
          isInDollar = not isInDollar

        if isDoubleDollar(fileContent, idx):
          isInDoubleDollar = not isInDoubleDollar
        
        if not isInDollar and not isInDoubleDollar and isOnKey(fileContent, idx, searchKey):
          [fileContent,idx] = convertToHTMLStyle(fileContent, idx)
        idx+=1
      
      updateFileContent(filePath, fileContent)      
        
        
      
    


  
  
  
  
  
  
  
  
  
  
  
