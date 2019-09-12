import io
import shutil
import os
import codecs

  
def findFileFirstLevel(dir, extension):
  files = next(os.walk(dir))[2]
  for file in files:
    if file.endswith(extension):
      return os.path.join(dir, file);
  return ''
  

def getFileContent(file):
  with open(file, encoding='utf8') as f:
    text = f.read().strip()
    return text
    
def updateFileContent(file, text):
  print("file: " + file)
  print("text: " + text)
  with open(file, 'w', encoding='utf8') as f:
    f.write(text)

  

  
rootDir = "../"
searchKey = r"\bye"
searchKeyDiv = r"</div>"

for subdir, dirs, files in os.walk(rootDir):
  indexFilePath = findFileFirstLevel(subdir, 'index.html')
  if indexFilePath != "":
    indexFileContent = getFileContent(indexFilePath)
    position = indexFileContent.find(searchKey)
    if position != -1:
      print(position)
      positionDiv = indexFileContent.find(searchKeyDiv, position)
      if positionDiv != -1:
        result = indexFileContent[:position] + indexFileContent[positionDiv:]
        updateFileContent(indexFilePath, result)
  else:
    print("cannot find files in " + subdir)

    
    