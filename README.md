# mwnz_eval
Code for https://github.com/MiddlewareNewZealand/evaluation-instructions/tree/main. 
Aim is to build simple application that connects to a static XML API and transforms it to a JSON response.

# Getting started
Installation
```
cd mwnz
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

To run the flask app:
```
flask --app flaskr run
```

# Trouble Shooting
If this error occurs when installing the project, then a newer version of pip needs to be used.
```
ERROR: File "setup.py" not found. Directory cannot be installed in editable mode: /home/cleverlana/mwnz
(A "pyproject.toml" file was found, but editable mode currently requires a setup.py based build.)
```

You can do this by using the following command
```
python -m pip install --upgrade pip
```
