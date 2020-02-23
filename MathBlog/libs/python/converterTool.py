import os
import re
from pathlib import Path
from shutil import copyfile

gBlogDir = R"C:\Users\khuda\Desktop\Blog"
gDestinationDir = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog"
GENERAL_BEGIN_KEY = "GENERAL_BEGIN_KEY"
GENERAL_END_KEY = "GENERAL_END_KEY"
gTemplate = """<!DOCTYPE html>
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
  
def removeAfterBye(data):
  byeString = R"\bye"
  foundIdx = data.find(byeString)
  if foundIdx == -1:
    raise "cannot find \bye command"
   
  return data[:foundIdx]
  
def checkCaretInsideFormula(data, caretIdx):
  result = False
  dataStripped = data[:caretIdx + 1]
  currentIdx = 0;
  while (True):
    fIdx1 = dataStripped.find("$", currentIdx)
    fIdx2 = dataStripped.find("$$", currentIdx)

    if (fIdx1 == -1) and (fIdx2 == -1):
      return result
    
    if (fIdx1 == fIdx2):
      currentIdx = fIdx1 + 2 
    else:
      currentIdx = fIdx1 + 1 
      
    result = not result    

def getMinMax(data, startIdx, openStr, closeStr):
  fIdxMin = data.find(openStr, startIdx)
  if (fIdxMin - startIdx) < 2:
    return
  
  sum = 1
  fIdx = fIdxMin + 1
  while fIdx < len(data):
    if (data.find(openStr, fIdx) == fIdx):
      sum += 1
    if (data.find(closeStr, fIdx) == fIdx):
      sum -= 1
      
    if sum == 0:
      return [fIdxMin, fIdx]
    
    fIdx += 1
  
  raise "the start and open keys are not canceling each other"
        
    
  
def replace(data, startIdx, minmax, keys, replacementPair):
  first = data[:startIdx]
  second = data[minmax[0] + len(keys[0]):minmax[1]]
  third = data[minmax[1] + len(keys[1]):]
  
  data = first + replacementPair[0] + GENERAL_BEGIN_KEY +\
    second + GENERAL_END_KEY + replacementPair[1] + third
    
  return data  

def replaceCommand_OverwhelmingType(
  data, commandString, 
  replacementPair):  
  
  foundIdx = data.find(commandString)
  if checkCaretInsideFormula(data, foundIdx):
    raise "command is inside formula"

  minmaxParentheses = getMinMax(data, foundIdx, "{", "}")  
  minmaxInternalKeys = getMinMax(data, foundIdx,
    GENERAL_BEGIN_KEY, GENERAL_END_KEY)  
  
  minmax = None
  keys = None

  if minmaxParentheses != None:
    minmax = minmaxParentheses
    keys = ["{", "}"]    
  
  if minmaxInternalKeys != None and \
    minmaxParentheses != None and \
    minmaxInternalKeys[0] < minmaxParentheses[0]:
    minmax = minmaxInternalKeys
    keys = [GENERAL_BEGIN_KEY, GENERAL_END_KEY]
  
  if minmax == None:
    raise "cannot find open/close keys for the command"  
    
  data = replace(data, foundIdx, minmax, keys, replacementPair)  
  return data
    
   
def eqnoToTag(data):
  data = re.sub(R"\\eqno.*\((.*)\)", r"\\tag{\1}", data)
  return data
  
     

def convertTexString(data):
  data = removeHeaderDefs(data)
  data = removeAfterBye(data)
  data = eqnoToTag(data)
  data = replaceCommand_OverwhelmingType(
    data, R"\centerline", [R"<h3>", R"</h3>"])
  return data
  

def convert(pathFrom, pathTo):
  with open(pathFrom, 'r') as file:
    data = file.read();

  data = convertTexString(data)
  result = gTemplate.replace("PYTHON_DATE_KEY", "SDFDSF")
  result = result.replace("PYTHON_MAIN_ARTICLE_KEY", data)
  with open(pathTo, 'w') as file:
    file.write(result)
  print(result)
    
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
          

