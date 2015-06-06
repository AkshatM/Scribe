document.onkeyup = function (event) {
   native_url = "http://www.akshatm.com:8080/?";
   if (event.keyCode == 113){
      var x = document.getElementsByClassName("Am Al editable LW-avf va_ar");//for compose windows
      var urlRegex = /(https?:\/\/[^\s]+)/g; // regular expression for matching URLS.
      // This regex is bad, but that is alright - this is just a proof of concept for the moment.
      for (i = 0; i < x.length; i++){
          // iterate through x[i] and match to urlRegex
	  x[i].innerHTML = x[i].innerText.replace(urlRegex, function(url){
	      return '<a href="' + url + '">' + HTTPResponse(url) + '</a>';
	      });
	  }
   };
}

function HTTPResponse(url){
   var xmlHttp = new XMLHttpRequest();
   var native_url = "http://www.akshatm.com:8080/?"; // will not work because of mixed content restrictions
   xmlHttp.open("GET",native_url+url);
   xmlHttp.send();
   return xmlHttp.responseText;
}
