#!/bin/bash

#Test all bioentity schemas

#Check that z-schema is installed
./test_z-schema.sh &&

z-schema ../src/bioentity/target.json bioentities/target.json
z-schema ../src/bioentity/disease.json bioentities/disease.json
z-schema ../src/bioentity/drug.json bioentities/drug.json
z-schema ../src/bioentity/phenotype.json bioentities/phenotype.json
z-schema ../src/bioentity/snp.json bioentities/snp.json