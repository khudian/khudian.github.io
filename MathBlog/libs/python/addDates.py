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

  
rootDir = "..\\..\\"
searchKey = 'class="article"'
def updateString(inputString, position, numCharactersToRemove, stringToInsert):
  return inputString[:position] + stringToInsert + inputString[position + numCharactersToRemove:]

def parseSubDir(subDir):
  splitted = subDir.split("\\")
  if not splitted[2].isdigit():
    return [False, 0, 0, 0]
  year = splitted[2]
  month = splitted[3]
  month = month[0:-2]
  day = splitted[4]
  day = day[0:2]
  if not day.isdigit():
    day = 0
  return [True, day, month, year]  
  
def generateDateString(day, month, year):
  date = ''
  if day == 0:
    date = str(month) + ' ' + str(year)
  else:
    date = str(int(day)) + ' ' + str(month) + ' ' + str(year)
  return date  
  
for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    if file.endswith("html"):
      [isParsed, day, month, year] = parseSubDir(subdir)
      if isParsed:
        dateString = generateDateString(day, month, year);
        print(dateString)
        filePath = os.path.join(subdir, file)
        content = getFileContent(filePath)
        position = content.find(searchKey)
        if position >= 0:
          content = (content[:position + len(searchKey)] + ' date="' +
          dateString + '"' + content[position + len(searchKey):])
          print(content)
          updateFileContent(filePath, content)
