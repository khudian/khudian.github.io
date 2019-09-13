import os
import shutil


rootDir = "../"
srcPath = "index.html"

for subdir, dirs, files in os.walk(rootDir):
  targetPath = os.path.join(subdir, "index.html")
  print(targetPath)
  if not os.path.exists(targetPath):
    shutil.copyfile(srcPath, targetPath)

    
  
  
  
