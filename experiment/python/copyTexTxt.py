import os
import shutil


rootDir = "../"
srcPath = "index.html"

for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    filePath = os.path.join(subdir, file)
    extension = os.path.splitext(filePath)[1]
    if (extension == ".tex"):
      targetPath = os.path.splitext(filePath)[0] + "_converted.txt";
      print(targetPath)
      shutil.copyfile(filePath, targetPath)

      


    
  
  
  
