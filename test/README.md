# Test suite - validation of individual schemas and instances

#### Requirements: node.js and z-schema validator

##Installation Notes

1] Install [node.js](https://nodejs.org/)

- If you are behind a firewall proxy, you need to follow [these instructions](http://jjasonclark.com/how-to-setup-node-behind-web-proxy/) because the validator needs to query remote schemas.

2] Install [z-schema validator](https://github.com/zaggino/z-schema) using the node.js shell:
```bash
npm install --global z-schema
z-schema --help
z-schema mySchema.json
z-schema mySchema.json myJson.json
z-schema --strictMode mySchema.json myJson.json
```
3] Try validation:

```bash
#Validate the schema itself:
z-schema schema.json

#Validate an instance against the schema:
z-schema schema.json instance.json
```

4] If you are using windows+cygwin and have installed the windows version of node.js (and prefer to use z-schema from a UNIX prompt):

```bash
#Add the following line to your .bashrc; this will setup the nodejs. ENV variables:
alias nodejs_setup="/cygdrive/c/Program\ Files/nodejs/nodevars.bat;echo z-schema myschema.json instance.json"
nodejs_setup
```
