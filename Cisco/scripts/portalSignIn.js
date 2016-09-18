$(document).ready(function() {
  $("#confirmPassword").keyup(validateRegister);
  $("#addressRequested").hide(); 
  $("#connectionStatus").hide(); 
  $("#connected").hide(); 
  $('#registerForm').submit(function(){
          setTimeout(showConnectionAddress, 1000);
          setTimeout(showAddressOk, 2700);
          setTimeout(showConnectionStatus, 3300); 
          setTimeout(showDnsOk, 5900);
          setTimeout(showConnected, 6700);
    });
});


function validateRegister() {
  var username = $("username").val();
  var password1 = $("#password").val();
  var password2 = $("#confirmPassword").val();

    if(password1 == password2) {
       $("#validate-status").text("Passwords match!");
       if(username !== ""){
       		$('#registerButton').prop('disabled',false);
       }
    }
    else {
        $("#validate-status").text("Passwords do not match!");  
        $('#registerButton').prop('disabled',true);
    }
    
}

function showConnectionAddress(){ 
  $("#addressRequested").show(); 
}

function showAddressOk(){
  $("#showAddressOk").show(); 
}

function showConnectionStatus(){ 
  $("#connectionStatus").show(); 
}

function showDnsOk(){
  $("#showDnsOk").show(); 
}

function showConnected(){ 
  $("#connected").show(); 
}

function popupConnection(){
  setTimeout(showConnectionAddress, 1000);
  setTimeout(showAddressOk, 2700);
  setTimeout(showConnectionStatus, 3300); 
  setTimeout(showDnsOk, 5900);
  setTimeout(showConnected, 6700);
  setTimeout(function(){ $.mobile.loading( "hide"); }, 6900);

}

function submitForm(){    
  var name = $("input#name").val();
  var email = $("input#email").val();
  var password = $("input#password").val();
  var dataString = 'name='+ name + '&email=' + email + '&password=' + password;
  $.ajax({   
    type: "POST",
    data : dataString,
    cache: false,  
    url: "formHandler.php",   
    success: function(data){
      //                
    }   
  }); 

  $( "#popupDialog" ).popup( "open" );
  $.mobile.loading( "show", {
  text: "Connecting...",
  textVisible: true,
  theme: "a",
  html: ""
  }); 
  popupConnection(); 

  
}
