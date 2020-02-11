import os
from pathlib import Path

gBlogDir = R"C:\Users\khuda\Desktop\Blog"
gDestinationDir = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog"

print(gBlogDir)

def getMonthAndYear(subdir):
  splitted = os.path.split(subdir)
  month = splitted[1]
  year = os.path.split(splitted[0])[1]
  return [month, year]

for subdir, dirs, files in os.walk(gBlogDir):
  for file in files:
    if file.endswith("tex"):
      fullPath = os.path.join(subdir, file)
      [month, year] = getMonthAndYear(subdir)
      targetDir = os.path.join(gDestinationDir, year, month, Path(file).stem)
      targetFile = os.path.join(targetDir, 'index.html')
      if not os.path.exists(targetFile):
        print(targetFile)
        
      
