# Orderrapport

## Vad gör programmet?

Programmet läser orderdata från en CSV-fil och skapar rapporter om försäljning och returer.

Rapporterna sparas som CSV-filer i mappen `output`.

## Installation

Installera Pandas  och pytest:



## Köra programmet

Kör från projektets huvudmapp:

```bash
python -m src.order_report.main
```

Programmet läser:

```text
data/orders.csv
```

och skapar:

```text
output/overview.csv
output/sales_by_category.csv
output/sales_by_region.csv
output/returns_by_category.csv
```

## Tester

Testerna körs med pytest:

```bash
pytest
```

Tester finns i mappen `tests`.

## Projektstruktur

* `main.py` – startar programmet
* `config.py` – innehåller inställningar
* `loader.py` – läser in CSV-filen
* `validation.py` – kontrollerar datan
* `processing.py` – bearbetar och räknar ut värden
* `reports.py` – skapar och sparar rapporter
* `tests/` – automatiska tester

## Reflektion

Originalkoden hade nästan all kod i en fil. Det gjorde koden svårare att läsa och testa.

Jag delade därför upp koden i flera moduler med olika ansvar. Jag ersatte också `print()` med logging och lade till bättre felhantering.

Jag använde en dataclass för programmets konfiguration eftersom det ger ett enkelt sätt att samla sökvägar och inställningar.

Testerna kontrollerar viktiga beräkningar och även fel, till exempel om en obligatorisk kolumn saknas.

Det svåraste var att dela upp originalkoden utan att ändra resultatet. Jag kontrollerade därför att de nya rapporterna gav samma resultat som originalprogrammet.

Om jag hade haft mer tid hade jag lagt till fler tester och mer avancerad validering av datan.
