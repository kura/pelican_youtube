.PHONY: install uninstall pypi
install:
	python setup.py install

uninstall:
	pip uninstall pelican_youtube

pypi:
	pip install wheel twine
	python setup.py sdist bdist_wheel
	twine upload dist/*
