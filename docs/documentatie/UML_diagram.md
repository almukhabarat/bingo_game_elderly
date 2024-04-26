# UML diagram NAO6

We gaan de robot programmeren in Python. Het is nog een concept waar we kunnen onze classes ongeveer zo indelen.

```mermaid
    classDiagram
        movement <|-- performGesture
        movement <|-- turnWheel
        movement <|-- grabBall
        movement <|-- discardBall

        speech <|-- callNumber
        speech <|-- callWon

        class getNumber {

        }

        class movement {
            
        }

        class performGesture {

        }

        class turnWheel {

        }

        class grabBall {

        }

        class discardBall {

        }

        class speech {

        }

        class callNumber {

        }

        class callWon {

        }

```