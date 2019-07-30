  $( document ).ready(function() 
  {
    var string = '<div align ="center"><font color="red" size="6"> <b> Hovhannes M. Khudaverdian </b></font></div>';
    string += '<p align="center">';
    string += '  <small>';
    string += '    <a href="http://khudian.net/index.html" target="main">Main page</a>';
    string += '    <a href="http://khudian.net/experiment/index.html" target="main">Math blog</a>';
    string += '    <a href="http://khudian.net/Research/temp.html" target="main">Research</a>';
    string += '    <a href="http://khudian.net/Teaching/teaching.html" target="main">Teaching</a>';
    string += '    <a href="http://khudian.net/Lectures/lectures.html" target="main">Lectures</a>';
    string += '    <a href="http://khudian.net/Etudes/etudes.html" target="main">&Eacute;tudes</a>';
    string += '  </small>';
    string += '</p>';
    string += '<hr>';

    //$("#menu").html(string);

    document.getElementById("menu").innerHTML = string;
  }
  );
