function sendCommand(command) {
    fetch('/control?command=' + command)
        .then(response => response.text())
        .then(data => console.log(data));
}