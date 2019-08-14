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
searchKey = r'<h2 class="title" date=""></h2>'

for subdir, dirs, files in os.walk(rootDir):
  txtFilePath = findFileFirstLevel(subdir, 'converted.txt')
  indexFilePath = findFileFirstLevel(subdir, 'index.html')
  if txtFilePath != "" and indexFilePath != "":
    indexFileContent = getFileContent(indexFilePath)
    txtFileContent = getFileContent(txtFilePath)
    position = indexFileContent.find(searchKey)
    position+=len(searchKey)
    result = indexFileContent[:position] + '\n' + txtFileContent  + '\n'  + indexFileContent[position:]
    updateFileContent(indexFilePath, result)
  else:
    print("cannot find files in " + subdir)

    
    
    


#  dirs = next(os.walk(rootDir))[1]
#for dir in dirs:
#  dir = os.path.join(rootDir, dir)
#  convertedTXT = findFileByName(dir, "converted.txt")
#  indexHTML = findFileByName(dir, "index.html")
#  if indexHTML !="" and convertedTXT != "":
#    indexHTMLContent = getFileContent(indexHTML)
#    convertedTXTContent = getFileContent(convertedTXT)
#    position = indexHTMLContent.find(searchKey)
#    position += len(searchKey)
#    result = indexHTMLContent[:position] + '\n' + convertedTXTContent  + '\n'  + indexHTMLContent[position:]
#    updateFileContent(indexHTML, result)
#  else:
#    print("cannot find files in " + dir)

  
  
  
  
  
  
  
  
  
  
  
