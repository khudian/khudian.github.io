function propogateDate()
{
  html = getArticleDateHTML('')
  $('div.article').prepend(html);
}

function addLinkToMathBlog()
{
  html = `<div class="mathBlogButton">
    <a class="mathBlogButton" href="../../../index.html">Math Blog</a>
  </div>`
  $("div.mainText").prepend(html);
  $("div.mainText").append(html);
}

$( document ).ready(function() 
{ 
  propogateDate();
  linkFootnotes();
  addLinkToMathBlog();
  }
);
