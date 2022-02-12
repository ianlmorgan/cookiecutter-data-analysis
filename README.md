# My Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

Forked and modified from [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter -c v1 https://github.com/ianlmorgan/cookiecutter-data-science


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
    ├── LICENSE             <- Open-source license
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for individuals using this project
    ├── data
    │   ├── intermediate    <- Intermediate data that has been transformed
    │   ├── processed       <- The final, canonical data sets for modeling
    │   └── raw             <- The original, immutable data dump
    │
    ├── docs                <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models              <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                          the creator's initials, and a short `-` delimited description, e.g.
    │                          `1.0-ilm-initial-data-exploration`.
    │
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting
    |
    ├── results             <- Generated results from data analysis and fitting models
    │
    ├── src                 <- Source code for use in this project
    │   ├── __init__.py     <- Makes src a Python module
    │   │
    │   ├── data            <- Scripts to load and process data
    │   │   └── load_data.py
    |   |   └── create_int_data
    │   │   └── create_pro_data.py
    │   │
    │   ├── models          <- Scripts for models and fitting processed data
    │   │   └── model.py
    │   │
    │   └── visualization   <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                          generated with `pip freeze > requirements.txt`
    │
    ├── setup.py            <- makes project pip installable (pip install -e .) so src can be imported
    |
    └── test_environment.py <- checks that correct python interpreter is installed
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
