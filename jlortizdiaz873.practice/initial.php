<?php 

    $link = mysqli_connect("sdb-w.hosting.stackcp.net", "users_database-323133aa08", "djeqlnu3o9", "users_database-323133aa08");


    if(array_key_exists('name', $_POST) OR array_key_exists('passwords', $_POST)){

        if($_POST['name'] == ''){
            echo "No email address";
            echo $_POST['passwords'];
        }
        
        if($_POST['passwords'] == ''){
            echo $_POST['name'];
            echo "No password available";
        }

        else{
            echo $_POST['name'];
            echo $_POST['passwords'];
        }
        
    }

    if(mysqli_connect_error()){

    die("Sorry, could not connect");

    }

    // $query = "INSERT INTO `users` (`email`, `password`) VALUES ('', '')"; Inserts record

    // $query = "UPDATE `users`  SET `password` = '' WHERE `email` = '' LIMIT 1"; Updates record

    // mysqli_query($link, $query); Calls the query

    // $query = "SELECT * FROM `users` WHERE `email` LIKE '%gmail.com'"; % means search for anything

    // $query = "SELECT * FROM `users` WHERE `id` >= 2"; * selector for everything

    // $query = "SELECT `email` FROM `users` WHERE `id` >= 2"; selects email using id only

    // $query = "SELECT `email` FROM `users` WHERE `id` >= 2 AND `email` LIKE '%t%'"; uses AND to select multiple fields

    // $name = "Jorge O'Shea"; Name value

    // $query = "SELECT `email` FROM `users` WHERE `name` = '".mysqli_real_escape_string($link, $name)."'"; Always escape your characters to prevent sql injection attacks

    // if($result = mysqli_query($link, $query)){
        // while($row = mysqli_fetch_array($result)){

            // print_r($row);

        // }
    // }
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="Description" content="Enter your description here" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <title>SQL Practice</title>
</head>

<body>
    <div class="container justify-content-center">
        <div class="row">
            <div class="col d-flex justify-content-center">
                <form method="post">
                    <h1>Hello There!</h1>
                    <p><label for="name" class="form-item">What is your name: <br><sub>Please place real name
                                here</sub></label>
                        <br>
                        <input type="text" id="name" name="name" placeholder="name here">
                    </p>
                    <p><label for="passwords" class="form-item">Enter your password: <br><sub>Must contain at least 6
                                characters
                                and 1 number</sub></label>
                        <br>
                        <input type="password" name="passwords" id="passwords">
                    </p>
                    <input type="submit" value="Submit">
                </form>
                <p>Hello</p>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>

</html>