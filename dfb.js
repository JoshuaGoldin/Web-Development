/*
Joshua Goldin
dfb
Cake Application
4/5/18
*/


	function addEvent(obj, evt, target){
		if(obj.addEventListener){
			obj.addEventListener(evt, target, false);
		} else {
			if(obj.attachEvent) {
				obj.attachEvent("on" + evt, target, false);
			}
		}
	}


	function removeEvent(obj, evt, target) {
		if (obj.removeEventListener){
    		 obj.removeEventListener(event, target, false);
  		} else if (obj.attachEvent){
    		  obj.detachEvent("on" + event, target);
 		    }
	}


	function writeCookie(cName, cValue, expDate, cPath, cDomain, cSecure) {
		if (cName && cValue != "") {
			var cString = cName + "=" + escape(cValue);
			if (expDate)
				cString += ";expires=" + expDate.toGMTString();
			if (cPath)
				cString += ";path=" + cPath;
			if (cDomain)
				cString += ";domain=" + cDomain;
			if (cSecure)
				cString += ";secure";


     document.cookie = cString;
  }
}


function writeCookie(cookieName, cookievalue, exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));

	var expires = "expires=" + d.toGMTString();
	document.cookie = cookieName+ "=" + cookievalue+ "; " + expires;
}


function getCookie(cookieName) {
	if(document.cookie) {
		var cookiesArray = document.cookie.split("; ");
		for(var i = 0; i < cookiesArray.length; i++) {
			if(cookiesArray[i].split("=")[0] == cookieName) {
				 return unescape(cookiesArray[i].split("=")[1]);
			}
		}	
	
	}
}

function clearCookies() {
	var cookieString = document.cookie;
	var cookieArray = cookieString.split("; ");
	var expiresDate = new Date();
	
	expiresDate.setDate(expiresDate.getDate() - 7);
	for(var i = 0; i < cookieArray.length; i++) {
		document.cookie = cookieArray[i] + "; expires=" + expiresDate.toUTCString();
	}
}



