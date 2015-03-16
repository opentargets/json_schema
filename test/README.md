# Test - using remote schemas

1. Install node.js
2. Install [z-schema validator](https://github.com/zaggino/z-schema) as follows using node.js command prompt:
```
npm install --global z-schema
z-schema --help
z-schema mySchema.json
z-schema mySchema.json myJson.json
z-schema --strictMode mySchema.json myJson.json
```
3. Try validation:

```
z-schema schema.json instance.json
```