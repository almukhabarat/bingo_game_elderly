<?php
header('Content-Type: application/json');

// Example command
$response = array(
    'action' => 'speak',
    'message' => 'Hello from the Raspberry Pi!'
);

echo json_encode($response);
?>
