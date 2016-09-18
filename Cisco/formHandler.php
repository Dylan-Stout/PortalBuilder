<?php

$name = $_POST["name"];
$email = $_POST["email"];
$password = $_POST["password"];

$postData = $name . "," . $email . "," . $password. "\n";

// the name of the file you're writing to
$myFile = __DIR__."/tmp/user.txt";

// opens the file for appending (file must already exist)
$fh = fopen($myFile, 'a+');

// Write to the file
fwrite($fh, $postData);

// You're done
fclose($fh);

?>