$(document).ready(function(){
  $('#mode').click(function(){
  if($('link#styles').attr('href')=="assets/css/style.css"){
  $('#mode').attr('value','Switch To Day Mode')
  $('link#styles').attr('href','assets/css/darkmodestyle.css')
  }
  else
  {
  $('#mode').attr('value','Switch To Night Mode')
  $('link#styles').attr('href','assets/css/style.css')
  }
  })
  
  });