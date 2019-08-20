# pySqlEntityCreatorCLI
CLI designed to create entities, copy old entities and change values or create simple entities pre-prepared.

## Installation
This simple script uses [PyInquirer](https://github.com/CITGuru/PyInquirer), check their repository page for more information. The

```
pip install pyInquirer
```

Before starting create the folder 'files' in the same level of main.py, and be sure you check 'src/config.py' and change the url that leads to the folder where you are storing all your .sql.

## Features

Right now the script allows you to do three different tasks:
* Create a new entity from scratch.
* Copy an old entity and replace values from it to create a new one.
* Use pre-prepared entities that work as a template with a few options.