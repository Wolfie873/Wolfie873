<?php
mysqli_connect('localhost', 'sa', 'admin@jl873', 'Jorge');

 if(mysqli_connect_error()){
    echo "There was an error in the connection";
 }
 else{
    echo "Connected to the database";
 }

?>