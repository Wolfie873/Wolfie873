window.onload = function () {};
var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;

function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
function scrolling() {
  document.getElementById("div_top").scrollIntoView({ behavior: "smooth" });
}
function viewer() {
  if (document.getElementById("documentViewer").style.display == "none") {
    document.getElementById("documentViewer").style.display = "block";
  } else {
    document.getElementById("documentViewer").style.display = "none";
  }
}
