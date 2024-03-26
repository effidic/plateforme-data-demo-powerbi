# plateforme-data-demo-powerbi


## Liste des sources

voir docs/sources.md

## Install

git clone 

If you don't have venv : 
> pip install virtualenv

Create venv : 
> python -m venv venv

Activate (on Windows Powershell) : 
> .\venv\Scripts\Activate.ps1

Install Poetry : 
> pip install poetry

Install project with Poetry : 
> poetry install --no-root

Activate pre-commit : 
> poetry run pre-commit install

To run pre-commit manually : 
> poetry run pre-commit run --all-files