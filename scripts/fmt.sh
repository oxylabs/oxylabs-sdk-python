#!/bin/bash

# Run isort on the src directory
isort src

# Run black on the src directory
black --line-length 79 src
