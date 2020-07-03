$(function() {
  console.log("hello world from client.js file");

  // if ($_POST["action"] == "Keywords") {
  //   $.get("/keywords", function(keywords) {
  //     keywords.forEach(function(keyword) {
  //       $("<li></li>")
  //         .text(keyword)
  //         .appendTo("ul#keywords");
  //     });
  //   });
  // } else if ($_POST["action"] == "Websites") {
  //   $.get("/websites", function(websites) {
  //     websites.forEach(function(website) {
  //       $("<li></li>")
  //         .text(website)
  //         .appendTo("ul#websites");
  //     });
  //   });
  // } else {
  //   //invalid action!
  // }
$.get('/keywords', function(keywords) {
    keywords.forEach(function(keyword) {
      $('<li></li>').text(keyword).appendTo('ul#keywords');
    });
  });


  $("form").submit(function(event) {
    event.preventDefault();
    keyword = $("input").val();

    // if ($_POST["action"] == "Keywords") {
      $.post("/keywords?" + $.param({ keyword: keyword }), function() {
        $("<li></li>")
          .text(keyword)
          .appendTo("ul#keywords");
        $("input").val("");
        $("input").focus();
      });
    // } else if ($_POST["action"] == "Websites") {
    //   $.post("/websites?" + $.param({ website: website }), function() {
    //     $("<li></li>")
    //       .text(website)
    //       .appendTo("ul#websites");
    //     $("input").val("");
    //     $("input").focus();
    //   });
    // } else {
    //   //invalid action!
    // }
  });
});
