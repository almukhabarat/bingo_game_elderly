# NAO Robot

De NAO robot is een humanoïde robot die wordt gebruikt voor onderzoek en educatie. De robot is ontwikkeld door het Franse bedrijf Aldebaran Robotics, dat in 2015 is overgenomen door het Japanse Softbank Robotics. De robot is ongeveer 58 cm hoog en weegt ongeveer 5 kg. De NAO robot is een van de meest gebruikte robots in onderzoek en onderwijs. De robot is uitgerust met verschillende sensoren, waaronder camera's, microfoons, een gyroscoop en een accelerometer. De robot kan worden geprogrammeerd met behulp van verschillende programmeertalen, waaronder Python en C++.

![NAO Robot](nao-robots.png)

## Mogelijkheden

Wanneer je gebruik wilt maken van deze robot zou je aan het volgende toepassingen kunnen denken:

- Je wilt een toepassing maken waarmee de robot een interactie aan gaat met de gebruiker.
- Je wilt een toepassing waarbij bewegingen en omgang met de robot centraal staan, maar geen grote afstanden aflegt.
- Je wilt de robot laten communiceren met de gebruiker door audio en beweging.
- Je wilt vooral gebruik maken van sensoren/actuatoren die in de robot aanwezig zijn.

Met deze robot zijn er ook beperkingen, zoals:

- De robot is niet geschikt voor het afleggen van grote afstanden.
- De robot is al gebouwd: Er is weinig speelruimte voor het aanpassen van de hardware op de robot zelf.
- Audiofuncties zijn beperkt: De robot heeft moeite met het verstaan van spraak in een rumoerige omgeving.

## Documentatie

Voor de NAO-robot heeft de fabrikant, Softbank Robotics / Aldebaran, documentatie beschikbaar gesteld in de vorm van verschillende handleidingen.

### NAO - User Guide

Deze handleiding gaat in op het gebruik van de NAO-robot voor de eerste keer. De robot die jullie gebruiken is echter al geconfigureerd, dat hoeven jullie dus niet meer te doen, maar deze pagina geeft ook goede informatie over het dagelijks gebruik van de robot. Lees dit goed door voordat je met de robot aan de slag gaat.

➤&nbsp; [NAO - User Guide](http://doc.aldebaran.com/2-8/family/nao_user_guide/index.html)


### NAO - Developer Guide

Deze pagina is bedoeld voor technische ondersteuning. Je kan hier informatie vinden over de specificaties van bijvoorbeeld de aanwezige hardware of over de kinematica.

➤&nbsp; [NAO - Developer Guide](http://doc.aldebaran.com/2-8/family/nao_technical/index_naov6.html)



### NAOqi - Developer guide

NAOqi is de naam van het software platform wat op de robot draait en wat wordt gebruikt om de robot te besturen. Het 'NAOqi Framework' is het programmeer framework om de NAO te programmeren.

Er zijn Software Development-Kits (SDK) beschikbaar voor de volgende programmeertalen:

![NAOqi SDK supported languages](supported_language.png)

- Python
- C++
- Javascript
- ROS

➤&nbsp; [NAOqi - developer guide](http://doc.aldebaran.com/2-8/index_dev_guide.html)


## Programmeren van de NAO

De NAO-robot moet je zien als één grote API (Application Programming Interface). Op de robot draaien allemaal verschillende services, deze zijn allemaal verantwoordelijk voor hun eigen taken. Zo is er een service voor het praten, bewegen, geluid opnemen, ... !

➤&nbsp; [Overzicht van API's](http://doc.aldebaran.com/2-8/naoqi/index.html)

De software die jullie ontwikkelen zal voornamelijk bestaan uit het aanroepen van deze services. Dit kan in verschillende programmeertalen, zoals Python, C++, Javascript of ROS.
Om je daarmee te helpen maak je gebruik van de SDK's die beschikbaar zijn voor deze talen.


## Choregraphe

Choregraphe is een software programma waarmee je de NAO-robot kan programmeren. Het is een visuele programmeeromgeving waarbij je blokken aan elkaar kan koppelen om zo een programma te maken. Het is een handige tool om snel en eenvoudig een programma te maken voor de NAO-robot.

![Choregraphe](choregraphe.jpg)

Het is niet de bedoeling om jullie software te ontwikkelen met of voor Choregraphe, maar het is wel een handige tool om snel en eenvoudig een beeld te krijgen van wat de robot doet. Handig dus voor het debuggen.

➤&nbsp; [Choregraphe](https://www.aldebaran.com/en/support/nao-6/downloads-softwares)


## Oudere instructie video's

In het verleden zijn er veel instructie video's gemaakt over het programmeren van de NAO-robot. Deze video's zijn nog steeds relevant en kunnen jullie helpen bij het programmeren van de robot. Let er wel op dat er in deze video's gebruik wordt gemaakt van de programmeertaal Java, terwijl deze niet meer wordt ondersteund door de fabrikant.

➤&nbsp; [Hello World](https://youtu.be/9mculonRz2Y)

➤&nbsp; [Posture](https://youtu.be/yrUKAk0nAQw)

➤&nbsp; [Events](https://youtu.be/We7gP1_CSLU)

➤&nbsp; [Camerabeelden & OpenCV](https://youtu.be/2K6w8tfPEOQ)

{{ mdocotion_header('/assets/nao.png') }}