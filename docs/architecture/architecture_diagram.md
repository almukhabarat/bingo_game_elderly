
# System Context Diagram
Dit C4-diagram toont de architectuur van het Bingo Game Systeem, met de belangrijkste componenten en hun interacties. Het diagram illustreert de communicatie en protocollen tussen deze componenten.

```mermaid
C4Container
Person(host, "Spelleider", "Bedient het bingospel en communiceert met het systeem")

Container_Boundary(c1, "Bingo Game System") {
    Container_Boundary(c2, "Besturings- en Verwerkingseenheden") {
        Container(laptop, "Laptop", "Python", "Host en draait het bingospelscript")
        Container(nao_v6, "NAO V6 Robot", "Python", "Draait het bingospelscript en scant QR-codes")
        Container_Boundary(rpi_boundary, "Raspberry Pi") {
            Container(rpi, "Raspberry Pi", "Python", "Interacts with NAO V6 and ESP32 devices") 
            ContainerDb(mariadb, "MariaDB", "SQL", "Stores game data and logs")
        }
    }
    Container_Boundary(c3, "ESP32 Devices") {
        Container(esp32_bingo, "ESP32 (Bingo Knop)", "C++", "Registreert de bingoknopdruk")
        Container(esp32_vending, "ESP32 (Snoepautomaat)", "C++", "Bestuurt de snoepautomaat spoel")
        Container(esp32_electromagnet, "ESP32 (Elektromagneet)", "C++", "Bestuurt de elektromagneet")
    }
}

Rel(host, laptop, "Controls and monitors")
Rel(laptop, nao_v6, "Ethernet (NAOqi API)")
Rel(esp32_bingo, laptop, "Wi-Fi (HTTP)")
Rel(host, esp32_bingo, "Presses bingo button")
Rel(laptop, esp32_vending, "Wi-Fi (HTTP)")
Rel(laptop, esp32_electromagnet, "Wi-Fi (HTTP)")
Rel(nao_v6, rpi, "Wi-Fi (HTTP)")
```

## Sequence diagram, pi,database,esp,snoepautomaat
```mermaid 
    sequenceDiagram
    participant Nao robot
    participant Laptop
    participant RaspberryPi
    participant Database
    participant ESP32_S3
    participant Snoepautomaat

    Laptop->>Nao robot: Nummers via random
    RaspberryPi->>Database: Voeg winnaar toe aan database
    RaspberryPi->>ESP32_S3: Geef opdracht om snoepautomaat te activeren
    ESP32_S3->>Snoepautomaat: Activeer snoepautomaat
    Snoepautomaat-->>ESP32_S3: Bevestiging van activering
    ESP32_S3-->>RaspberryPi: Bevestiging van activering
```