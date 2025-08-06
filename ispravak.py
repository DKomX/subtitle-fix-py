# Popis zamjena
zamjene = {
    "ae": "ć",
    "Æ": "Ć",
    "æ": "ć",
    "ć": "ć",
    "č́": "č",
    "dj": "đ",
    "Dj": "Đ",
    "Ð": "Đ",
    "ð": "đ",
    "È": "Č",
    "É": "Č",
    "è": "č",
    "é": "č",
    "ś": "š",
    "š́": "š",
    "ź": "ž"
}

# 1. Unos imena ulazne datoteke
ulaz = input("Unesi ime .txt datoteke s titlovima (npr. titl.txt): ")

# 2. Pokušaj otvoriti i pročitati datoteku
try:
    with open(ulaz, "r", encoding="cp1250") as f:
        tekst = f.read()
except FileNotFoundError:
    print("Greška: datoteka nije pronađena. Provjeri ime i pokušaj ponovno.")
    exit()
except UnicodeDecodeError:
    print("Greška kod čitanja datoteke. Pokušaj otvoriti fajl s ispravnim kodiranjem.")
    exit()

# 3. Izvrši zamjene
for stari, novi in zamjene.items():
    tekst = tekst.replace(stari, novi)

# 4. Spremi rezultat u novi fajl
izlaz = f"ispravljeno_{ulaz}"
with open(izlaz, "w", encoding="utf-8") as f:
    f.write(tekst)

print(f"Ispravak je gotov! Provjeri '{izlaz}'.")
