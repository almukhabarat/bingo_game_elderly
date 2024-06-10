<?php
$servername = "localhost";
$username = "ti3groep";
$password = "BG32L2D";
$dbname = "BingoDB";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$query_type = $_POST['query_type'] ?? null;

if ($query_type == 'post_game_begin') {
    $stmt = $conn->prepare("INSERT INTO BingoSpel (beginTijd, eindTijd) VALUES (CURRENT_TIMESTAMP(), NULL)");
    if ($stmt && $stmt->execute()) {
        echo json_encode(["bingoSpelId" => $conn->insert_id]);
    }
    $stmt->close();
}

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

if ($query_type == 'get_bingo_card') {
    $bingo_kaart_id = $_POST['bingoKaartId'] ?? null;
    if ($bingo_kaart_id) {
        $stmt = $conn->prepare("SELECT getal FROM BingoKaart WHERE bingoKaartId = ?");
        if ($stmt) {
            $stmt->bind_param("i", $bingo_kaart_id);
            if ($stmt->execute()) {
                $stmt->bind_result($getal);
                $results = [];
                while ($stmt->fetch()) {
                    $results[] = $getal;
                }
                if (!empty($results)) {
                    echo json_encode(["getal" => implode(',', $results)]);
                } else {
                    echo json_encode(["error" => "Bingo card not found"]);
                }
            } else {
                echo json_encode(["error" => "Failed to execute statement"]);
            }
            $stmt->close();
        } else {
            echo json_encode(["error" => "Failed to prepare statement"]);
        }
    } else {
        echo json_encode(["error" => "Invalid bingoKaartId"]);
    }
}

$conn->close();
?>