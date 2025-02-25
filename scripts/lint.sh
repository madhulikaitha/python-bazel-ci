#!/bin/bash

echo "Running pylint..."
pylint src/*.py tests/*.py

exit $?
