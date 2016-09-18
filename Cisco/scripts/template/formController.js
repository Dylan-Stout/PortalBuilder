/**
 * @author - Dylan Stout
 * 7/19/2016
 * 
 * Description: handling events on all screens except Release Load
 * Used to capture asterisk keypress and carriage return. 
 */


sfFocus = function() {
	var sfEls = document.getElementsByTagName("INPUT");
	for (var i=0; i<sfEls.length; i++) {
		sfEls[i].onfocus=function() {
			this.className+=" sffocus";
		}
		sfEls[i].onblur=function() {
			this.className=this.className.replace(new RegExp(" sffocus\\b"), "");
		}
	}}
if (window.attachEvent) window.attachEvent("onload", sfFocus);

/**
 * Carriage Return Handling - select next focusable field on [Enter/Return](keyCode=13)
 */
function handleCarriageReturn(e){ 
	if(e.keyCode == 13){ // enter pressed
		try{
			e.preventDefault ? e.preventDefault() : (e.returnValue = false);

			var $canfocus = $(':focusable');
			var index = $canfocus.index(document.activeElement) + 1;
			if (index >= $canfocus.length) index = 0;
			$canfocus.eq(index).focus(); //set focus to next available focusable //set focus to next available focusable

		}catch(err){
			alert(err.message); 
		}
	}
}

/**
 * Iterate over input fields.. If empty place cursor in that 
 * input field. (exclude checkboxes)
 * 
 * Redirect to Release Load Screen on ASTERISK (*) press 
 * via grey+tab buttons on Symbol RF Gun
 */
function onBodyLoad(){

	$(function() {
		$("input[value='']:not([type='checkbox'], [type='button']):visible:first").focus();
	});

	document.onkeypress = function(e){ 
		e = e || window.event; 
//		alert("KeyCode: " + e.keyCode); 
		if(e.keyCode == 42){
			window.location.href = servletContext()+ '/piolax/GetReleaseLoads';
		}

		if(e.keyCode == 46){
			window.location.href = '/ScanUI/piolax/LogoutUser';
		}

	};
};

/**
 * Returns servlet context pathname
 * @returns {String}
 */
function servletContext() {
	var sc = window.location.pathname.split( '/' );
	return "/"+sc[1];
} 

/**
 * Move cursor to the (STATION.JSP) "From Station:" input text field
 */
function focusFromStation(){
	document.getElementById("fromStationForm").elements[0].focus(); 
};

/**
 * Move cursor to the (STATION.JSP) "To Station:" input text field
 */
function focusToStation(){
	document.getElementById("toStationForm").elements[0].focus(); 
};

/**
 * Move cursor to the (STATION.JSP) "To Load:" input text field
 */
function focusToLoad(){
	document.getElementById("toLoadForm").elements[0].focus(); 
};

/**
 * Move cursor to the (PICKING.JSP) "From Station:" input text field
 */
function focusPickingFromStation(){
	document.getElementById("pickingFromStationForm").elements[0].focus(); 
};


/**
 * Move cursor to the (PICKING.JSP) "To Load:" input text field
 */
function focusPickingSerialNumber(){
	document.getElementById("pickingSerialNumberForm").elements[0].focus(); 
};

/**
 * Move cursor to the (PICKING.JSP) "To Load:" input text field
 */
function focusPickingToStation(){
	document.getElementById("pickingToStationForm").elements[0].focus(); 
};


/**
 * Move cursor to next empty input text field on station.jsp
 */
function stationFocusOnNextBlank(){ 
	if(document.getElementById("fromStationForm").elements[0].value == ""){
		focusFromStation();
	}else if(document.getElementById("toStationForm").elements[0].value == ""){ 
		focusToStation();
	}else if(document.getElementById("toLoadForm").elements[0].value == ""){ 
		focusToLoad();
	}
};

/**
 * Move cursor to next empty input text field on picking.jsp
 */
function pickingFocusOnNextBlank(){ 
	if(document.getElementById("pickingFromStationForm").elements[0].value == ""){
		focusPickingFromStation();
	}else if(document.getElementById("pickingSerialNumberForm").elements[0].value == ""){ 
		focusPickingSerialNumber();
	}else if(document.getElementById("pickingToStationForm").elements[0].value == ""){ 
		focusPickingToStation();
	}
};



/**
 * @author - Dylan Stout
 * 7/19/2016
 * 
 * Description: handling events on the Release Load screen. 
 * Used to release the from/to station's loads via RF UI
 */

/**
 * Release: TO LOAD button pressed 
 * Set as disabled to change color and disallow input
 */
function releaseToLoad(){ 
	alert("RELEASED TO LOAD!"); 
	document.getElementById('toLoadReleaseButton').disabled = 'disabled'; 
};

/**
 * Release: FROM LOAD button pressed 
 * Set as disabled to change color and disallow input
 */
function releaseFromLoad(){ 
	alert("RELEASED FROM LOAD!"); 
}; 


