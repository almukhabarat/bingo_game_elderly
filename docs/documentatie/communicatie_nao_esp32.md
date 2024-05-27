# NAO Bingo project netwerk documentatie

In dit document wordt uitgelegd hoe de communicatie tussen de NAO robot, de ESP32 microcontrollers en de database zal verlopen. In de eerste sprint van het project was er nog veel discussie over hoe we de communicatie tussen de NAO robot en de randapparatuur zouden gaan aanpakken. Een idee was om het via een lokale raspberry pi te doen, deze kwam dan op de rug van de NAO robot en alle ESP32 microcontrollers waren dan via Wi-Fi of bedraad verbonden met de deze raspberry pi. Omdat we uiteindelijk met een database wilden gaan werken in het project, en op basis van feedback die we hadden gekregen van een docent hadden we toch besloten om het via server op school te doen. Op dit moment maken we gebruik van een raspberry pi 3 die op dit moment in een serverruimte draait van HBO-ICT op de Hogeschool van Amsterdam. 

Op deze rasberry pi 3 draait een apache webserver met daarop een flask API. Het is straks de bedoeling dat de NAO robot en de microcontrollers via de API's van de webserver met elkaar kunnen communiceren. Door onze netwerk infrastructuur op deze manier op te zetten is het uiteindelijk ook zeer envoudig om de database functionaliteit in ons project te implementeren aangezien het voor de microcontrollers/NAO robot via de API's redelijk eenvoudig is om met de database te kunnen praten.

## Prijsautomaat communicatie met webserver (sequence diagram)

```mermaid
sequenceDiagram
    participant ESP32-S3
    participant WiFi netwerk
    participant FlaskAPI

    ESP32-S3->>WiFi netwerk: Verbinden met Wi-Fi
    ESP32-S3->>FlaskAPI: Stuurt een HTTP GET request naar /get_command
    NAO robot->>FlaskAPI: Send HTTP POST /set_command
    FlaskAPI-->>NAO robot: Bevestiging dat bericht is ontvangen door API
    FlaskAPI-->>ESP32-S3: Krijgt een HTTP response terug die afkomstig is van /set_command
    Note over ESP32-S3: Instructie wordt ontvangen als JSON
    Note over NAO robot: Instructie wordt verzonden als JSON
    Note over FlaskAPI: De Flask API maakt gebruik van HTTP long polling

