#!/bin/bash

echo "Running black..."
black --check src/ tests/

exit $?
