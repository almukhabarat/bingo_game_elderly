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

We hebben in onze laatste sprint gewerkt aan het samenvoegen van alle losse embedded hardware, dit is ons geluk met behulp van de gemaakte flask api. Onze NAO is voorzien van software die de game host en samen met de vending machine, het bingorat en de Bingo knop een compleet spel vormt.

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
    - De nao robot kan niet draaien aan het kleine wiel dat wij hadden.
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

**Voeg hier een afbeelding toe van jullie retrospective. Beschrijf wat jullie hebben besproken en wat jullie gaan aanpassen voor de volgende sprint.**


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
(fictief vierde blok)
- Verbeterd product
- Betere behuizing versieren
- Doos met knoppen werkend krijgen

## STARRT

### Situatie
De situatie was een sprint van 2/3 weken sprint 3 om precies te zijn. We moesten het project afmaken dat is waarom de taken onstonden. De mensen die er bertrokken waren bij sprint 3 waren Tess, amin, brian, tyler

### Taak
De lastige opgave die ik/wij moesten doen is dat alle esps, pi en met database met elkaar moesten praten en dat het ook op volgorde moest gaan. Het spel moest goed lopen qua nummers. De behuizingen van dingen dingen maken dus meer het fysieke dingen en de documentatie van alles maken.
Mijn verantwoordelijkheid was de bingoknop en de startknop, duidelijkheid over de database. Dat de robot bingo kon leiden zonder problemen. Ik wilde bereieken dat ik een waardige teammate was die bezig was en het project naar voren hielp.


### Actie/Aanpak
Vooral communiceren heb ik genruikt als ik dingen lastig vond mijn teammates om hulp vragen nadat ik het internet had bezocht. Ik owu eerst het even zelf proberen als ik het nietkon vinden of toch niet zo goed begrijpen dan zou vroeg ik me teammates omdat hun toch wat meer knowledge al hebben en anders vroeg ik de docent zodat ik de andere ook meer knowledge kon geven. Ik vind dat me aanpak goed was want daardoor communiceerde ik waar ik mee bezig was maar ook liet ik zien dat ik leerlgierig ben.

### Resultaat
Ik denk dat ik een beetje de software taken van de embedded  heb overgenomen en dat tess dan de documentatie ervoor had geschreven en dat ik de documentatie erbij dan ging aanpassen. Het resultaat voldeed aan requirments. Ik was tevreden met het resultaat vond het alleen jammer dat de bingo knop af en toe glitchen. Ik ben tevreden omdat ik mijn best heb gedaan en alles toch wel goed is afgelopen qua het project. Ik vind dat we een mooi project hebben neergelegd.

### Reflectie
Mijn aanpak was effectief ik had altijd alles op tijd af en het was altijd code en of dingen die we tot het eind hebben gebruikt. Ik heb daardoor ook meer geleerd dan de hele tijd tegen een muur trappen en gewoon om hulp te vragen. Ik heb geleerd dat ik vaker moet documenteren zo begrijp ik het ook beter.


### Transfer
Je kan dit in de toekomst aanpassen op denk ik elk moment ik denk dat ik dan ook steeds beter leer om het antwoord te vinden waardoor ik minder snel hulp nodig heb. Dat is dan ook wat ik ook meer wil leren het zelf weten. 

## Smart leerdoel

### Specifiek
Mijn doel is naast dat ik geautomatiseerd documentatie wil schrijve ook betere documenatie schrijven voor mijn coderen, ook graag met database meer werken zodat ik dat beter onder de knie heb. De doel komt uit zelf reflectie en dat ik daar vooruitgang wil hebben. Het is een leerdoel voor mij omdat het iets is wat ik beter moet leren. Ik denk dat ik tegen dingen lopen omdat het geen automatisme is het moet zeg maar de eerste stap zijn van mijn aanpak. Ik wil bereiken dat ik mooie codes kan schrijven zonder enig probleem met goeie documentatie en database onder de knie heb met communicaties tussen embedded systemen. 

### Meetbaar
Ik begin eerst met documenteren en plannen hoe ik het ga aanpakken daarna ga ik mijn code en of database maken. Andere kunnen het vstellen door mijn code makkelijker te begrijpen en te kunnen herbruiken. Mijn doelen check ik door vaker naar de docent gaan. 

### Acceptabel
Ik sta achter het doel want ik denk dat het het belangrijkst is van coderen naast de code zelf. Ik wil zelf eraan werken zodat ik evalueer als icter. Ik stel dit doel vanuit mijn toekomstige persoon. Het is nodig voor de toekomstige taken.

### Realistisch
Ik basseer dit op de eerste half jaar van mijn tweede jaar school. De mogelijkheden voor mijn doel is best groot daarom wil ik er ook aan werken. Hulpmiddelen zijn voor mij mijn docenten en me medestudenten. Ik denk de tijd dat ik in school kan steken vanwege thuissituatie, werk etc maakt het wat lstig maar daar will ik ook aanwerken. Ik heb zelf discipline nodig om me doel te bereiken.

### Tijdgebonden
Mijn eerste half jaar van mijn tweede jaar dus de 6 maanden dat we dan nog projecten hebben in die tijd zou ik het volledig onder de knie wil hebben.