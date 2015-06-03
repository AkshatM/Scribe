var s = document.createElement('script');
s.src = chrome.extension.getURL('listener.js');
(document.head || document.documentElement).appendChild(s);
