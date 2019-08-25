function populateCSSSettings()
{
  maxWidth = 800;
  stretchingCoeff = 0.97;

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

function linkFootnotes()
{
  $('.footnote-head').unbind()

  $('.footnote-head').click(function(){
      $(this).next().slideToggle('normal');
  })
  $('.footnote-body').hide();
}

$( document ).ready(function() 
{ 
  populateCSSSettings();
}
);

$( window ).resize(function() 
{
  populateCSSSettings();
});

