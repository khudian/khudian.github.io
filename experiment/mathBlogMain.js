function configureMathJax()
{
  MathJax.Hub.Config({
  TeX: 
  {
    Macros: 
    {
      A: "{\\bf A}",
      C: "{\\bf C}",
      Cl: "{\\tt \\hbox{Cliff}}",
      E: "{\\bf E}",
      FF: "{\\cal F}",
      L: "{\\cal L}",
      R: "{\\bf R}",
      SS: "{\\cal S}",
      X: "{\\bf X}",
      XX: "{\\cal X}",

      a: "\\alpha",
      e: "{\\bf e}",
      f: "{\\bf f}",
      g: "{\\bf g}",
      grad: "{\\rm grad\\,}",
      p: "\\partial",
      pt: "{\\bf pt}",
      t: "\\tilde",
      tS: "{\\tilde \\Sigma}",
      s: "\\sigma",
      v: "{\\bf v}",
      vare: "\\varepsilon",
      x: "{\\bf x}",
      y: "{\\bf y}",
      w: "\\omega"
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