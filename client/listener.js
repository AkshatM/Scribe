document.onkeyup = function (event) {
   if (event.keyCode == 113){ // listen for press of F2 button
      var compose_ids = Array.prototype.slice.call(document.getElementsByClassName("Am Al editable LW-avf va_ar"));//for compose windows
      var reply_ids = Array.prototype.slice.call(document.getElementsByClassName("Am a09 Al editable LW-avf va_ar"));//for reply windows
      var windows = compose_ids.concat(reply_ids);
      for (i = 0; i < windows.length; i++){
          windows[i].innerHTML = Autolinker.link(windows[i].innerHTML,
	      {
	         replaceFn : function (autolinker, match) { // replace all 
		     var final_value = HTTPResponse(match.getAnchorHref());
                     var tag = new Autolinker.HtmlTag();
		     if (final_value[1].indexOf("image") != -1){ 
		     // if URL is of an image, then insert img tag with appropriate source
		        tag.setTagName('img');
			tag.setAttr('src', match.getAnchorHref();
			tag.setAttr('alt',match.getAnchorHref());
		     } else {
		       // otherwise, replace with human-readable hyperlink
			tag.setTagName('a');
			tag.setAttr('href',match.getAnchorHref());
			tag.setInnerHtml(final_value[0]);
		     }
		     return tag;
		 }
          });
      }
   }
} 




function HTTPResponse(url){
   var xmlHttp = new XMLHttpRequest(); //create XMLHttpRequest
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

