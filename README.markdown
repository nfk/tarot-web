# The project depends of
- python 2.7
- coverage 3.5
- django 1.5.1

# Environnement
export PYTHONPATH=$(pwd)

# Run all unit test
python -m unittest discover -v 

# Run coverage
for f in `find -name test_*.py`; do python-coverage run -a $f; done
python-coverage report -m
