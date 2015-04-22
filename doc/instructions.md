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

- There are 5 target-disease evidence string schemas tailored for different types of experimental evidence. Click to see each:
	1. [Literature](../src/literature.json)
This is quite a generic schema. You are required to add a further label to help us place the evidence in the right place in the CTTV application. These are the valid labels:
```bash
"literature_evidence_string", "genomics_literature_evidence_string", "affected_pathways_evidence_string"
```

	2. [Expression](../src/expression.json) 
```bash    
    "expression_evidence_string"
```    
	3. [Drug](../src/drug.json) 
```bash   
    "drug_evidence_string"
```
	4. [Genetics](../src/genetics.json) 
```bash    
    "genetics_evidence_string"
```    
	5. [Animal models](../src/animal_models.json) 
```bash
    "animal_models_evidence_string"
```

- [Click here](https://github.com/CTTV/json_schema/blob/master/doc/json_schema_migration_from_1.1_to_1.2.xlsx?raw=true) for the list of changes from schema 1.1 to 1.2

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