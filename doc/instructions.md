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

- [Click here for an Excel file](https://github.com/opentargets/json_schema/blob/master/doc/json_schema_migration_from_1.1_to_1.2.xlsx?raw=true) detailing the list of changes from schema 1.1 to 1.2

- [Click here](../examples) to see some validated examples.

- Please provide JSON instances validated against the above schema in **a single file** using 1 JSON instance per line e.g.
```bash
{ "target_disease_association_object_1" }
{ "target_disease_association_object_2" }
{ "target_disease_association_object_3" }
{ "target_disease_association_object_4" }
...
```


## Test the schemas

- Install [required schema validation tools](../test/README.md)
- git clone https://github.com/opentargets/json_schema.git

```bash
cd test
./run_all_tests.sh
```


## Python factory package

- We are developing this.
