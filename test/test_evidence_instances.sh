#!/bin/bash

#Test all evidence schemas against instances (in the folder ./evidence against their reference schema)

#Check that z-schema is installed
./test_z-schema.sh &&

echo -e "TESTSUITE: EVIDENCE OBJECTS\n"

for i in `find ./evidence/ -name "*.json"`;
	do BNAME=`basename $i`;echo "TEST: $BNAME";z-schema ../src/evidence/$BNAME $i;
done
