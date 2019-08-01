var links =
[
  ["Symmetries of Clairaut equation", "2019/May19/3symclairaut/index.html"]
]

  
  function populateCSSSettings()
  {
    maxWidth = 800;
    stretchingCoeff = 0.9;

    var width = $(window).width();
    
    if (width > maxWidth)
    {
      var textWidth = maxWidth * stretchingCoeff;
      var padding = (width - textWidth) / 2
      $(".mainText").css('width', textWidth);
      $(".mainText").css('padding-left', padding);
      }
    else
    {
      stretchingCoeffPercent = (stretchingCoeff * 100).toString()+ '%';
      paddingPercent = ((1 - stretchingCoeff) / 2 * 100).toString()+ '%';
      $(".mainText").css('width', stretchingCoeffPercent);
      $(".mainText").css('padding-left', paddingPercent);
    }
  }   

  function generateArticlesCode(link, name, imageLink)
  {
    var HTMLCode = `
    <a class="panel" href="` + link + `/">
      <div class="panel">
        <div class="panelText">` + 
          name +
       `</div>
        <div class="panelImg">
          <img class="panel" src="` + imageLink + `">` +
       `</div>
     </div>
    </a>
    `
    
    return HTMLCode;

  }
  
  function generateArticles()
  {
    var htmlCode = "";
    for (var i in links)
    {
      htmlCode += generateArticlesCode(
        links[i][0], links[i][1], links[i][0]+'/main_thumbnail.jpg');
    }
    alert(htmlCode);
    //$("#panels").html(htmlCode);
  }

  
  $( document ).ready(function() 
  { 
    populateCSSSettings();
    //generateArticles();
  }
  );
  
    $( window ).resize(function() 
  {
    populateCSSSettings();
  });