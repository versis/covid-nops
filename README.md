# Status
Plik: **nops.csv**

Ostatnia aktualizacja: **2021-05-04**

# Opis

[Na stronie gov.pl](https://www.gov.pl/web/szczepimysie/niepozadane-odczyny-poszczepienne) dostępne są informacje dot. NOP, w tym raport w pliku .pdf z **niepożądanymi odczynami poszczepiennymi (NOP)**. Znajduje się na samym dole strony.

Format `.pdf` nie jest łatwy w późniejszej analizie, dlatego powstał skrypt `pdf_to_csv_converter.py`, który parsuje dane do formatu `.csv`. 


# Instalacja

Jeśli nie korzystałeś wcześniej z Pythona to proponuję instalację [Minicondy](https://docs.conda.io/en/latest/miniconda.html) z Pythonem w wersji 3.8.


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

# Inne informacje
Czas przetworzenia całego pdfa to około **15 minut**

W razie potrzeby, sugeruję wskazywać tylko strony, które nas interesują. Np.
```python
df_nops = convert_pdf_to_csv(path_in=path_in, pages="740-end", remove_new_lines=True) 
```
dla stron od 740 do ostatniej.

---
Pozdro :)