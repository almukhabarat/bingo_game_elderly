
# Sequence diagram

 Dit is een sequence diagram voor de verbinding van de Pi (database) met de nao robot en de pi, met de barcode, de bingo button en een electromagneet.  


```mermaid
flowchart LR
    subgraph RaspberryPi["Raspberry Pi\nController"]
        MySQL["MySQL Database"]
    end

    RaspberryPi <--> NAO_Robot
    RaspberryPi -->|Power Control| Electromagnet
    BarcodeScanner -->|Data Output| RaspberryPi
    BingoButton -->|Signal Output| RaspberryPi

    NAO_Robot["NAO Robot"]
    Electromagnet["Electromagnet"]
    BarcodeScanner["Barcode Scanner"]
    BingoButton["Bingo Button"]

```
    Sequence diagram, pi,database,esp,snoepautomaat
```mermaid 

   sequenceDiagram
   participant Nao robot
    participant RaspberryPi
    participant Database
    participant ESP32_S3
    participant Snoepautomaat

    RaspberryPi->>Database: Voeg winnaar toe aan database
    RaspberryPi->>Nao robot:Nummers via random
    %% Database-->>RaspberryPi: Bevestiging van toevoeging
    %% Database->>RaspberryPi: 
    RaspberryPi->>ESP32_S3: Geef opdracht om snoepautomaat te activeren
    ESP32_S3->>Snoepautomaat: Activeer snoepautomaat
    Snoepautomaat-->>ESP32_S3: Bevestiging van activering
    ESP32_S3-->>RaspberryPi: Bevestiging van activering




```