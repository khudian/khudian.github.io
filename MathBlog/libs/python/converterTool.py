import os
import re
from pathlib import Path
from shutil import copyfile

gBlogDir = R"C:\Users\khuda\Desktop\Blog"
gDestinationDir = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog"
gTemplate = """
<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
  <link rel="stylesheet" type="text/css" href="../../../libs/mathBlogStyle.css">

  <script type="text/javascript" src="../../../libs/jquery_3.4.1.js"></script>
  <script type="text/javascript" src="../../../libs/menu.js"></script>
  <script type="text/javascript" src="../../../config.js"></script> 
  <script type="text/javascript" src="../../../libs/mathBlogBase.js"></script>
  <script type="text/javascript" src="../../../libs/mathBlogArticle.js"></script> 
  <script type="text/x-mathjax-config">
    configureMathJax();
  </script>
  <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>  
</head>

<body>
  <div id="menu"></div>

  <div class="mainText">
    <div class="article" date="PYTHON_DATE_KEY">
      PYTHON_MAIN_ARTICLE_KEY
    </div>
 </body>
</html>
"""

def monthStringToNumber(monthString):
  monthsMap = {'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr':4,
    'may':5,
    'jun':6,
    'jul':7,
    'aug':8,
    'sep':9,
    'oct':10,
    'nov':11,
    'dec':12}
  
  strippedString = monthString.strip()[:3].lower()
  try:
    out = monthsMap[strippedString]
    return out
  except:
    raise ValueError('Not a month')
        
        
def getMonthAndYear(subdir):
  splitted = os.path.split(subdir)
  month = splitted[1]
  year = os.path.split(splitted[0])[1]
  return [month, year]

def getMonthAndYearNum(month, year):
  return [monthStringToNumber(month), int(year)]

  
def validateMonthAndYear(month, year):
  return (year == 2019) and (month > 6) or (year > 2019) 

def cleverCopy(inFile, targetFile):
  targetFolder = os.path.split(targetFile)[0];
  if not os.path.exists(targetFolder):
    os.makedirs(targetFolder)
  copyfile(inFile, targetFile)  
  
def convert(inFile, targetFile):
  print("converting: " + inFile)
  print("destination:" + targetFile)
  cleverCopy(inFile, targetFile)
  print("")

def removeHeaderDefs(data):
  lastDef = R"\def\w {\omega}"
  foundIdx = data.find(lastDef)
  if foundIdx == -1:
    raise "invalid header"
   
  return data[foundIdx + len(lastDef):]
   
    
def eqnoToTag(data):
  data = re.sub(R"\\eqno.*\((.*)\)", r"\\tag{\1}", data)
  return data
  
     

def convertTexString(data):
  data = removeHeaderDefs(data)
  data = eqnoToTag(data)
  return data
  

def convert(pathFrom, pathTo):
  with open(pathFrom, 'r') as file:
    data = file.read();

  data = convertTexString(data)
  result = gTemplate.replace("PYTHON_DATE_KEY", "SDFDSF")
  result = result.replace("PYTHON_MAIN_ARTICLE_KEY", data)
  print(result)
  with open(pathTo, 'w') as file:
    file.write(result)  
    
def execute():
  for subdir, dirs, files in os.walk(gBlogDir):
    for file in files:
      if file.endswith("tex"):
        fullPath = os.path.join(subdir, file)
        [month, year] = getMonthAndYear(subdir)
        targetDir = os.path.join(gDestinationDir, year, month, Path(file).stem)
        targetFile = os.path.join(targetDir, 'index.html')
        [monthNum, yearNum] = getMonthAndYearNum(month, year)
        if (not os.path.exists(targetFile) and 
          validateMonthAndYear(monthNum, yearNum)):
          convert(fullPath, targetFile)

execute();
convert(R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog\2020\January20\9theorem\index.html",
        R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog\2020\January20\9theorem\index_covnertes.html")
          

