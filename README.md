#CTTV JSON schema

#### ![info](https://github.com/CTTV/input_data_format/raw/master/help/images/info.gif) [**Instructions for generating  target-disease-association objects using newest schema**](doc/instructions.md)

## Schema overview

![Schema 1.2 overview](imgs/schema_1.2.png)


## Validation
Execute something like:
```
cpanm JSON::Validator
git clone https://github.com/opentargets/json_schema.git json_schema
cat <your document> | json_schema/scripts/json_schema_validator.pl --schema <your schema>
```
The script is a thin wrapper around https://github.com/jhthorsen/json-validator. There was a bug affecting our schema between 0.96 and 1.04, do make sure you use at least version 1.05.
