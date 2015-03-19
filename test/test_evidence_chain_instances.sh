#!/bin/bash

./test_z-schema.sh &&

echo -e "TESTSUITE: EVIDENCE_CHAIN\n"

z-schema ../src/evidence_chain/generic.json ./evidence_chain/generic.json