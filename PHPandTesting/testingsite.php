<!DOCTYPE html>
<html lang="en-us">
<header>
  <title>Test It!</title>
  <!-- Required meta tags -->
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />

  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <!--JQuery input call-->

  <!--<link rel="stylesheet" href="mainStyle.css" />-->
  <!--/*Website Colors:
      --davys-grey: #494947ff;
      --eggshell: #f0ebd8ff;
      --cerulean-frost: #6b9ac4ff;
      --vermilion: #ca3c25ff;
      --venetian-red: #c20114ff;-->
</header>

<body>

  <div class="container">

    <div class="row">

      <div class="col-md-6">

        <a class="navbar-brand" href="../index.html"><img style="width: 50px; height: 50px" src="../Images/Penguinpoints112.png" /></a>


        <?php
        echo '<h3>Hello World! </h3>';

        $name = '<h1>Jorge Ortiz de la Mancha</h1>';

        echo "<p>My name is: $name.</p>";

        $string1 = '<p>This is the first.</p>';
        $string2 = '<p>This is the second.</p>';

        echo $string1 . $string2;

        $myNumber = 33;
        $calculation = $myNumber + (33 / 4) * 6;

        echo "<p>The result of whatever the hell I'm calculating is:</p><p>$calculation</p>";

        $variableName = 'name';

        echo $$variableName;

        $myArray = ['Jorge', 'Viviana', 'Amor'];

        print_r($myArray);

        echo '<br><br>';

        echo "<p>Te quiero mucho $myArray[1]</p><br>";

        $anotherArray[0] = 'Pizza';
        $anotherArray[1] = 'Hot Dog';
        $anotherArray[2] = 'Banana';
        $anotherArray[3] = 'Margarita';
        $anotherArray['favoriteFood'] = 'Steak';

        print_r($anotherArray);

        echo '<br><br>';

        $thirdArray = [
            'PR' => 'Spanish',
            'USA' => 'English',
            'FR' => 'Français',
            'GR' => 'Deutsch',
        ];

        print_r($thirdArray);

        echo '<br><br>';

        echo '<p>The language in USA is ' .
            $thirdArray['USA'] .
            "</p>
            <p>El lenguaje de PR es " .
            $thirdArray['PR'] .
            "</p>
            <p>La langue en France est le " .
            $thirdArray['FR'] .
            "</p>
            <p>In Deutschland wird " .
            $thirdArray['GR'] .
            ' gesprochen</p>';

        echo '<ul><li>Array 1: ' .
            sizeof($myArray) .
            '</li><li>Array 2: ' .
            sizeof($anotherArray) .
            '</li><li>Array 3: ' .
            sizeof($thirdArray) .
            '</li></ul>';

        $anotherArray[] = "Bitchin'";

        print_r($anotherArray);

        echo '<br><br>';

        unset($anotherArray[1]);

        print_r($anotherArray);
        ?>

      </div>

      <div class="col-md-6">

        <?php
        $user = 'Jj';

        if ($user == 'JJ' || $user == 'Jj' || $user == 'jj') {
            echo "<h1>Que la que $user!</h1>";
        } else {
            echo "<h1 style='color: red; font-size: 100px; font-weight: bold'>Get the fuck out!</h1>";
        }

        $age = 500;

        if ($age >= 250) {
            echo "<h2> You are exactly $age y/o. Congrats!</h2>";
        } else {
            echo "<h2 style='color: red; font-size: 100px'> NOOOOOO </h2>";
        }

        for ($i = 10; $i >= 0; $i--) {
            echo $i . '<br>';
        }

        $familyArray = ['Jorge', 'Oira', 'Kim', 'Jomar', 'Vader'];

        for ($i = 0; $i < sizeof($familyArray); $i++) {
            echo $familyArray[$i] . '<br>';
        }

        foreach ($familyArray as $key => $value) {
            $value = $value . ' Ortiz';

            echo 'Array item ' . $key . ' is ' . $value . '<br>';
        }

        $farmsize = sizeof($familyArray) - 1;

        while ($farmsize >= 0) {
            echo '<br>While array item ' .
                $farmsize .
                ' is ' .
                $familyArray[$farmsize] .
                '<br>';

            $farmsize = $farmsize - 1;
        }
        ?>

      </div>

    </div>
    <div class="row">

      <div class="col-sm-6">

        <p>Enter a number to see if it's prime: </p>

        <form>

          <input type="text" name="number">

          <input type="submit" name="go">

        </form>

      </div>

      <div class="col-sm-6">

        <?php
        echo '<br><br>';

        print_r($_GET);

        echo '<br><br>';

        $userin = $_GET['number'];

        /*if($userin%2 < $userin && $userin%2 != 0){
 echo "Prime number.";
 }
 else{
 echo "Composite Number.";
 }*/

        if (
            is_numeric($_GET['number']) &&
            $_GET['number'] > 0 &&
            ($_GET['number'] = round($_GET['number'], 0))
        ) {
            $i = 2;
            $isPrime = true;

            while ($i < $_GET['number']) {
                if ($_GET['number'] % $i == 0) {
                    //Not Prime Number
                    $isPrime = false;
                }
                $i++;
            }

            if ($isPrime) {
                echo "<h1 style='padding: 10px; color: white; font-weight: bold; background-color: black;'>Congrats! " .
                    $userin .
                    ' is a prime number!</h1>';
            } elseif ($isPrime == false) {
                echo "<p style='padding: 10px;'>" .
                    $userin .
                    ' is not a prime number...</p>';
            }
        } elseif ($_GET) {
            echo "<div 
            class='alert alert-danger alert-dismissible fade show' 
            role='alert'>
            <button
            style='float: right;' 
            type='button' 
            class='close' 
            data-dismiss='alert' 
            aria-label='Close'> 
            <span aria-hidden='true'>&times;</span>
            </button>
            It needs to be a positive number from 1 to infinity. Hint: 1 and 2 are prime numbers.
            </div>";
        }
        ?>

      </div>

    </div>

  </div>
  <!-- Option 1: Bootstrap Bundle with Popper -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

</body>

</html>