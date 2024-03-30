#!/bin/bash

rm -rf dist/ build/ oxylabs.egg-info/
python setup.py sdist bdist_wheel
twine upload dist/*
