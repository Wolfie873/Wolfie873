window.onload = function () {
  var xpPoints = document.getElementById("xp").innerHTML;
  var x = 5;

  for (var i = 0; i < x; i++) {
    document.getElementById("minushp").onclick = function () {
      var hp = 0;
      hp = hp - 1;
      document.getElementById("hp").innerHTML = String(hp);
    };
    document.getElementById("plushp").onclick = function () {};
    document.getElementById("minusmp").onclick = function () {};
    document.getElementById("plusmp").onclick = function () {};
    document.getElementById("minusstr").onclick = function () {};
    document.getElementById("plusstr").onclick = function () {};
    document.getElementById("minuslck").onclick = function () {};
    document.getElementById("pluslck").onclick = function () {};
  }
};
