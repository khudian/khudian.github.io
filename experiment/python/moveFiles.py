import os

rootDir = "../"

def collectHtmlFiles():
  results = []
  for subdir, dirs, files in os.walk(rootDir):
    for file in files:
      extension = os.path.splitext(file)[1]
      if (extension == ".tex"):
        fullPath = os.path.join(subdir, file)
        results.append(fullPath)
  return results
      
allFiles = collectHtmlFiles()
for file in allFiles:
  dirPath = os.path.dirname(file)
  fullFileName = os.path.basename(file)
  fileName = os.path.splitext(fullFileName)[0]
  newDirPath = os.path.join(dirPath, fileName)
  pdfFileName = os.path.join(dirPath, fileName + ".tex")
  if os.path.exists(pdfFileName):
    newPdFFileName = os.path.join(newDirPath, fileName + ".tex")
    os.rename(pdfFileName, newPdFFileName)
    print(newPdFFileName)
  else:
    print("Doesn't exist")
  
  
      