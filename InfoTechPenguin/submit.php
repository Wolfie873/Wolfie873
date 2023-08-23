<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    $to = 'jorge.ortiz20@outlook.com';

    $subject = "$name has sent you an information request";

    $messageBody = "Name $name\n";
    $messageBody .= "Email: $email\n";
    $messageBody .= "Message: \n$message\n";

    $headers = "From $email\r\n";

    $mailSuccess = mail($to, $subject, $messageBody, $headers);

    if ($mailSuccess) {
        echo "Thank you for your message. We will get back to you soon.";
    } else {
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // Redirect to the contact form if accessed directly.
    header("Location: contact_form.html");
}
?>
