# ERD Concept

```mermaid
    erDiagram
        GAMESTATE ||--o| BINGO : heeft
        BINGO ||--o| BINGO_CHART : bevat
        NUMBER_CALLED ||--o{ BINGO_CHART : geldt

        BINGO_CHART {
            Number STRING PK
        }

        NUMBER_CALLED {
            Called STRING PK
        }

        BINGO {
            WonId INT PK
            Time TIMESTAMP
            Number STRING FK
        }

        GAMESTATE {
            GameId INT PK
            Start TIMESTAMP
            End TIMESTAMP
            WonId INT FK
        }
```

Qr code bevat bingo getallen >>> 

Nao6 krijgt getallen van raspi en noemt deze op >>> 

Raspberry Pi genereert getallen (van bijvoorbeeld 1 tot 50) >>>

Een database moet opslaan welke getallen al zijn omgeroepen en welke niet >>>

Een database kan weten hoe vaak een bingo al is omgeroepen en eventueel om welke getal combinaties het gaat >>>

## v2

Idee 1 

```mermaid
    erDiagram
        BingoCard ||--o{ Won : heeft
        Game ||--|| Won : bevat

        BingoCard {
            cardId INT PK
            cardNumber INT
        }

        Game {
            gameId INT PK
            gameDate TIMESTAMP 
        }

        Won {
            WonId INT PK
            cardId INT FK
            gameId INT FK
            WonCount INT
            WonDate INT 
        }
```

Apart tabel maken voor bingokaart nummers

## ERD / Huidige database ontwerp 

```mermaid
    erDiagram
        BingoSpel ||--|| BingoWin: bevat
        BingoWin ||--|| BingoKaart: heeft 
        BingoSpel ||--o{ BingoGetal: heeft
        PrijsAutomaat ||--o{ Snoep: bevat

        BingoGetal {
            id INT PK
            bingoSpelId INT FK
            opgenoemd INT
        }

        BingoKaart {
            id INT PK
            getal VARCHAR
        }

        BingoWin {
            id INT PK
            bingoKaartId INT FK
            winDatum TIMESTAMP
        }

        BingoSpel {
            id INT PK
            bingoWinId INT FK
            beginTijd TIMESTAMP 
            eindTijd TIMESTAMP 
        }

        PrijsAutomaat {
            snoepId INT FK
        }

        Snoep {
            id INT PK
            soort STRING
            merk STRING
        }
```

### Database ontwerp uitgewerkt in SQL | sprint 3

Dit is uiteindelijk het database ontwerp dat we hebben geïmplementeerd. Zodra het spel begint wordt er eerst een nieuwe BingSpelId aangemaakt waar later de omgeroepen getallen aan worden gekoppelt. 

In het BingoGetal tabel worden de omgeroepen nummers opgeslagen die gekoppelt zijn aan een BingSpelId. Hiermee kan men waarnemen wel getallen in welke volgorde waren omgeroepen per bingo ronde.

Tenslotte wordt er een winId gekoppelt aan de bijbehorende spelId.

We hebben als concept ook nog een prijsautomaat tabel met een snoep tabel toegevoegd als concept van wat we nog konden implementeren in de database.