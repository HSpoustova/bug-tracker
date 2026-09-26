# 🐞 Bug tracker

Webová aplikace na hlášení a sledování bugů, kterou stavím krok za krokem v kurzu **Bug Hunter Akademie**.

**Technologie:** Python, Flask, SQLite, HTML, CSS a JavaScript. Testy píšu v pytestu a Seleniu.

## Spuštění v GitHub Codespaces (počítač, tablet, mobil)

1. Na GitHubu otevři repozitář a klikni na **Code → Codespaces → Create codespace on main**.
2. Počkej, až se prostředí nainstaluje. Poprvé to trvá pár minut.
3. V terminálu (dole) spusť aplikaci:
   ```bash
   python app.py
   ```
4. Codespaces nabídne **Open in Browser** na portu 5000. Tam aplikace běží.

## Testy

```bash
pytest -v                 # všechno
pytest -v -m "not gui"    # bez prohlížeče (rychlé)
pytest -v -m gui          # Selenium testy v prohlížeči
pytest -k validace        # jen testy se slovem validace
```

## Struktura

| Soubor | Co v něm je |
| --- | --- |
| `konstanty.py` | povolené severity, priority a stavy |
| `validace.py` | kontrola, jestli je bug správně vyplněný |
| `stavy.py` | workflow: ze kterého stavu kam se smí |
| `schema.sql`, `databaze.py` | tabulka a práce s databází SQLite |
| `app.py` | Flask: API (`/api/bugy`) a stránky |
| `templates/`, `static/` | HTML šablony, CSS a JavaScript |
| `tests/` | pytest: validace, databáze, API, stavy, bezpečnost, GUI |
