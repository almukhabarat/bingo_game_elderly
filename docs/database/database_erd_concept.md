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

## v3

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



