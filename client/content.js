var s = document.createElement('script');
s.src = chrome.extension.getURL('listener.js');
(document.head || document.documentElement).appendChild(s);

var s = document.createElement('script');
s.src = chrome.extension.getURL('Autolinker.min.js');
(document.head || document.documentElement).appendChild(s);

chrome.extension.sendRequest("show_page_action");
