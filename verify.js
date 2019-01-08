/*
Joshua Goldin
Cake Application
04/5/18
*/

"use strict";


var favCakes = ["Butter Cream", "Chocolate", "Vanilla", "Red Velvet"];


function retrieveMemberInfo()  {
	
    var htmlSpanFirstN = document.getElementById("firstName");
	var htmlSpanLastN = document.getElementById("lastName");
	var htmlSpanEmail = document.getElementById("email");
	var htmlSpanBirth = document.getElementById("birthday");
	
    var htmlSpanFavCake = document.getElementById("favoriteCake");
    var htmlSpanFrenquency = document.getElementById("frequency");


    for(var i = 0; i < favCakes.length; i++){
		
	    htmlSpanFirstN.innerHTML = getCookie("fNElement");
		htmlSpanLastN.innerHTML = getCookie("lNElement");
		htmlSpanEmail.innerHTML = getCookie("eMElement");
		htmlSpanBirth.innerHTML = getCookie("bDElement");
					  
        htmlSpanFavCake.innerHTML = getCookie("selectElement");
	    htmlSpanFrenquency.innerHTML = getCookie("radioElements");
    }
}

function SetPage() {
    retrieveMemberInfo();
}


addEvent(window, "load", SetPage);