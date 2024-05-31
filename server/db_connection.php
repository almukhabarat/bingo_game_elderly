<?php
$servername = "localhost";
$username = "ti3groep";
$password = "BG32L2D";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>