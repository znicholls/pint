# Not a real makefile, just the steps
# make a conda env e.g. conda create -n pint-pandas -y python=3.6
# activate the env e.g. conda activate pint-pandas
# conda install pip jupyter numpy cython pytest pytest-cov coveralls
# pip install git+https://github.com/pandas-dev/pandas.git
# cd pint
# pip install -e .

.PHONY: test
test:
	python -bb -m coverage run -p --source=pint --omit="*test*","*compat*" setup.py test
	python -bb -m coverage run -p --source=pint --omit="*test*","*compat*" -m py.test pint/testsuite/pandas_test_interface.py
	coverage combine
	coverage report -m
