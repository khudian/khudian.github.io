function configureMathJax()
{
  MathJax.Hub.Config({
  TeX: 
  {
    Macros: 
    {
      p: "\\partial",
      t: "\\tilde",
      a: "\\alpha",
      x: "{\\bf x}",
      X: "{\\bf X}",
      y: "{\\bf y}",
      v: "{\\bf v}",
      f: "{\\bf f}",
      g: "{\\bf g}",
      vare: "\\varepsilon",
      grad: "{\\rm grad\\,}",
      w: "\\omega",
      A: "{\\bf A}",
      Cl: "{\\tt \\hbox{Cliff}}",
      E: "{\\bf E}",
      e: "{\\bf e}",
      tS: "{\\tilde \\Sigma}"
    }    
  },
  tex2jax: 
  {
    inlineMath: 
    [ 
      ['$','$'] 
    ]
  }
  });
}

  
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



$( document ).ready(function() 
{ 
  populateCSSSettings();
}
);

$( window ).resize(function() 
{
  populateCSSSettings();
});