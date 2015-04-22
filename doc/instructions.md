#Instructions for generating target-disease evidence strings

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** 

  - [Aim](#aim)
  - [Test the schemas](#test-the-schemas)
  - [Python factory package](#python-factory-package)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Aim

- The goal of this schema is to standardize target-disease evidence from different data projects.

- [Click here](https://github.com/CTTV/json_schema/blob/master/doc/json_schema_migration_from_1.1_to_1.2.xlsx?raw=true) for the list of changes from schema 1.1 to 1.2

- There are 5 target-disease evidence string schemas tailored for different types of experimental evidence. Click to see each:

| Link to schema | .type field in schema |
|--------|--------|
|     [Literature](../src/literature.json)   |   "literature_evidence_string", "genomics_literature_evidence_string", "affected_pathways_evidence_string"     |
| [Expression](../src/expression.json) | "expression_evidence_string" |
| [Drug](../src/drug.json) | "drug_evidence_string" |
| [Genetics](../src/genetics.json)  | "genetics_evidence_string" |
| [Animal models](../src/animal_models.json) | "animal_models_evidence_string" |

Note: ["Literature"](../src/literature.json) is quite a generic schema.




- [Click here](../examples) to see some validated examples.

- Please provide JSON instances validated against the above schema in **a single file** using 1 JSON instance per line e.g.
```bash
{ "target_disease_association_object_1" }
{ "target_disease_association_object_2" }
{ "target_disease_association_object_3" }
{ "target_disease_association_object_4" }
...
```


- The above schemas reference a number of remote schemas e.g. [target](../src/bioentity/target.json), [disease](../src/bioentity/disease.json), [variant](../src/bioentity/variant.json), [expression evidence](../src/evidence/expression.json) etc. So, it is much more granular than schema 1.1.

## Test the schemas

- Install [required schema validation tools](../test/README.md)
- git clone https://github.com/CTTV/json_schema.git

```bash
cd test
./run_all_tests.sh
```


## Python factory package

- We are developing this.