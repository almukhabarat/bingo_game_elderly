# Bingokaarten

Voor het spelen van de bingo, zijn er natuurlijk bingokaarten nodig.

![alt text](bingokaart.png)

Wij hebben ervoor gekozen om de kaarten 3 bij 3 vakjes te maken, zodat het spel niet te lang duurt.
De kaarten worden uitgeprint op papier en daarna gelamineerd. Op deze manier kunnen de kaarten hergebruikt worden door er met whiteboardmarker op te schrijven.

Op de achterkant staat een qr code, als deze gescant word door de nao robot, kan deze zien welke nummers er op de kaart staan.

De bingokaarten worden gegenereerd met een python script.

In het script kan aangepast worden hoeveel kaarten er moeten worden gegenereerd. Ook kan de hoeveelheid getallen aangepast worden.

De code bestaat uit verschillende classes:

- bingo_card_generator
- qr_code_generator
- pdf_generator
- bingo_game

