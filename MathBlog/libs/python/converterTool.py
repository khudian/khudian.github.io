import os
from pathlib import Path

gBlogDir = R"C:\Users\khuda\Desktop\Blog"
gDestinationDir = R"C:\Users\khuda\Desktop\khudian.github.io\MathBlog"

print(gBlogDir)

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
        print(targetFile)
        
      
