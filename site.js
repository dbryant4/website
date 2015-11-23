$(document).ready(function() {
  $.get("resume.md", function(data){
    $("div.resume").html(marked(data));
  });
});
