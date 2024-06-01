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

// Get data from POST request
$player_name = $_POST['player_name'];
$score = $_POST['score'];

// Prepare and bind
$stmt = $conn->prepare("INSERT INTO bingo_results (player_name, score) VALUES (?, ?)");
$stmt->bind_param("si", $player_name, $score);

// Execute the statement
if ($stmt->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
