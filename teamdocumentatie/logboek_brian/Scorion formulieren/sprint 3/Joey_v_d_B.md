# Expert review sprint 3 | Joey van de Bie

K1: OOP & Database, Ik wil mijn OOP code laten zien in python en ook de database integratie. 

Uitleg OOP

Encapsulatie -> In de NaoInit class worden de ALProxy api`s aangeroepen met private variables, deze worden later gebruikt in een andere class.

Overerving -> class Movement(NaoInit), deze class neemt de variabelen en methodes over van de NaoInit class om hiermee de class/het object verder uit te werken.

Polymorfisme -> wordt niet echt toegepast in deze code volgens mij aangezien er een geen basis functie is gedefinieerd in de NaoInit class die wordt overschreden in een andere class.

Abstractie -> Wordt toegepast aangezien de NaoInit class zelf niet wordt gebruikt om een object te creëren maar andere classes wel afhankelijk zijn van deze class.

Database

Ik wil mijn ERD laten zien en de configuratie.

K3: Ik wil de netwerk infrastructuur van ons project laten zien en een overzicht van alle onderdelen binnen het project.
HTTP long polling en API`s.

K4: Prijsautomaat, we hebben een prijsautomaat gemaakt die snoepjes kan afgeven zodra er een winnaar bekend is.
Ik wil een demonstratie tonen van onze prijsautomaat.

K5: Arduino code voor stepper motor. Ik had hiervoor een simpele flask library hiervoor uitgewerkt zodat mensen die aan andere actuatoren hier gebruik van kunnen maken. 

Feedback:

K1: Houd rekening met coding conventions wat betreft OOP. Sommige methodes staan niet in de juiste class, zet classes in losse bestanden.

K3: Sequence diagram moet nog meer verduidelijking hebben, de HTTP long polling loop was niet duidelijk omschreven. Er moet bijstaan dat het om een timeout loop gaat van 30 seconden. Ik had mijn eigen systeem documentatie laten zien, deze zag er goed uit, maar uiteindelijk is moet deze uitgewerkt worden in een UML deployment diagram.

K4: Voor documentatie van actuator ontbrak het aansluitschema, bronvermelding en/of BOM.

K5: Ik heb de functionaliteit van de prijsautomaat proberen te laten zien, maar de batterij was helaas op. Ik had een library geschreven voor het versturen en ontvangen van HTTP requests, ook hierbij moest ik rekening houden met coding conventions.

