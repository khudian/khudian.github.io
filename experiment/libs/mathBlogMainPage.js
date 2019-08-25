function generateWrapper(id)
{
   var result = `
   <div id="`+id+`"></div><br>
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
  
  return 0;
}

function getMinMaxPageIds(pageId)
{
  const numArticlesPerPage = 5;
  var minArticleNumber = pageId * numArticlesPerPage;
  var maxArticleNumber = (pageId + 1) * numArticlesPerPage - 1;
  maxArticleNumber = Math.min(maxArticleNumber, links.length - 1);
  return [minArticleNumber, maxArticleNumber];
}

function isPageIdValid(pageId)
{
  [min, max] = getMinMaxPageIds(pageId);
  return (pageId >= 0) && (min <= max);
}

function generateNavigatinLink(pageId, caption)
{
  return `<a style="font-size:20px; color: black;" href="index.html?page=` + pageId + `">` + 
  caption + `</a> `;
}
function generateNavigationLinks()
{
  var currentPageId = getPageId();
  var prevPageId = currentPageId - 1;
  var nextPageId = currentPageId + 1;
  result = "";
  if (isPageIdValid(prevPageId))
  {
    result += generateNavigatinLink(prevPageId, "Prev");
  }
  result += `&nbsp&nbsp`;
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
  [minArticleNumber, maxArticleNumber] = getMinMaxPageIds(pageId);
  htmlCode += generateNavigationLinks()
  for (var i = minArticleNumber; i <= maxArticleNumber; i++)
  {
    htmlCode += generateWrapper(i);
  }
  htmlCode += generateNavigationLinks()
  
  $("#articles").html(htmlCode);
}

function loadArticle(i, link)
{
  var idRef = "#"+i.toString();
  $(idRef).load(link + " div.article", 
  function() 
  {
    articleObject = $(idRef).find("div.article");
    titleHTML = `<a style="float: right; color: black;" href="`+ link +`">link</a>`;
    articleHtml = articleObject.html();
    articleHtml = titleHTML + articleHtml;
    articleObject.html(articleHtml);
    linkFootnotes();
    MathJax.Hub.Queue(["Typeset",MathJax.Hub]); //update MathJax
  });
}

function generateArticles()
{
  generateWrappers();
  var pageId = getPageId();
  [minArticleNumber, maxArticleNumber] = getMinMaxPageIds(pageId);
  
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
