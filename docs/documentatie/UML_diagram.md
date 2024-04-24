# UML diagram NAO6

We gaan de robot programmeren in Python.

```mermaid
    classDiagram
        Movement <|-- Walk
        Movement <|-- Gesture

        Speech <|-- callNumber
        Speech <|-- callWon

        class Movement {
            
        }

        class Walk {

        }

        class Gesture {

        }

        class Speech {

        }

        class callNumber {

        }

        class callWon {

        }