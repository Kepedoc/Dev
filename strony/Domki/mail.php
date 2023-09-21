<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $wiadomosc = $_POST["wiadomosc"];
    
    $odbiorca = "kasjanoboss@gmail.com";

    $temat = "Support Meerblick";

    $naglowki = "From: $email" . "\r\n" .
                "Reply-To: $email" . "\r\n" .
                "X-Mailer: PHP/" . phpversion();
    
    if (mail($odbiorca, $temat, $wiadomosc, $naglowki)) {
        echo "Wiadomość została wysłana pomyślnie.";
    } else {
        echo "Wystąpił błąd podczas wysyłania wiadomości.";
    }
}
?>