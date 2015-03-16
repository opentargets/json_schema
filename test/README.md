# Tests - validation of individual schemas with examples

#### Requirements: node.js and z-schema validator

1. Install [node.js](https://nodejs.org/)
2. Install [z-schema validator](https://github.com/zaggino/z-schema) using the node.js shell:
```bash
npm install --global z-schema
z-schema --help
z-schema mySchema.json
z-schema mySchema.json myJson.json
z-schema --strictMode mySchema.json myJson.json
```
3. Try validation:

```bash
#Validate the schema itself:
z-schema schema.json

#Validate an instance against the schema:
z-schema schema.json instance.json
```