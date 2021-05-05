# Opis

[Na stronie gov.pl](https://www.gov.pl/web/szczepimysie/niepozadane-odczyny-poszczepienne) dostępne są informacje dot. NOP, w tym raport w pliku .pdf z **niepożądanymi odczynami poszczepiennymi (NOP)**. Znajduje się na samym dole strony.

Format `.pdf` nie jest łatwy w późniejszej analizie, dlatego powstał skrypt `pdf_to_csv_converter.py`, który parsuje dane do formatu `.csv`. 

# Instalacja

[Zainstaluj](https://camelot-py.readthedocs.io/en/master/user/install-deps.html#install-deps) zaleźności potrzebne do użycia Pythonowej biblioteki `Camelot`.

Zainstaluj biblioteki Pythonowe:
```bash
pip install -r requirements.txt
```

# Użycie

```bash
python pdf_to_csv_converter.py
```

### Potencjalne parametry do ustawienia w skrypcie (standardowe zachowanie)
* nazwa pliku wejściowego (`nops.pdf`)
* parsowanie konkretynych stron (wszystkie)
* usuwanie znaków nowej linii (włączone)

Skrypt nie posiada parametrow, które można ustawić puszczajac go z linii poleceń.


# ---
Pozdro :