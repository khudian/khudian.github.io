function generateWrapper(id)
{
   var result = `
   <div id="`+id+`">
   <div class="article">
     Loading...
   </div>
   </div><br>
   `
   return result;
}

function getPageId()
{
  var url = window.location.toString();
  var urlSplitted = url.split('=');
  if (urlSplitted.length > 1)
  {
    var pageId = parseInt(urlSplitted[1]);
    if (!isNaN(pageId))
    {
     return pageId;
    }
  }
  
  return 1;
}

function getMinMaxArticleIds(pageId)
{
  const numArticlesPerPage = 5;
  var minArticleNumber = (pageId - 1) * numArticlesPerPage;
  var maxArticleNumber = pageId * numArticlesPerPage - 1;
  maxArticleNumber = Math.min(maxArticleNumber, links.length - 1);
  return [minArticleNumber, maxArticleNumber];
}

function isPageIdValid(pageId)
{
  [min, max] = getMinMaxArticleIds(pageId);
  return (pageId >= 1) && (min <= max);
}

function generateNavigatinLink(pageId, name)
{
  return `
  <div class="`+ name + `">
    <a class="navigation" href="index.html?page=` + pageId + `">` + 
    name + `</a> 
  </div>
  `;
}
function generateNavigationLinks()
{
  var currentPageId = getPageId();
  var prevPageId = currentPageId - 1;
  var nextPageId = currentPageId + 1;
  result = "";
  if (!isPageIdValid(currentPageId))
  {
    return result;
  }

  if (isPageIdValid(prevPageId))
  {
    result += generateNavigatinLink(prevPageId, "Prev");
    result += `&nbsp&nbsp`;
  }
  if (isPageIdValid(nextPageId))
  {
    result += generateNavigatinLink(nextPageId, "Next");
  }
  result += `<br><br>`
  return result;
}


function generateWrappers()
{
  var htmlCode = "";
  var pageId = getPageId();
  
  if (!isPageIdValid(pageId))
  {
    return;
  }
  
  [minArticleNumber, maxArticleNumber] = getMinMaxArticleIds(pageId);
  htmlCode += generateNavigationLinks()
  for (var i = minArticleNumber; i <= maxArticleNumber; i++)
  {
    htmlCode += generateWrapper(i);
    if (i < maxArticleNumber)
    {
      htmlCode += `<br><br>`;
    }      
  }
  htmlCode += generateNavigationLinks()
  
  $("#articles").html(htmlCode);
}

function getArticleLinkHTML(link)
{
  return `
  <div class="articleLink">
    <a class="articleLink" href="`+ link +`">link</a>
  </div>  
    `
}

function loadArticle(i, link)
{
  var idRef = "#"+i.toString();
  $(idRef).load(link + " div.article", 
  function() 
  {
    articleObject = $(idRef).find("div.article");
    htmlDate = getArticleDateHTML(idRef)
    articleObject.prepend(html);

    htmlLink = getArticleLinkHTML(link);
    articleObject.prepend(htmlLink);
    linkFootnotes();
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]); //update MathJax
  });
}

function generateArticles()
{
  generateWrappers();
  var pageId = getPageId();
  [minArticleNumber, maxArticleNumber] = getMinMaxArticleIds(pageId);
  
  for (var i = minArticleNumber; i <= maxArticleNumber; i++)
  {
    loadArticle(i, links[i]);
  }

  
}

$( document ).ready(function() 
{ 
  generateArticles();
}
);
