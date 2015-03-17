#!/bin/bash

#Test all schemas in src folder are valid JSON schemas

#Check that z-schema is installed
./test_z-schema.sh &&

for i in `find ../src/ -name "*.json"`;
	do BNAME=`basename $i`;echo "TEST: $BNAME";z-schema $i;
done
