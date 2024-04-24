# Hoe gebruik je de (python) SDK voor het programmeren van de NAO6 robot. 

Voor het programmeren van de NAO6 robot kun je gebruik maken van SDK's voor verschillende programmeer talen. Je kunt de NAO6 robot programmeren in zowel python als C++. We hadden initieel besloten om python te gebruiken voor het programmeren van de robot. Ik weet niet of mensen al veel ervaring hebben met python, maar omdat de NAO SDK voor python vrij uitgebreid is, en omdat het een eenvoudige taal is om mee te programmeren denk ik dat het handig is om python voor dit project te gebruiken. 

## Hoe installeer je de NAO python SDK?

```
Let op! voor de NAO python SDK moet je een oudere versie (versie 2) van python hebben geïnstalleerd. De nieuwste versie van python (versie 3.12.3 op het moment van schrijven) werkt niet.
```

Om gebruik te maken van de NAO python SDK, moet je python op je werkcomputer installeren. Ik maak zelf gebruik van python 2.7.18, deze kun je hier downloaden:

---

https://www.python.org/downloads/release/python-2718/ 

Voor Windows kun je het best gewoon de `Windows x86-64 MSI installer` downloaden.

---

Nadat je deze hebt geïnstallleerd, kun je de NAO python SDK downloaden en installeren. 
---

Python SDK voor het programmeren van de NAO6 robot
(Dit is voor Windows)

https://community-static.aldebaran.com/resources/2.8.7/Python+SDK/pynaoqi-python2.7-2.8.7.4-win64-vs2015-20210818_210634.zip

---

Nadat je de zip hebt gedownload kun je deze uitpakken op je C: schijf. Het is handig om de map die je hebt uitgepakt een duidelijke naam te geven:

Ik heb de map `pynaoqi-python2.7` genoemd.

Om de python SDK te gebruiken moet je eerst nog extra omgevingsvariabelen toevoegen.

`Voor Windows 11:`

1. Type in de zoekbalk, en open "systeem".
2. Klik vervolgens op en Geavanceerde systeeminstellingen.
3. Op de geavanceerd tab klik je op "omgevingsvariabelen".
4. In gebruikersvariabelen voeg je een nieuwe variabele toe, deze noem je "PYTHONPATH". In het veld "Waarde van" voeg je het volgende pad toe: `C:\mapnaam van je python SDK\lib` <br>
*. Ik heb zelf dus "C:\pynaoqi-python2.7\lib"
5. Nu heb je de python SDK geïnstalleerd. Om dit te controleren kan je de python IDE (IDLE (python GUI)) openen en de installatie van de SDK checken in de IDLE terminal met `import naoqi`. Als er geen foutmeldingen worden gegeven is de NAO python SDK successvol geïnstalleerd.

---

## Hoe gebruik je de Python SDK in Visual Studio Code

Je kunt de Python SDK gebruiken in Microsoft Visual Studio Code om daarin te programmeren en te communiceren met de robot.

Je moet als eerst hiervoor de python extensie op Microsoft Visual Studio Code hebben geïnstalleerd *(deze is meestal voorgeïnstalleerd dus deze stap kun je in de meeste gevallen negeren)*.

Nogmaals, de NAO python SDK kan alleen in oudere versies van python gebruikt worden.

Je kunt in Visual Studio Code een python interpreter kiezen, oftewel, een specifieke python versie die je hebt geïnstalleerd.

1. Klik op de python versie in je Visual Studio balk rechtsonder.
<img src="images/VSC_balk_1.png">

2. Vervolgens klik je op `Enter interpreter path` in het menu dat boven verschijnt.

3. Voer hier het pad van je python 2.7 installatie, deze is standaard: `C:\Python27`.

4. Nu kun je de python SDK in Visual Studio Code gebruiken.







