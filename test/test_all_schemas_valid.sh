#!/bin/bash

#Test all schemas in src folder are valid JSON schemas

#Check that z-schema is installed
./test_z-schema.sh &&

echo -e "TESTSUITE: ALL SCHEMAS\n"

for i in `find ../src/ -name "*.json"`;
	do echo "TEST: $i";z-schema $i;
done
