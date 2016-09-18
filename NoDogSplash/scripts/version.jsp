
User.User user = new User.User();    
<% %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Testing IE Compatibility Mode</title>
    <script src="ieUserAgent.js" type="text/javascript"></script>
	<link href="${pageContext.request.contextPath}/css/base/jquery-ui-1.10.4.custom.css" rel="stylesheet">
	<script src="${pageContext.request.contextPath}/scripts/jquery-1.10.2.js"></script>
	<script src="${pageContext.request.contextPath}/scripts/jquery-ui-1.10.4.custom.js"></script>
	<script src="${pageContext.request.contextPath}/scripts/piolax/formController.js"></script>
	
</head>
<body>
<div id="results">Results:</div>
<script type="text/javascript">
    var val = "IE" + ieUserAgent.version;
    if (ieUserAgent.compatibilityMode)
        val += " Compatibility Mode (IE" + ieUserAgent.renderVersion + " emulation)";
    $("#results").html("We have detected the following IE browser: " + val);
</script>
</body>
<script>
if (window.jQuery) {  
    alert("jquery is active");
} else {
    alert("jquery is NOT active"); 
}

document.onkeypress = function(e){ 
	e = e || window.event; 
	alert("KeyCode: " + e.keyCode); 
};
</script>
</html>