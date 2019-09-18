  $( document ).ready(function() 
  {
    var string = '<div align ="center"><font color="red" size="6"> <b> Hovhannes M. Khudaverdian </b></font></div>';
    string += '<p align="center">';
    string += '  <small>';
    string += '    <a href="http://khudian.net/index.html">Main page</a>';
    string += '    <a href="http://khudian.net/Research/temp.html">Research</a>';
    string += '    <a href="http://khudian.net/Teaching/teaching.html">Teaching</a>';
    string += '    <a href="http://khudian.net/Lectures/lectures.html">Lectures</a>';
    string += '    <a href="http://khudian.net/Etudes/etudes.html">&Eacute;tudes</a>';
    string += '    <a href="http://khudian.net/MathBlog/index.html">Math Blog</a>';
    string += '  </small>';
    string += '</p>';
    string += '<hr>';

    document.getElementById("menu").innerHTML = string;

  }
  );


