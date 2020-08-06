# Varaussovellus

Sovelluksessa toteutetaan yksinkertainen tuntienvarausjärjestelmä. Sovelluksella on kahdenlaisia käyttäjiä: ylläpitäjiä ja peruskäyttäjiä. Ylläpitäjä voi lisätä varausjärjestelmään tunteja, joilla on vaikeusaste ja maksimiosallistujamäärä. Jokaisella rekisteröityneellä käyttäjällä on määritetty profiilissa taitotaso, ja hän voi ilmoittautua vain sellaisille tunneille, joiden vaikeusaste on sama tai pienempi kuin hänen taitotasonsa. Käyttäjällä on myös oltava voimassa oleva sarjakortti, jotta hän voi varata tunteja. Käyttäjä voi myös perua ilmoittautumisensa.

Perustoiminnot lyhyesti:
- Kuka tahansa voi selata tuntitarjontaa
- Rekisteröitynyt käyttäjä voi:
  - Selata tuntitarjontaa
  - Varata tunteja tietyin edellytyksin
  - Perua varaamiaan tunteja
  - "Ostaa" sarjakortteja. Varsinainen ostaminen (esim. maksutapahtumat) eivät kuulu tämän sovelluksen piiriin.
  - Seurata omia ilmoittautumisiaan ja muita tietojaan
- Opettaja voi lisäksi:
  - Vahvistaa peruskäyttäjän taitotason
  - Seurata omille tunneilleen ilmoittautuneita henkilöitä
- Ylläpitäjä voi lisäksi:
  - Lisätä, muokata ja poistaa tunteja
  - Lisätä tai poistaa yksittäisiä henkilöitä tunneilta
  - Seurata kaikille tunneille ilmoittautuneita henkilöitä (esim. osallistujalistojen tulostus) 

## 2. välipalautus:

Sovellus Herokussa:
https://tranquil-tundra-57661.herokuapp.com/

- Ensimmäisiä toimintoja aloitettu:
  - Rekisteröityminen, kirjautuminen sisään ja ulos
  - Tuntien lisääminen
  - Tuntien listaus
  - Tuntien varaaminen (ei huomioi vielä taitotasoa tai ilmoittautuneiden määrää)
  - Sarjakortin ostaminen

- Tässä kohdassa vielä selkeitä puutteita:
  - Syötteiden oikeellisuuden tarkastelu
  - Virhetilanteiden käsittely
  - Käyttäjäroolien ja -oikeuksien huomiointi
  - Sovelluksen ulkonäkö ja käytettävyys
