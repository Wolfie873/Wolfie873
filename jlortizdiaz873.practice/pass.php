<?php 

echo "<p>This is level 1 encryption: ".md5('password')."</p>"; //One way encryption
//Level 1 encryption, weak

$salt = 'hhsgdt6789e9*&IK*^Y';
 echo "<p>This is level 2 encryption: ".md5($salt.'password')."</p>";
//Level 2 encryption, medium

$row['id'] = 3;
echo "<p>This is level 4 encryption: ".md5(md5($row['id']).'password')."</p>";
//Level 4 encryption, better

$hash = password_hash('password', PASSWORD_DEFAULT);
echo "<p>This is password_hash() encryption: ".$hash."</p>";// Visible hash
echo "<br>";
if(password_verify('password', $hash)){

    echo "Password is valid";
}
else{

    echo "Incorrect password";
}
//Level 5 encryption password_hash(), best


?>