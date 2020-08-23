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
  - Lisätä, muokata ja poistaa tunteja
  - Vahvistaa peruskäyttäjän taitotason
  - Seurata omille tunneilleen ilmoittautuneita henkilöitä
- Ylläpitäjä voi lisäksi:
  - Lisätä, muokata ja poistaa tunteja
  - Seurata kaikille tunneille ilmoittautuneita henkilöitä (esim. osallistujalistojen tulostus) 

## 3. välipalautus:

Sovellus Herokussa:
https://tranquil-tundra-57661.herokuapp.com/

Admin-toimintojen testaamista varten käyttäjätunnus admin ja salasana admin

Opettaja-toimintojen testaamista varten käyttäjätunnus opettaja ja salasana opettaja

- Tämän hetken toiminnallisuudet:
  - Toimintojen pitäisi huomioida eri käyttäjäroolit
  - Kirjautumaton käyttäjä:
    - Rekisteröityminen, kirjautuminen, tuntitarjonnan selaaminen
  - Kirjautunut käyttäjä (edellisten lisäksi):
    - Tuntien varaus ja peruminen, ml. eri vaatimusten tarkistus
    - Sarjakortin ostaminen
    - Omien varausten tarkastelu
    - Omien tietojen tarkastelu (osittain)
  - Opettaja (edellisten lisäksi):
    - Tuntien lisäys
    - Käyttäjän tason vahvistus
  - Admin (edellisten lisäksi):
    - Käyttäjän roolin muuttaminen

- Vielä puuttuvia toimintoja:
  - Tuntien osallistujien listaus. Tarkoitus on, että opettaja voi nähdä omille tunneilleen ilmoittauneet ja admin kaikille tunneille ilmoittautuneet
  - Opetettavien tuntien listaus
  - Tuntien muokkaus ja poisto

- Muita huomioita:
  - Syötteiden oikeellisuuden tarkastelu edelleen osittain vaiheessa. Odottamaton syöte saattaa siis aiheuttaa virhetilanteen, jota ei käsitellä.
  - Tietoturva-asiat osittain vaiheessa
  - Taulukot tulostuvat varsin ahtaasti, css-tiedosto muutenkin vaiheessa

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
