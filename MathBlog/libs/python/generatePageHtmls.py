import io
import shutil
import os
import codecs
    
def getPageContent(i):
  strBegin = """<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
  <link rel="stylesheet" type="text/css" href="../mathBlogStyle.css">

  <script type="text/javascript" src="../jquery_3.4.1.js"></script>
  <script type="text/javascript" src="../menu.js"></script> 
  <script type="text/javascript" src="../mathBlogMain.js"></script> 
  <script type="text/javascript" src="../mathBlogArticles.js"></script> 
  <script type="text/x-mathjax-config">
    configureMathJax();
  </script>
  <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>  
</head>

<body>
  <div id="menu"></div>
  <div class="mainText">
    <div id="articles" pageId=\""""
  
  strEnd ="""\">
    </div>       
  </div>

 </body>

</html>"""
  return strBegin + str(i) + strEnd
  
def updateFileContent(file, text):
  #print("file: " + file)
  #print("text: " + text)
  with open(file, 'w', encoding='utf8') as f:
    f.write(text)

  


rootDir = "../pages"
for i in range(50, 101):
  print(i)
  updateFileContent(rootDir + "/page"+str(i)+".html", getPageContent(i))

  
  
  
  
  
  
  
  
  
  
  
