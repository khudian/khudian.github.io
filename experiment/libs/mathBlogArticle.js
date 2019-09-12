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
  $("div.mainText").prepend('<br><br>');
  $("div.mainText").prepend(html);
  $("div.mainText").append('<br>');
  $("div.mainText").append(html);
  $("div.mainText").append('<br><br>');
}

$( document ).ready(function() 
{ 
  propogateDate();
  linkFootnotes();
  addLinkToMathBlog();
  }
);
