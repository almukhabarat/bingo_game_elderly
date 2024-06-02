<?php
$servername = "localhost"; // Change if your MySQL server is different
$username = "ti3groep";
$password = "BG32L2D";
$dbname = "BingoDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Post data komt binnen en wordt opgesplitst in 4 variabelen
$query_type = $_POST['query_type']
$bingo_spel_id = $_POST['bingoSpelId'];
$bingo_win_id = $_POST['bingoWinId'];
$begin_tijd = $_POST['beginTijd'];
$eind_tijd = $_POST['eindTijd'];


// SQL query voorbereiden
// $stmt = $conn->prepare("INSERT INTO BingoSpel (bingoWinId, beginTijd, eindTijd) VALUES (NULL, ?, ?)");
if ($query_type == 'post_game_begin') {
    $stmt = $conn->prepare("INSERT INTO BingoSpel (bingoSpelId, bingoWinId, beginTijd, eindTijd) VALUES (NULL, NULL, ?, NULL)");
    $stmt->bind_param("ss", $begin_tijd, $eind_tijd);
}

// Execute the statement
if ($stmt->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
