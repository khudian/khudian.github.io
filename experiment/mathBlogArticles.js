var links =
[
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
  htmlCode += generateWrapper(5);
  htmlCode += generateWrapper(6);
  htmlCode += generateWrapper(7);
  $("#articles").html(htmlCode);
}

function generateArticles()
{
  generateWrappers();
  $( "#5" ).load("2019/May19/3symclairaut/index.html div.mainText" );
}

$( document ).ready(function() 
{ 
  generateArticles();
}
);
