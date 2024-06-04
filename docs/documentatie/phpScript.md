# Documentatie voor BingoSpel PHP script

Deze documentatie biedt een overzicht en uitleg van de PHP code die dient als backend voor het bingospel. De code zorgt voor database connectie voor het starten van een nieuw bingospel en het opslaan van opgeroepen nummers.

## Verbinden

```php
<?php
$servername = "localhost";
$username = "ti3groep";
$password = "BG32L2D";
$dbname = "BingoDB";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
```

In dit gedeelte van de code worden de database-inloggegevens ingesteld en een nieuwe MySQL verbinding gemaakt. Indien de verbinding faalt, wordt een foutmelding weergegeven en wordt het script beëindigd.

## Afhandelen van Verzoeken

### `query_type` Parameter

```php
$query_type = $_POST['query_type'] ?? null;
```

Hier wordt de `query_type` parameter uit de POST request gehaald en toegewezen aan een variabele. Indien de parameter niet aanwezig is, wordt `null` toegewezen.

### `post_game_begin` request

```php
if ($query_type == 'post_game_begin') {
    $stmt = $conn->prepare("INSERT INTO BingoSpel (beginTijd, eindTijd) VALUES (CURRENT_TIMESTAMP(), NULL)");
    if ($stmt && $stmt->execute()) {
        echo json_encode(["bingoSpelId" => $conn->insert_id]);
    }
    $stmt->close();
}
```

Indien de `query_type` gelijk is aan `post_game_begin`, wordt een nieuwe rij toegevoegd aan het BingoSpel tabel met de huidige tijd als beginTijd en `NULL` als eindTijd. De id van het nieuw gemaakte bingospel wordt teruggestuurd als JSON.

### `post_number` request

```php
if ($query_type == 'post_number') {
    $bingo_spel_id = $_POST['bingoSpelId'] ?? null;
    $opgenoemd = $_POST['opgenoemd'] ?? null;

    if ($bingo_spel_id && $opgenoemd) {
        $stmt = $conn->prepare("INSERT INTO BingoGetal (bingoSpelId, opgenoemd) VALUES (?, ?)");
        if ($stmt) {
            $stmt->bind_param("ii", $bingo_spel_id, $opgenoemd);
            $stmt->execute();
            $stmt->close();
        }
    }
}
```

Indien de `query_type` gelijk is aan `post_number`, worden de `bingoSpelId` en `opgenoemd` parameters uit de POST request gehaald. Indien beide parameters aanwezig zijn, wordt een nieuwe rij toegevoegd aan het BingoGetal tabel met het opgegeven bingospel-id en het opgeroepen nummer.

#

```php
$conn->close();
```
Na het afhandelen van de verzoeken wordt de databaseverbinding gesloten.