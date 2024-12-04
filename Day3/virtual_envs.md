# Virtual envs
Najpopularniejsze narzędzia do tworzenia i zarządzania wirtualnymi środowiskami w Pythonie:
- venv (wbudowane w Pythonie od wersji 3.3)
- virtualenv
- pipenv
- conda - często używane z Anaconda płatne - darmowa wersje miniconda
- poetry


### Tworzenie nowego środowiska
`conda create --name myenv python=3.8`

### Aktywacja środowiska
`conda activate myenv`

### Dezaktywacja środowiska
`conda deactivate`

### Instalacja pakietu
`conda install numpy`

Mozna tez nadal uzywac pip

`pip install numpy`

### Tworzenie środowiska z pliku
`conda env create --file environment.yml`

Jak wyglada przykładowy plik environment.yml
```
name: myenv
channels:
  - defaults
dependencies:
  - python=3.8
  - numpy
  - pandas
```

### Zapis środowiska do pliku 
`conda env export --name myenv --file environment.yml`

### Usuniecie środowiska
`conda env remove --name myenv`