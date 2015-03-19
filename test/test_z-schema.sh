#!/bin/bash

#Check that z-schema is installed

echo -e "TESTSUITE: Z-SCHEMA INSTALLATION\n"

which z-schema > /dev/null
if [[ $? != 0 ]]; then
		echo "z-schema is not installed; please install this before trying again"
		exit 1
else
   echo "z-schema installed [SUCCESS]"
   exit 0
fi