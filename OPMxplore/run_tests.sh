#!/bin/bash

# run this script via: bash run.sh

# run the unit tests
# You need to include --cover-package so that it does not also run all of the
# unit tests on the dependencies also (which can take 10+minutes)
#nosetests --with-coverage --cover-html --cover-package OPMxplore.py --cover-package OPMvis.py 
#nosetests --cover-package OPMxplore.py --cover-package OPMvis.py 
nosetests -vv
# run the PEP8 checker
pycodestyle OPMxplore.py OPMvis.py tests/test_OPMvis.py tests/test_OPMxplore.py