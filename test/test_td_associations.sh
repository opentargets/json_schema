#!/bin/bash

./test_z-schema.sh &&

echo -e "TESTSUITE: TARGET-DISEASE-ASSOCIATION OBJECTS\n"

z-schema ../src/target_disease_association.json ./target_disease_assoc/target_disease_association.json