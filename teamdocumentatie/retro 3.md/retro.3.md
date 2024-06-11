# Sprint Report - Sprint 2

**Opdracht**: NAO Robot
**Sprint**: Sprint 2
**Team**: 3
**Auteurs**:  Brian, Tyler, Amin, Tess, Ana
**Datum**:  24-5-2024
**Versie**: v1

---

## Inleiding

**Schrijf hier een inleiding voor het sprint report. Wat is jullie opgevallen tijdens deze sprint?**

We hebben heel snel heel veel voor elkaar gekregen. Het programmeren van de NAO verloopt goed. En we hebben verschillende verbeteringen gemaakt aan ons productdesign. Het schrijven van een betoog hindert ons uiteindelijk niet zo veel. We hebben ook veel verschillende toevoegingen gemaakt qua embedded hardware.

## Feedback opdrachtgever

**Wat vond de opdrachtgever van wat jullie gepresenteerd hebben tijdens de Sprint Review? Wat waren de positieve punten (tops) en wat waren de verbeterpunten (tips)?**

Het ontwerp moet mooier en meer presentabel. De vending machine moet een "klepje"om de prijs een verassing te maken. Ook moet de NAO meer feestelijk zijn. De rest van het project zag er goed uit. We konden veel presenteren en we hadden een goede demostratie.1

## Sprint behaalde doelen

**Welke User Stories hebben jullie af kunnen ronden tijdens deze sprint? Geef een overzicht.**

- Als gebruiker wil ik dat de esp32 een call ontvangt om een bal los te laten in een bakje
- Als gebruiker wil ik dat de esp32 een call ontvangt om een bal te pakken met behulp van een elektromagneet
- Als gebruiker wil ik dat de NAO kan draaien aan de bingomolen
- Als gebruiker wil ik dat er genoeg bingokaarten zijn voor alle spelers
- Als gebruiker wil ik dat ik een prijs kan winnen als ik bingo heb
- Als gebruiker wil ik dat ik op een knop kan drukken als ik bingo heb
- Als gebruiker wil ik dat de NAO een QR code kan scannen door middel van zijn ogen, zodat de robot bingokaarten kan herkennen
- Als gebruiker wil ik dat spel data van de bingo in een database kan worden opgeslagen

## User Stories die niet afgerond zijn

**Welke User Stories hebben jullie niet af kunnen ronden tijdens deze sprint? Geef een overzicht, geef ook aan welke aanpassingen jullie hier nog aan moeten maken.**

- Als gebruiker wil ik dat de robot beweegt zodat ik meer interactie heb ermee
- Als gebruiker wil ik dat de esp32 een call ontvangt om een ball los te laten in een bakje
- Als gebruiker wil ik dat de esp32 een call ontvangt om een ball te pakken met behulp van een elektromagneet
- Als gebruiker wil ik dat de nao robot kan draaien aan de bingomolen
- Als gebruiker wil ik dat de robot de balletjes kan oppakken dmv een electromagneet
- Als gebruiker wil ik dat de NAO een show kan geven zodat hij de aandacht van andere kan trekken om bingo te spelen

## Nieuwe User Stories

**Welke nieuwe User Stories hebben jullie opgesteld voor de volgende sprint?**

- Als gebruiker wil ik dat er genoeg bingokaarten zijn voor alle spelers
- Als gebruiker wil ik dat de nao robot kan draaien aan de bingomolen
- Als gebruiker wil ik dat ik op een knop kan drukken als ik bingo heb.

## Prioriteiten

**Wat is belangrijk geweest afgelopen sprint, wat is belangrijk voor de volgende sprint?**

Deze sprint was het belangrijk om alle losse onderdelen werkend te krijgen. De systemen zoals de NAO, database en verschillende ESP's kunnen zo hun taken uitvoeren. Voor volgende sprint is het belangrijk om een MVP te maken.

## Retrospective

**Voeg hier een afbeelding toe van jullie retrospective. Beschrijf wat jullie hebben besproken en wat jullie gaan aanpassen voor de volgende sprint.**

![Retrospective sprint 2](Retrospective2.jpg)

Wind:

- inspiratie en goede documentatie
- genoeg tijd
- duideloijk doel

Anker:

- het betoog en zelfontwikkelingsplan
- database dilema

Rotsen:

- te veel willen
- te veel inspiratie
- scrum board toepassen

Eiland:

- verbeterd product
- behuizing versieren
- mooie presentatie op de beurs

---
---

# Eigen reflectie op sprint 2 (Brian Kirchoff)

***Wat vond ik bij mezelf goed gaan tijdens deze sprint?***

Het SMART doel dat ik in de vorige sprint voor mezelf had opgesteld was dat ik meer en vooral beter wilde communiceren met mijn groepje. In sprint 1 had ik hier nog veel moeite mee omdat ik mijn groepje nog goed moest leren kennen. Bij mij duurt het altijd even voordat ik gewend raak aan mensen en hoe ik weet hoe ik met hen moet communiceren. Ik vind zelf dat ik tijdens deze sprint meer vragen aan mijn teamgenoten heb gesteld en dat ik zelf ook meer input en feedback heb gegeven. Een paar dagen geleden kwamen we samen nog bijeen om te bespreken wat we wilde laten zien tijdens de sprintreview van sprint 2 en waar we nog aan moesten werken. 

Daarnaast ben ik zelf tevreden met de progressie die ik heb gemaakt tijdens deze sprint. Ik bleef in het begin van de sprint een beetje hangen bij het database ontwerp dus op ik ging me daarom meer focussen op de snoep automaat en het netwerk gedeelte van ons project. Hierin heb ik aardig wat progressie geboekt.

## Waar kan ik aan werken in de volgende sprints? (door middel van een SMART doel)

Ik wil werken aan documenteren voor de volgende sprint. Niet alleen heb ik aan de hand van onze progressie van ons project nu veel informatie om te documenteren, we hebben de documentatie ook echt nodig omdat we bijvoorbeeld straks alle embedded apparaten via een webserver met elkaar gaan verbinden. Het is dus handig dat iedereen een overzicht heeft van bijvoorbeeld onze webserver setup.

---

# Persoonlijke SMART doel

## Specifiek

Ik wil beter en meer documenteren zodat mensen in mijn groepje of de opdrachtgever een beter overzicht hebben over het project en (meer) inzicht kunnen krijgen over hoe het project in elkaar zit.

## Meetbaar

Ik wil documentatie schrijven over de netwerk interactie tussen de NAO robot en de microcontrollers met de webserver en elkaar. Ik wil het visueel gaan documenteren met mermaid door middel van flowcharts and sequence diagrams. Daarnaast wil ik ook documentatie hebben geschreven over mijn code en de python flask api en hoe deze interacteren met de microcontrollers. 

## Acceptabel

Met documentatie schrijven wil ik vooral ingaan op het netwerk aspect, ik zou dit namelijk graag visueel willen documenteren door middel van schematische tekeningen. Ik heb dit nog niet veel gedaan in het algemeen en vooral niet tijdens dit blok. Met code documentatie bijvoorbeeld hoef ik geen uitgebreid verslag te schrijven.

## Realistisch

Het is een realistisch doel aangezien ik soms UML documenteer met mermaid. Ik zou graag willen leren hoe een C4 diagram of een sequence diagram werkt, en hoe ik deze kan maken in mermaid.

## Tijdsgebonden

In de periode van Sprint 3 heb ik 2 expert reviews. Mijn idee was dus dat ik dan mijn SMART doel wil bereiken rond 7 juni. Op 28 mei heb ik een expert review met Mats dus dan kan ik al vrij snel wat feedback ontvangen.

---