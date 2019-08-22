function configureMathJax()
{
  MathJax.Hub.Config({
  TeX: 
  {
    Macros: 
    {
      A: "{\\bf A}", 
      C: "{\\bf C}",
      CC: "{\\cal C}",
      Cl: "{\\tt \\hbox{Cliff}}",
      E: "{\\bf E}",
      EE: "{\\cal E}",
      FF: "{\\cal F}",
      G: "\\Gamma",
      GG: "{\\cal G}",
      K: "{\\bf K}",
      L: "{\\cal L}",
      M: "{\\cal M}",
      N: "{\\bf N}",
      R: "{\\bf R}",
      Sb: "{\\bf S}",
      SS: "{\\cal S}",
      Tr: "{\\rm Tr\\,}",
      V: "{\\cal V}",
      X: "{\\bf X}",
      XX: "{\\cal X}",
      Y: "{\\bf Y}",
      Z: "{\\bf Z}",

      a: "\\alpha",
      ac: "{\\bf a}",
      b: "{\\bf b}",
      dist: "{\\tt \\hbox{distance}}",
      e: "{\\bf e}",
      f: "{\\bf f}",
      finish: "\\blacksquare",
      g: "{\\bf g}",
      grad: "{\\rm grad\\,}",
      h: "\\hbar",
      k: "{\\bf k}",
      l: "{\\bf l}",
      m: "{\\bf m}",
      n: "{\\bf n}",
      p: "\\partial",
      pb: "{\\bf p}",
      pt: "{\\bf pt}",
      q: "{\\bf q}",
      r: "{\\bf r}",
      s: "\\sigma",
      t: "{\\bf t}",
      tS: "{\\tilde \\Sigma}",
      td: "\\tilde",
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