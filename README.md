![Python application](https://github.com/jacknely/MealAPI/workflows/Python%20application/badge.svg)
![Python package](https://github.com/jacknely/MealAPI/workflows/Python%20package/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Meal API

Performs a set of recipe operations on an imported recipe file and allows user
to get recipes by ID, get recipes by cuisine, and update an existing recipes

## Requirements

- Python 3.7
- Flask
- Pytest
- Pandas

Install from requirements.txt


## Usage

Running the web app.

```
set FLASK_APP=run.py
flask run
```
Navigate to local host with recipe ID in order to see details of that recipe
```
http://127.0.0.1:5000/<id>
```


Navigate to recipe-by-cuisine with a specified cuisine.
Specify page number if desired
```
http://127.0.0.1:5000/cuisine/british?page=1&items=1
```


Update existing recipes using a PUT request with the data to be updated for the corresponding ID.
```
eg
data = {"title": "changed"}
http://127.0.0.1:5000/<id>
```

