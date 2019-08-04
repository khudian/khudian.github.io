var links =
[
  ["2019/May19/3symclairaut/index.html"]
]


function generateArticlesCode(link)
{
  var HTMLCode = '';
  //alert(link);
$.get( link, function( data ) {
  HTMLCode = data;
  alert(data)
});  
 return HTMLCode;

}

function generateArticles()
{
  var htmlCode = "";
  for (var i in links)
  {
    htmlCode += generateArticlesCode(
      links[i][0]);
  }
  $("#articles").html(htmlCode);
}

$( document ).ready(function() 
{ 
  generateArticles();
}
);
