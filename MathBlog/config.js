function configureMathJax()
{
  MathJax.Hub.Config({
  TeX: 
  {
    Macros: 
    {
      A: "{\\bf A}", 
      B: "{\\cal B}",
      C: "{\\bf C}",
      D: "{\\cal D}",
      CC: "{\\cal C}",
      Cl: "{\\tt \\hbox{Cliff}}",
      E: "{\\bf E}",
      EE: "{\\cal E}",
      F: "{\\cal F}",
      FF: "{\\cal F}",
      G: "\\Gamma",
      GG: "{\\cal G}",
      H: "{\\bf H}",
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
      bs: "{\\bf s}",
      c: "{\\bf c}",
      d: "\\delta",
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