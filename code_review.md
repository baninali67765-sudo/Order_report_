# Code Review

Jag gick igenom originalkoden innan jag började refaktorera den.

## 1. All kod finns i en fil

**Observation:** Nästan hela programmet finns i samma fil.

**Konsekvens:** Det blir svårt att läsa och ändra koden.

**Förslag:** Dela upp koden i flera moduler med olika ansvar.

## 2. print() används

**Observation:** Programmet använder `print()` för information och fel.

**Konsekvens:** Det är svårare att kontrollera och följa programmets körning.

**Förslag:** Använd Python `logging`.

## 3. Samma kod upprepas

**Observation:** Rapporten för kategori och region använder nästan samma kod.

**Konsekvens:** Det blir onödigt mycket kod och svårare att ändra.

**Förslag:** Skapa en funktion som kan användas för båda rapporterna.

## 4. Dålig felhantering

**Observation:** Programmet använder `except Exception`.

**Konsekvens:** Olika typer av fel behandlas på samma sätt och viktig information kan försvinna.

**Förslag:** Använd tydligare och mer specifik felhantering.

## 5. Otydligt felmeddelande

**Observation:** Om kolumner saknas visas bara `"Fel data"`.

**Konsekvens:** Man vet inte vad som är fel.

**Förslag:** Visa vilka kolumner som saknas.

## 6. Ingen automatisk testning

**Observation:** Originalprogrammet har inga tester.

**Konsekvens:** Det är svårt att veta om ändringar förstör beräkningarna.

**Förslag:** Använd pytest för att testa viktiga funktioner.

## Sammanfattning

Den största förbättringen är att koden nu är uppdelad i tydliga delar. Det gör programmet enklare att läsa, testa och ändra.
