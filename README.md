#CTTV JSON schema

#### ![info](https://github.com/CTTV/input_data_format/raw/master/help/images/info.gif) [**Instructions for generating  target-disease-association objects using newest schema**](doc/instructions.md)

## Schema overview

![Schema 1.2 overview](imgs/schema_1.2.png)


## Validation
Execute something like:
```
git clone https://github.com/opentargets/json_schema.git /var/tmp/json_schema && /var/tmp/json_schema/scripts/json_schema_validator.pl <your file>
```
Beware there are a couple of bugs in the perl json schema validation library, so the output of this script will not be 100% accurate.

See [issues](https://github.com/jhthorsen/json-validator/issues?q=is%3Aissue+author%3AckongEbi) here.
