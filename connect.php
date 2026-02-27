<?php

$host = "localhost";
$user = "root";
$pass = "";
$db = "login";
$conn = new mysqli($host,$user,$pass,$db);
if($conn -> connection_error){
    echo "Failed to connect DataBase!!!".$conn -> connection_error;
}
?>