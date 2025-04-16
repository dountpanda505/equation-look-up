function refreshIframe() {
  var ifr = document.getElementsByName('python')[0];
  ifr.src = ifr.src;
}




function refresh() {
  var ifr_t1 = document.getElementsByName('two')[0];
  var ifr_t2 = document.getElementsByName('one')[0];
  ifr_t1.src = ifr_t1.src;
  ifr_t2.src = ifr_t2.src;
}




function myFunction() {
  var one = document.getElementById("one");
  var two = document.getElementById("two");

  if (one.style.display === "none") {
    one.style.display = "block";
    two.style.display = "none";
  } else {
    one.style.display = "none";
    two.style.display = "block";
  }
}