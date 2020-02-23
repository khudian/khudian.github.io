import os
import re
from pathlib import Path
from shutil import copyfile

gBlogDir = R"C:\Users\khuda\Desktop\Blog"
gDestinationDir = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog"
gArticlesJsPath = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog\articles.js"
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
  
def getDayNum(file):
  oneDigit = file[0]
  twoDigits = file[0:2]
  if not oneDigit.isdigit():
    raise "File name does not contain any day information"
  
  if twoDigits.isdigit():
    return int(twoDigits)

  return int(oneDigit)    
  

  
def validateMonthAndYear(month, year):
  return (year == 2019) and (month > 6) or (year > 2019) 

def creatFileDirIfNotExist(file):
  folder = os.path.split(file)[0];
  if not os.path.exists(folder):
    os.makedirs(folder)

def removeHeaderDefs(data):
  lastDef = R"\def\w {\omega}"
  foundIdx = data.find(lastDef)
  if foundIdx == -1:
    print("WARNING: cannot find a header in the file")
    return data
   
  return data[foundIdx + len(lastDef):]
  
def removeAfterBye(data):
  byeString = R"\bye"
  foundIdx = data.find(byeString)
  if foundIdx == -1:
    print("WARNING: cannot find \bye command")
    return data
   
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
  if not fIdxMin in range(startIdx, startIdx + 2):
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

  print("startIdx", startIdx)
  print("opencloseStr", [openStr, closeStr])
  print("substring", data[startIdx: startIdx + 10])
  print("data", data)
  
  raise "the start and open keys are not canceling each other"
        
def getMinMax_inner(data, startIdx, openStr, closeStr):
  idx1 = startIdx - len(openStr)
  if (data.find(openStr, idx1) == idx1):
    return getMinMax(data, idx1, openStr, closeStr)

  idx1 -= 1
  if (data.find(openStr, idx1) == idx1):
    return getMinMax(data, idx1, openStr, closeStr)
  
  return
  
  
def replace(data, startIdx, minmax, keys, replacementPair):
  first = data[:startIdx]
  second = data[minmax[0] + len(keys[0]):minmax[1]]
  third = data[minmax[1] + len(keys[1]):]
  
  data = first + replacementPair[0] + GENERAL_BEGIN_KEY +\
    second + GENERAL_END_KEY + replacementPair[1] + third
    
  return data  
  
def replace_forInner(data, startIdx, minmax, keys, replacementPair):
  first = data[:minmax[0]]
  second = data[startIdx:minmax[1]]
  third = data[minmax[1] + len(keys[1]):]
  
  data = first + GENERAL_BEGIN_KEY + replacementPair[0] +\
    second  + replacementPair[1]  + GENERAL_END_KEY + third
  
  return data  
  

def chooseMinMaxAndKeys(minmaxParentheses, minmaxInternalKeys):
  minmax = None
  keys = None

  if minmaxParentheses != None:
    return [minmaxParentheses, 
      ["{", "}"]]
  
  if minmaxInternalKeys != None: 
    return [minmaxInternalKeys,
      [GENERAL_BEGIN_KEY, GENERAL_END_KEY]]
  
  raise R"cannot find open/close keys for the command"  
    

def replaceCommand_OverwhelmingType(
  data, commandString, 
  replacementPair):  
  
  while True:
    foundIdx = data.find(commandString)

    if foundIdx == -1:
      return data

    if checkCaretInsideFormula(data, foundIdx):
      raise "command is inside formula"
  
    minmaxParentheses = getMinMax(data, 
      foundIdx + len(commandString), "{", "}")  
    minmaxInternalKeys = getMinMax(data,
      foundIdx + len(commandString), GENERAL_BEGIN_KEY, GENERAL_END_KEY)  

    minmaxKeys = chooseMinMaxAndKeys(
      minmaxParentheses, minmaxInternalKeys)  
    data = replace(data, foundIdx, minmaxKeys[0],
      minmaxKeys[1], replacementPair)  
  
  
def replaceCommand_InnerType(
  data, commandString, 
  replacementPair):  
  
  while True:
    foundIdx = data.find(commandString)
    if foundIdx == -1:
      return data
    
    if checkCaretInsideFormula(data, foundIdx):
      raise "command is inside formula"
    
    minmaxParentheses = getMinMax_inner(data, foundIdx, "{", "}")  
    minmaxInternalKeys = getMinMax_inner(data, foundIdx,
      GENERAL_BEGIN_KEY, GENERAL_END_KEY)  
    
    [minmax, keys ] = chooseMinMaxAndKeys(
      minmaxParentheses, minmaxInternalKeys)  
      
    data = replace_forInner(data, foundIdx + len(commandString), 
      minmax, keys, replacementPair)  
  
    
   
def eqnoToTag(data):
  data = re.sub(R"\\eqno.*\((.*)\)", r"\\tag{\1}", data)
  return data
  
def skipsToBr(data):
  data = re.sub(R"\\medskip", r"<br><br>", data)
  data = re.sub(R"\\smallskip", r"<br><br>", data)
  data = re.sub(R"\\bigskip", r"<br><br><br>", data)
  data = re.sub(R"\n\n", r"<br><br>\n", data)
  return data

def removeInternalKeys(data):
  data = re.sub(R"GENERAL_BEGIN_KEY", "", data)
  data = re.sub(R"GENERAL_END_KEY", "", data)
  return data
     

def convertTexString(data):
  data = removeHeaderDefs(data)
  data = removeAfterBye(data)
  data = eqnoToTag(data)
  data = skipsToBr(data)
  data = replaceCommand_OverwhelmingType(
    data, R"\centerline", [R"<h3>", R"</h3>"])
  data = replaceCommand_InnerType(
    data, R"\bf", [R"<b>", R"</b>"])
  data = replaceCommand_InnerType(
    data, R"\it", [R"<i>", R"</i>"])
  data = replaceCommand_InnerType(
    data, R"\tt", [R"<tt>", R"</tt>"])
  data = removeInternalKeys(data)  
  return data
  

def convert(pathFrom, pathTo):
  print("pathFrom: ", pathFrom)
  print("pathTo: ", pathTo)
  with open(pathFrom, 'r', encoding="utf8") as file:
    data = file.read();

  data = convertTexString(data)
  result = gTemplate.replace("PYTHON_DATE_KEY", "SDFDSF")
  result = result.replace("PYTHON_MAIN_ARTICLE_KEY", data)
  creatFileDirIfNotExist(pathTo)
  with open(pathTo, 'w', encoding ="utf8") as file:
    file.write(result)

def generateLinksToInsert(targets):
  print("Adding links: ")
  targets.sort(reverse = True)
  result = ''
  for target in targets:
    targetStripped = target[3][len(gDestinationDir) + 1:]
    result += "\n  [\""  + targetStripped + "\"],"
    
  print(result)
  return result  
    
  
def addTargetsToArticlesJs(targets):
    
  data = ''
  with open(gArticlesJsPath, 'r', encoding ="utf8") as file:
    data = file.read();

  fIdx = data.find('[')
  if fIdx == -1:
    raise "Cannot find the first bracket"
  
  linksToInsert = generateLinksToInsert(targets)

  data = data[:fIdx + 1] + linksToInsert + data[fIdx + 1:]
  with open(gArticlesJsPath, 'w', encoding ="utf8") as file:
    file.write(data)
    
    
def execute():
  targets = []
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
          dayNum = getDayNum(file)
          convert(fullPath, targetFile)
          targets.append([yearNum, monthNum, dayNum, targetFile])          
  
  addTargetsToArticlesJs(targets)
  
execute();
          

