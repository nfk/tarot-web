# Tarot Web
## Requirements
- python 2.7
- coverage 3.5
- django 1.5.1

## Run all unit test and get coverage
```bash
export PYTHONPATH=$(pwd)
python -m unittest discover -v 
for f in $(find -name test_*.py); do python-coverage run -a $f; done
python-coverage report -m
```

## Run website
```bash
python gui/manage.py runserver
```
