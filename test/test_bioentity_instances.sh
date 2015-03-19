#!/bin/bash

#Test all bioentity schemas (in the folder ./bioentities against their reference schema)

#Check that z-schema is installed
./test_z-schema.sh &&

echo -e "TESTSUITE: BIOENTITIES\n"

for i in `find ./bioentities/ -name "*.json"`;
	do BNAME=`basename $i`;echo "TEST: $BNAME";z-schema ../src/bioentity/$BNAME $i;
done

# z-schema ../src/bioentity/target.json bioentities/target.json
# z-schema ../src/bioentity/disease.json bioentities/disease.json
# z-schema ../src/bioentity/drug.json bioentities/drug.json
# z-schema ../src/bioentity/phenotype.json bioentities/phenotype.json
# z-schema ../src/bioentity/snp.json bioentities/snp.json