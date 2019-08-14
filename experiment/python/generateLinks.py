import os
import shutil


rootDir = "../"
srcPath = "index.html"

allPaths = []
for subdir, dirs, files in os.walk(rootDir):
  for file in files:
    if file == "index.html":
      allPaths.append('["' + subdir+'/index.html"],')

for str in reversed(allPaths):
  print(str)
      


    
  
  
  
