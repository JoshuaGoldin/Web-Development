/*
Joshua Goldin
Cake Application
4/5/18
*/

"use strict";


function initPage() {
	document.getElementById("sbutton").onclick = saveMailingInfo;
    function saveMailingInfo() {
      clearCookies();
        var dayte = new Date();
        dayte.setFullYear(dayte.getFullYear() + 3);
        var mailingForm = document.getElementById("mailingForm");
		var fNElement = document.getElementById("firstName").value;
		var lNElement = document.getElementById("lastName").value;
		var eMElement = document.getElementById("email").value;
		var bDElement = document.getElementById("birthday").value;
		
        var selectElement = document.getElementById("favoriteCake").value;
        var radioElements = document.getElementsByName("frequency");
       
     for(var i = 0; i < mailingForm.length; i++) {
         writeCookie("selectElement", selectElement, 4);
         writeCookie("fNElement", fNElement, 4);
         writeCookie("lNElement", lNElement, 4);
         writeCookie("eMElement", eMElement, 4);
         writeCookie("bDElement", bDElement, 4);
		 alert("the cookie has been writen");
		 	if(mailingForm[i].checked == true){
					writeCookie("radioElements",  mailingForm[i].value, 10);
				}
     }
    }
}

function SetUpPage() {
    initPage();
}



addEvent(window, "load", SetUpPage);



