import os
import re
from pathlib import Path
from shutil import copyfile

gMainDir = R"C:\work\Nado\Disser\February\test"

   
def checkContainsRussian(word):
  for idx in range(0, len(word)):
    charOrd = ord(word[idx])
    if (charOrd >= 1040) and (charOrd <= 1103):
      return True
  
  return False  
  
def findNextBasicFormula(data, startIdx):
  fIdx = data.find('$', startIdx)
  if fIdx == -1:
    return [fIdx, '']
  
  if (data[fIdx + 1] != '$'):
    fCloseIdx = data.find('$', fIdx + 1)
    if fCloseIdx == -1:
      raise "Unexpected: can't find formula end for one"

    return [fCloseIdx + 1, data[fIdx + 1 : fCloseIdx]]
  elif (data[fIdx + 1] == '$'):
    fCloseIdx = data.find('$$', fIdx + 1)
    if fCloseIdx == -1:
      raise "Unexpected: can't find formula end for two"

    return [fCloseIdx + 2, data[fIdx + 2 : fCloseIdx]]
    
def findNextFormula(data, startIdx):
  fIdx = data.find(R'\begin{equation}', startIdx)
  if fIdx == -1:
    return [fIdx, '']
  
  fCloseIdx = data.find(R'\end{equation}', fIdx + 1)
  if fCloseIdx == -1:
    raise "Unexpected: can't find formula end for one"

  return [fCloseIdx + 1, data[fIdx + 16: fCloseIdx]]
    
    
  
def findBadFormulas(path):
  print("path: ", path)
  with open(path, 'r', encoding="utf8") as file:
    data = file.read();
  
  result = [0, ''];
  print("formulas: with one and two dollars:")
  while (result[0] != -1):
    result = findNextBasicFormula(data, result[0])
    if(checkContainsRussian(result[1])):
      print(result)  

  print("Normal formulas: begin/end equation:")
  result = [0, ''];
  while (result[0] != -1):
    result = findNextFormula(data, result[0])
    if(checkContainsRussian(result[1])):
      print(result)  

  return   
  
  
    
def execute():
  targets = []
  for subdir, dirs, files in os.walk(gMainDir):
    for file in files:
      if file.endswith("tex"):
        fullPath = os.path.join(subdir, file)
        findBadFormulas(fullPath)
        print('')
        print('')

  print('')
  print('')
  print('')
  print('')
  
  
execute();

          

