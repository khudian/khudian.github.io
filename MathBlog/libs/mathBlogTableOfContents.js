
function populateTableOfContents()
{
  htmlCode = '';
  mathBlogLink = `<div class="mathBlogButton">
    <a class="mathBlogButton" href="index.html">Math Blog</a>
  </div><br><br>`;

  htmlCode += mathBlogLink;

  for (i = 0; i < links.length; i++)
  {
    htmlCode += `<a href=` + links[i][0] + `>` + links[i][1] + '</a> ' + links[i][2] + `<br><br>`;
  }
  htmlCode +=mathBlogLink;

  $("#tableOfContents").html(htmlCode);
  
}


$( document ).ready(function() 
{ 
  populateTableOfContents();
}
);
