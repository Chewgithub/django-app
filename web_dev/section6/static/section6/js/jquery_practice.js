

$("button").text("Hello");
$("button").html("<em>Hello</em>");

$("a").attr("href","https://bing.com");

$(document).keydown(function (e) { 
    $("h1").text(e.key);
    console.log(e.key);
});