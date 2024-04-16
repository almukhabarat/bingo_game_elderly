# Little Endian

De [Pepper](../robots/pepper.md) en de [Nao](../robots/nao.md) robots zijn ontworpen om te lijken op mensen en voldoen daarmee aan een klassiek beeld van een robot. Echter hoeft een robot niet per se op een mens te lijken. 

Waar de [Pepper](../robots/pepper.md) en de [Nao](../robots/nao.md) al kant en klaar zijn is de "Little Endian" geen product dat te koop is. Het is een concept dat is bedacht door studenten van de Hogeschool van Amsterdam.

??? note "Wat is de "Little Endian"?"

    De `Little Endian` is een kleine "rover" robot die is ontworpen door studenten HBO-ICT om gebruikt te worden door kinderen in de leeftijd van 8 tot 12 jaar. De robot is ontworpen om kinderen te leren programmeren en om ze te laten zien hoe leuk techniek kan zijn. In het originele project is de `Little Endian` te besturen met een op blockly gebaseerde programmeeromgeving.

    Bij het ontwerpen van de `Little Endian` stond toegankelijkheid voorop. Kinderen kunnen hem zelf in elkaar zetten en de onderdelen zijn allemaal zo goedkoop mogelijk gekozen.

De basis van de Little Endian is een ESP gebaseerde microcontroller die twee motoren aanstuurt waaraan wielen zijn bevestigd, zodat deze robot kan rijden. De robot is voorzien van een pen waarmee hij kan tekenen. 

Op dit moment is de "Little Endian" meer een idee dan een product. Het is een concept dat nog verder uitgewerkt moet worden.

> **Je kiest deze opdracht als je echt een technische uitdaging zoekt en het leuk vindt om een robot helemaal vanaf de grond op te bouwen.**

## Toepassingen

De "Little Endian" is een robot die kan tekenen. Dit kan je op verschillende manieren inzetten. Denk bijvoorbeeld aan:

- Kinderen leren om te gaan met robots en techniek
    - [Little Endian Kit](https://iot.dev.hihva.nl/2021-2022-feb-jun/group-project/coderdojo-little-endian/little_endian/)
- Ouderen interactief laten tekenen met robots
    - [Drawing together](https://iot.dev.hihva.nl/2022-2023-sep-jan/group-project/vitalityandaging-drawing-together/)
    - [Collaborative drawing](https://human-robot-collaborative-drawing-iot-2023-2024--c1298d6f5160f3.dev.hihva.nl/)

## Materialen

- ESP32-C3 microcontroller
- 2x [DC motor](https://www.aliexpress.com/item/1005005605678253.html?spm=a2g0o.order_list.order_list_main.15.7fb41802Ks66YR) of stappenmotor ([28BY-J](https://www.aliexpress.com/item/1005005486356862.html?spm=a2g0o.productlist.main.5.7af74c4fjmXmL4&algo_pvid=4a73c262-c568-4247-91f5-193df0b9b11c&algo_exp_id=4a73c262-c568-4247-91f5-193df0b9b11c-2&pdp_npi=4%40dis%21EUR%214.14%212.11%21%21%2131.22%2115.92%21%40211b600817131850149845758ec081%2112000033273129748%21sea%21NL%21162207786%21&curPageLogUid=A9oOY2vnrfav&utparam-url=scene%3Asearch%7Cquery_from%3A))
- Dual channel DC motor controller ([HW-627](https://www.aliexpress.com/item/1005006158100008.html?spm=a2g0o.order_list.order_list_main.30.7fb41802Ks66YR))
- [Wielen](https://www.aliexpress.com/item/1005005962566462.html?spm=a2g0o.order_list.order_list_main.25.7fb41802Ks66YR)
- Raspberry Pi

Uiteraard ben je niet gebonden aan deze onderdelen en is het mogelijk om andere onderdelen te gebruiken.

## Uitdagingen

Om de Little Endian te realiseren zijn er een aantal uitdagingen die je moet overwinnen:

- **Motion control:** Hoe weet je waar de robot is en hoe kan je de robot precies laten tekenen wat je wilt?
- **energie:** De robot moet gevoed worden door een batterij. Hoe zorg je voor goede energievoorziening?
- **communicatie:** Hoe communiceert de robot met de gebruiker en met andere systemen?

Veel van deze uitdagingen zijn al in voorgaande projecten aangegaan door andere studenten. Leer vooral van wat je voorgangers hebben opgeleverd.

## Documentatie

Je zal toegang krijgen tot relevante gitlab repositories van vorige studententeams.

{{ mdocotion_header('/assets/little-endian.jpg') }}