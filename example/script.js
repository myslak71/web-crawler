const allLinks = document.querySelector('a')
var h1 = document.querySelector("h1");
var a = document.createElement('a');
var linkText = document.createTextNode("JS dynamic link");
a.appendChild(linkText);
a.href = "http://dynamic_link.js";
document.body.insertBefore(a, allLinks[allLinks.length]);
