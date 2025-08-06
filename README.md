# subtitle-fix-py
Ovaj Python program ispravlja najčešće pogrešne znakove u titlovima na hrvatskome jeziku. 
# Ispravak znakova u titlovima (Python program)

## O programu

Ovaj program automatski ispravlja pogrešno prikazane znakove u tekstualnim titlovima.  
Koristan je kada se znakovi poput č, ć, đ, š, ž ne prikažu pravilno (npr. ako se pojave kao "æ", "ð", "ae", itd.).

## Što program radi

- Traži od korisnika da unese ime .txt datoteke s titlovima
- Automatski pokušava učitati sadržaj datoteke s kodiranjem cp1250, a zatim s utf-8 ako prvo ne uspije
- Prepoznaje i ispravlja najčešće greške u prikazu znakova
- Sprema novi, ispravljeni fajl s nazivom ispravljeno_[originalni_naziv]

## Sadržaj projekta

ispravak.py - Python skripta koja vrši ispravke
README.md - Upute za korištenje programa

## Kako koristiti

1. Provjerite imate li instaliran Python (verzija 3.10 ili novija).  
   Python možete preuzeti ovdje: https://www.python.org/downloads/

2. Otvorite ispravak.py u bilo kojem Python editoru, npr.:
   - IDLE (dolazi uz Python)
   - Visual Studio Code
   - PyCharm
   - Terminal / CMD

3. Pokrenite program. Kada se pojavi poruka "Unesi ime .txt datoteke s titlovima (npr. titlovi.txt)" upišite naziv datoteke (npr. mojfilm.txt).

4. Program će pokušati otvoriti datoteku s kodiranjem cp1250. Ako to ne uspije, pokušat će s utf-8.

5. Nakon uspješnog učitavanja, program će napraviti ispravke i spremiti novu datoteku s nazivom: ispravljeno_mojfilm.txt

6. Otvorite ispravljenu datoteku i provjerite rezultat.

## Napomena o kodiranju

Ova verzija programa pokušava otvoriti datoteku s dva najčešća kodiranja:
- cp1250 (Windows kodna stranica za hrvatski/istočnoeuropske jezike)
- utf-8 (najrašireniji standard za kodiranje teksta)

Ako nijedno ne uspije, program će javiti korisniku detalje pokušaja.

## Zahtjevi

- Python 3.10 ili noviji
- .txt datoteka s titlovima koje želite ispraviti
- Editor koji može pokretati Python skripte


Autor: Iva Široki
