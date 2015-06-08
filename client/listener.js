document.onkeyup = function (event) {
   if (event.keyCode == 113){
      var compose_ids = Array.prototype.slice.call(document.getElementsByClassName("Am Al editable LW-avf va_ar"));//for compose windows
      var reply_ids = Array.prototype.slice.call(document.getElementsByClassName("Am a09 Al editable LW-avf va_ar"));//for reply windows
      var x = compose_ids.concat(reply_ids);
      console.log(x);
      var urlRegex = /(https?:\/\/[^\s]+)/g; // regular expression for matching URLS.
      // This regex is bad, but that is alright - this is just a proof of concept for the moment.
      for (i = 0; i < x.length; i++){
          // iterate through x[i] and match urls with  urlRegex
	  x[i].innerHTML = x[i].innerText.replace(urlRegex, function(url){
	      var final_value = HTTPResponse(url);
	      if (final_value[1].indexOf("image") != -1){
	         // embed image
		 return '<img src = "data:'+final_value[1]+';base64,'+final_value[0]+'"/>'; // returns base64 encoded image.
	         } else {
	            return '<a href="' + url + '">' + final_value[0] + '</a>';
	         }
	      });
	  }
   };
}

function HTTPResponse(url){
   var xmlHttp = new XMLHttpRequest();
   var mashape_api_key = "9kXiCVHd85msh7Scl9CLKlBFDhU7p1YwgoWjsn9JtTN8RAGnF3"; // insecure, but no risk is attached - revealing this just means that people get to ping my API, which is fine.
   var native_url = "https://akshatm-richgmaileditor-v1.p.mashape.com/?url=";
   xmlHttp.open("GET",native_url+url, false); //currently synchronous; must change to asynchronous
   xmlHttp.setRequestHeader("X-Mashape-Key", mashape_api_key);
   xmlHttp.send();
   if (xmlHttp.status == 400){
      return [url,"none"];
   }
   return [xmlHttp.responseText, xmlHttp.getResponseHeader("content-type")];
}
