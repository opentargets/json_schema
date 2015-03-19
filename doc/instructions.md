#Instructions for generating target-disease-association objects

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

  - [Aim](#aim)
  - [Test the schemas](#test-the-schemas)
  - [View examples](#view-examples)
  - [Python factory package](#python-factory-package)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Aim

- The goal of this schema is to standardize target-disease evidence from different data projects.

- [Click here](../src/target_disease_association.json) for the primary CTTV target-disease schema

- [Click here](../test/target_disease_assoc/target_disease_association.json) for an example instance (very much made up!) that fits the primary schema

- Please provide JSON instances validated against the above schema in **a single file** using 1 JSON instance per line e.g.
```
{ "target_disease_association_object_1" }
{ "target_disease_association_object_2" }
{ "target_disease_association_object_3" }
{ "target_disease_association_object_4" }
...
```


- The main schema above references a number of other schemas e.g. [target](../src/bioentity/target.json), [disease](../src/bioentity/disease.json), [snp](../src/bioentity/snp.json), [expression evidence](../src/evidence/expression.json), [genetic_evidence_via_snp](../src/evidence/genetics/snp.json), [target-drug-disease_evidence_chain](../src/evidence_chain/drug.json) etc. So, it is much more granular than schema 1.1.

## Test the schemas

- Install [required schema validation tools](../test/README.md)
- git clone https://github.com/CTTV/json_schema.git

```bash
cd test
./run_all_tests.sh
```

## View examples

- The above test suite references [a few manually generated JSON instances](../test). 

## Python factory package

- We are developing this.