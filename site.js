$(document).ready(function() {
  $.get("resume.md", function(data){
    $("div.resume").html(marked(data));
  })
  .fail(function(jqXHR, textStatus, errorThrown){
    $("div.resume").html("Although the resume is not loading, you can still download a PDF version by using the Download button.");
  });
});
