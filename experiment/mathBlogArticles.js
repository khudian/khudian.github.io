var links =
[
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"]
]



function generateWrapper(id)
{
   var result = `
   <div id="`+id+`"></div><br>
   `
   return result;
}

function generateWrappers()
{
  var htmlCode = "";
  for (var i in links)
  {
    htmlCode += generateWrapper(i);
  }
  
  $("#articles").html(htmlCode);
}

function loadArticle(i)
{
  var idRef = "#"+i.toString();
  $(idRef).load(links[i] + " div.article", 
  function() 
  {
    var titleObject = $(idRef).find("h2");
    var titleHTML = titleObject.html();
    titleHTML = `<a href="`+ links[i] +`">` + titleHTML + `</a>`;
    titleObject.html(titleHTML);
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]); //update MathJax
  });
}

function generateArticles()
{
  generateWrappers();
  for (var i in links)
  {
    loadArticle(i);
  }

  
}

$( document ).ready(function() 
{ 
  generateArticles();
}
);
