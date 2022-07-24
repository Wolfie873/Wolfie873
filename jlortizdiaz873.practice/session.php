<?

session_start();

if($_SESSION['email']){

    echo "<p>You are logged in</p>";
}
else{

    header("Location: initial.php");
}

?>