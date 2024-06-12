# Sprint Report - Sprint 3

**Opdracht**: NAO Robot  
**Sprint**: Sprint 3  
**Team**: 3  
**Auteurs**:  Brian, Tyler, Amin, Tess, Ana  
**Datum**:  11-6-2024  
**Versie**: v1

---

## Inleiding

**Schrijf hier een inleiding voor het sprint report. Wat is jullie opgevallen tijdens deze sprint?**

We hebben in onze laatste sprint gewerkt aan het samenvoegen van alle losse embedded hardware, dit is ons geluk met behulp van de gemaakte flask api. Onze NAO is voorzien van software die de game host en samen met de vending machine, het bingorat en de Bingo knop een compleet spel vormt. Er waren een paar low priority toevoegingen die we uiteindelijk niet hebben uitgewerkt

## Feedback opdrachtgever

**Wat vond de opdrachtgever van wat jullie gepresenteerd hebben tijdens de Sprint Review? Wat waren de positieve punten (tops) en wat waren de verbeterpunten (tips)?**

- Het project ziet er goed uit. Vooral omdat het een werkend product is waar de mensen al van kunnen genieten

## Feedback doelgroep

- Ouderen zijn niet zo snel, ze vinden het soms moeilijk om onderscheid te maken tussen bepaalde getallen. 
    - De herhaal functie kan dus wel handig zijn

- Misschien kan de robot nog wat enthousiaster bingo roepen! 
    - Uitbundiger zijn bij het winnen van een bingo spel door bewegingen en misschien een liedje/geluid.

- Humor toevoegen in de bingo.

- De stem van de NAO moet wat duidelijker en misschien wat langzamer praten.

- Het had misschien leuk geweest als de robot een meer menselijke stem zou hebben.

## Sprint behaalde doelen

**Welke User Stories hebben jullie af kunnen ronden tijdens deze sprint? Geef een overzicht.**

- Als gebruiker wil ik dat er genoeg bingokaarten zijn voor alle spelers
    - Er is een python script geschreven die elke keer 10 bingo kaarten met unieke qr-code genereert en die toevoegt aan de database.
- Als gebruiker wil ik dat ik een prijs kan winnen als ik bingo heb
    - We hebben een vendingmachine gemaakt die bij elke winst iets van snoepgoed afgeeft.
- Als gebruiker wil ik dat ik op een knop kan drukken als ik bingo heb
    - Er is een uitnodigende box gemaakt waar mensen op moeten drukken om hun bingo te laten valideren.
- Als gebruiker wil ik dat de NAO een QR code kan scannen door middel van zijn ogen, zodat de robot bingokaarten kan herkennen.
    - Er is een qr-code aan de achterkant van de bingo kaarten toegevoegd die de NAO kan scannen met zijn camera.
- Als gebruiker wil ik dat spel data van de bingo in een database kan worden opgeslagen
    - Alle genoemde nummers worden naar de database gestuurd met bij behorende game id, zodat wij weten welke nummers eerst worden genoemd en in welke volgorde.
- Als gebruiker wil ik dat de robot beweegt zodat ik meer interactie heb ermee
    - De NAO die zwaait bij het beginnen van een bingo spel en random op andere momenten.

## User Stories die niet afgerond zijn

**Welke User Stories hebben jullie niet af kunnen ronden tijdens deze sprint? Geef een overzicht, geef ook aan welke aanpassingen jullie hier nog aan moeten maken.**

- Als gebruiker wil ik dat de nao robot kan draaien aan de bingomolen
    - De nao robot is niet in staat om aan het kleine wiel te draaien dat wij hadden. In plaats daarvan draait een stepper motor de bingomolen.
- Als gebruiker wil ik dat de NAO een show kan geven zodat hij de aandacht van andere kan trekken om bingo te spelen
    - De wave die wij hebben toegevoegd is wel iets van beweging, maar we hebben niet een event gemaakt om mensen uittenodigen. Dat komt omdat we geen tijd meer hadden.

## User Stories die gedropt zijn

- Als gebruiker wil ik dat de robot de balletjes kan oppakken dmv een electromagneet
    - Bij het makken van de keyframes is het de eerste keer mogelijk om de bal op te pakken. Alleen heeft de NAO teveel slack om accuraat te blijven nadat alle keyframes uitgevoerd zijn en het later opnieuw moet beginnen.
- Als gebruiker wil ik dat de esp32 een call ontvangt om een ball los te laten in een bakje
    - Deze user storie is afgemaakt alleen hebben wij heb gedropt. Dit is omdat de NAO robot niet accuraat genoeg is.
- Als gebruiker wil ik dat de esp32 een call ontvangt om een ball te pakken met behulp van een elektromagneet
    - De user storie hebben wij af gekregen alleen had deze geen waarde meer aangezien we de elektromagneet het laatste moment niet meer hebben gebruikt.

## Retrospective


Wind:
- Laatste loodjes nog daardoor hadden we motivatie
- We moesten alles afmaken dus niks meer starten
- Duidelijk doel
- Sterk team

Anker:
- Het betoog en zelfontwikkelingsplan (nogsteeds)
- Database dilema (nogsteeds)
- Elektromagneet
- Robot die niet accuraat werkt
- NAO die snel oververhit raakt

Rotsen:
- Dat we niet meer zo veel tijd hadden
- Scrum board toepassen
- http request kwamen soms niet aan
- batterijen leeg

Eiland:  
(voor een fictieve vierde sprint)
- Verbeterd product
- Betere behuizing versieren
- Doos met knoppen werkend krijgen