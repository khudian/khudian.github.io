var links =
[
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"],
  ["2019/May19/3symclairaut/index.html"]
]


function generateArticlesCode(link)
{
  var HTMLCode = '';
$.get( link, function( data ) {
  HTMLCode = data;
});  
 return HTMLCode;

}

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

function generateArticles()
{
  generateWrappers();
  for (var i in links)
  {
    $( "#"+i.toString()).load(links[i] + " div.article");
  }
  
}

$( document ).ready(function() 
{ 
  generateArticles();
}
);
