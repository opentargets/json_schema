#!/bin/bash

#Test all schemas in src folder are valid JSON schemas

#Check that z-schema is installed
which z-schema > /dev/null
if [[ $? != 0 ]]; then
		echo "z-schema is not installed; please install this before trying again"
		exit 1
fi

for i in `find ../src/ -name "*.json"`;
	do z-schema ${i};
done
