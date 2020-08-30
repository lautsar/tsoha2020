# Varaussovellus

Sovelluksessa toteutetaan yksinkertainen tuntienvarausjärjestelmä, jolla on kolmenlaisia käyttäjiä: ylläpitäjiä, opettajia ja peruskäyttäjiä. Järjestelmässä on tunteja, joilla on vaikeusaste ja maksimiosallistujamäärä. Adminit ja opettajat voivat lisätä ja poistaa tunteja järjestelmästä.

Kuka tahansa voi selata tunteja ja rekisteröityä käyttäjäksi. Jokaisella rekisteröityneellä käyttäjällä on määritetty profiilissa taitotaso, ja hän voi ilmoittautua vain sellaisille tunneille, joiden vaikeusaste on sama tai pienempi kuin hänen taitotasonsa. Opettaja tai admin vahvistaa taitotason ennen kuin se astuu voimaan. Käyttäjällä on myös oltava voimassa oleva sarjakortti, jotta hän voi varata tunteja. Käyttäjä voi myös perua ilmoittautumisensa.

Opettaja ja admin voivat vahvistaa peruskäyttäjän taitotason. He voivat myös seurata tunneille ilmoittautuneita henkilöitä. Opettaja näkee vain omille tunneilleen ilmoittautuneet henkilöt, mutta admin näkee kaikille tunneille ilmoittautuneet henkilöt. Admin voi myös muuttaa muiden käyttäjien roolia.

Sovellus Herokussa:
https://tranquil-tundra-57661.herokuapp.com/

Admin-toimintojen testaamista varten käyttäjätunnus admin ja salasana admin

Opettaja-toimintojen testaamista varten käyttäjätunnus opettaja ja salasana opettaja

## Sovelluksen toiminnot
  - Kirjautumaton käyttäjä:
    - Rekisteröityminen, kirjautuminen, tuntitarjonnan selaaminen
  - Kirjautunut käyttäjä (edellisten lisäksi):
    - Tuntien varaus ja peruminen, ml. eri vaatimusten tarkistus
    - Sarjakortin ostaminen (varsinainen ostaminen ei kuulu sovelluksen piiriin, vaan "ostetut" kerrat siirtyvät suoraan käyttäjän tilille)
    - Omien varausten tarkastelu
    - Omien tietojen tarkastelu
  - Opettaja (edellisten lisäksi):
    - Tuntien lisäys
    - Käyttäjän tason vahvistus
    - Opetettavien tuntien listaus ja poisto
    - Opetettavien tuntien osallistujien listaus
  - Admin (edellisten lisäksi):
    - Käyttäjän roolin muuttaminen
    - Kaikkien opettajien tuntien listaus ja poisto
    - Kaikkien opettajien tuntien osallistujien listaus
