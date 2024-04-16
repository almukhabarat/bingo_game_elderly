# Pepper Robot

De Pepper robot is een humanoïde robot die ontwikkeld is door het Japanse bedrijf Softbank Robotics. De robot is ontworpen om te communiceren met mensen en kan dit doen door middel van spraak, gezichtsherkenning en beweging. Pepper is een sociale robot en wordt vaak ingezet in de retail, zorg en educatie.

![Pepper Robot](pepper_whole.png)

## Mogelijkheden

Wanneer je gebruik wilt maken van deze robot zou je aan het volgende toepassingen kunnen denken:

- Je wilt een toepassing maken waarmee de robot een interactie aan gaat met de gebruiker in bredere ruimtes.
- Je wilt een toepassing waarbij interactie met een tablet of scherm een grote rol speelt.
- Je wilt een toepassing waarbij de robot zich beweegt in een beperkte omgeving.

Met deze robot zijn er ook beperkingen, zoals:

- De robot is niet geschikt voor het afleggen van grote afstanden.
- De robot is al gebouwd: Er is weinig speelruimte voor het aanpassen van de hardware op de robot zelf.
- De robot kan moeilijk omgaan met drukke omgevingen.

## Documentatie

Voor de Pepper robot is soortgelijke documentatie beschikbaar als voor de NAO robot alleen is deze niet meer relevant. Onze Pepper robots draaien namelijk software op twee lagen:

- Pepper robot: De robot zelf, met de hardware en de software die de robot bestuurt.
- Android tablet: De tablet die op de borst van de robot is gemonteerd, waarop de applicaties draaien.

De robot wordt aangestuurd door de tablet die op de borst van de robot is gemonteerd. De tablet draait Android en de applicaties die op de robot draaien zijn Android applicaties. De robot zelf is een black box, waarbij de software niet toegankelijk is voor de gebruiker. Er zijn wel API's beschikbaar om de robot aan te kunnen sturen vanuit de Android applicaties.

### Android development

Je moet dus een Android Applicatie ontwikkelen om de robot aan te sturen. Om de robot aan te sturen gebruik je de qiSDK, hiervoor is informatie beschikbaar via:

- [qiSDK](https://qisdk.softbankrobotics.com/sdk/doc/pepper-sdk/index.html)
- [Android Development](https://developer.android.com/)

Android applicaties kan je ontwikkelen in Java of Kotlin. De qiSDK is een library die je kan toevoegen aan je Android project om de robot aan te sturen. Je kan dus goed bronnen van internet gebruiken over Android development om je project te realiseren.


{{ mdocotion_header('/assets/pepper_banner.png') }}