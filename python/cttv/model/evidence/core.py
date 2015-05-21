'''
Copyright 2014-2015 EMBL - European Bioinformatics Institute, Wellcome 
Trust Sanger Institute and GlaxoSmithKline

This software was developed as part of the Centre for Therapeutic 
Target Validation (CTTV)  project. For more information please see:

	http://targetvalidation.org

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import re
import sys
import iso8601
import types
import json
import logging
import cttv.model.evidence.association_score as evidence_association_score

__author__ = "Gautier Koscielny"
__copyright__ = "Copyright 2014-2015, The Centre for Therapeutic Target Validation (CTTV)"
__credits__ = ["Gautier Koscielny", "Samiul Hasan"]
__license__ = "Apache 2.0"
__version__ = "1.2"
__maintainer__ = "Gautier Koscielny"
__email__ = "gautierk@targetvalidation.org"
__status__ = "Production"

logger = logging.getLogger(__name__)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json
"""
class Base(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    
    """
    Name: unique_experiment_reference
    Type: string
    Description: A unique experiment identifer or literature reference that uniquely identifies the study in your database
    """
    self.unique_experiment_reference = unique_experiment_reference
    """
    Name: provenance_type
    """
    self.provenance_type = provenance_type
    
    """
    Name: is_associated
    Type: boolean
    """
    self.is_associated = is_associated
    
    """
    Name: date_asserted
    Type: string
    String format: date-time
    """
    self.date_asserted = date_asserted
    """
    Name: association_score
    """
    self.association_score = association_score
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.unique_experiment_reference:
        obj.unique_experiment_reference = clone.unique_experiment_reference
    if clone.provenance_type:
        obj.provenance_type = BaseProvenance_Type.cloneObject(clone.provenance_type)
    if clone.is_associated:
        obj.is_associated = clone.is_associated
    if clone.date_asserted:
        obj.date_asserted = clone.date_asserted
    if clone.association_score:
        obj.association_score = clone.association_score
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['unique_experiment_reference','provenance_type','is_associated','date_asserted','association_score']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'unique_experiment_reference' in map:
        obj.unique_experiment_reference = map['unique_experiment_reference']
    if  'provenance_type' in map:
        obj.provenance_type = BaseProvenance_Type.fromMap(map['provenance_type'])
    if  'is_associated' in map:
        obj.is_associated = map['is_associated']
    if  'date_asserted' in map:
        obj.date_asserted = map['date_asserted']
    if  'association_score' in map:
        obj.association_score = map['association_score']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Base
    :returns: number of errors found during validation
    """
    error = 0
    """ Check regex: http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}|STUDYID_.+$ for validation"""
    if self.unique_experiment_reference and not re.match('http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}|STUDYID_.+$', self.unique_experiment_reference):
        logger.error("Base - unique_experiment_reference '"+self.unique_experiment_reference+"' does not match pattern 'http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}|STUDYID_.+$'")
        logger.warn(json.dumps(self.unique_experiment_reference, sort_keys=True, indent=2))
    if self.unique_experiment_reference and not isinstance(self.unique_experiment_reference, basestring):
        logger.error("Base - 'unique_experiment_reference' type should be a string")
        error = error + 1
    if self.provenance_type:
        if not isinstance(self.provenance_type, BaseProvenance_Type):
            logger.error("BaseProvenance_Type class instance expected for attribute - 'provenance_type'")
            error = error + 1
        else:
            provenance_type_error = self.provenance_type.validate(logger)
            error = error + provenance_type_error
    if self.is_associated and not type(self.is_associated) is bool:
        logger.error("Base - 'is_associated' type should be a boolean")
        error = error + 1
    if self.date_asserted and not self.date_asserted == None:
        try:
            iso8601.parse_date(self.date_asserted)
        except iso8601.iso8601.ParseError, e:
            logger.error("Base - date_asserted '{0}' invalid ISO 8601 date (YYYY-MM-DDThh:mm:ss.sTZD expected)".format(self.date_asserted))
            logger.error(self.to_JSON())
            error = error+1
    if self.date_asserted and not isinstance(self.date_asserted, basestring):
        logger.error("Base - 'date_asserted' type should be a string")
        error = error + 1
        if not ( isinstance(self.association_score, evidence_association_score.Pvalue) or isinstance(self.association_score, evidence_association_score.Probability) or isinstance(self.association_score, evidence_association_score.Rank) or isinstance(self.association_score, evidence_association_score.Summed_Total)):
            logger.error("Base - 'association_score' incorrect type")
            error = error + 1
        else:
            association_score_error = self.association_score.validate(logger)
            error = error + association_score_error
    return error
  def date_assertedto_isoformat(self):
    iso8601.parse_date(self.date_asserted).isoformat()
  
  def serialize(self):
    classDict = {}
    if not self.unique_experiment_reference is None: classDict['unique_experiment_reference'] = self.unique_experiment_reference
    if not self.provenance_type is None: classDict['provenance_type'] = self.provenance_type.serialize()
    if not self.is_associated is None: classDict['is_associated'] = self.is_associated
    if not self.date_asserted is None: classDict['date_asserted'] = self.date_asserted
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json#base_evidence/definitions/single_lit_reference
"""
class Single_Lit_Reference(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param lit_id = None
  :param     score = None
  :param mined_sentences = None
  """
  def __init__(self, lit_id = None,     score = None, mined_sentences = None):
    
    """
    Name: lit_id
    Type: string
    Description: Note for pubmed identifiers, use the URI http://europepmc.org/abstract/MED/[0-9]+
    Required: {True}
    """
    self.lit_id = lit_id
    """
    Name: score
    """
    self.score = score
    
    """
    Name: mined_sentences
    Type: array
    """
    if mined_sentences is None:
        self.mined_sentences = []
    else:
        self.mined_sentences = mined_sentences
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.lit_id:
        obj.lit_id = clone.lit_id
    if clone.score:
        obj.score = evidence_association_score.Rank.cloneObject(clone.score)
    if clone.mined_sentences:
        obj.mined_sentences = []; obj.mined_sentences.extend(clone.mined_sentences)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['lit_id','score','mined_sentences']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("single_lit_reference - DictType expected - {0} found\n".format(type(map)))
      return
    if  'lit_id' in map:
        obj.lit_id = map['lit_id']
    if  'score' in map:
        obj.score = evidence_association_score.Rank.fromMap(map['score'])
    if  'mined_sentences' in map:
        obj.mined_sentences = map['mined_sentences']
    for key in map:
      if not key in cls_keys:
        logger.error("single_lit_reference - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Single_Lit_Reference
    :returns: number of errors found during validation
    """
    error = 0
    """ Check regex: http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$ for validation"""
    if self.lit_id and not re.match('http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$', self.lit_id):
        logger.error("Single_Lit_Reference - lit_id '"+self.lit_id+"' does not match pattern 'http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$'")
        logger.warn(json.dumps(self.lit_id, sort_keys=True, indent=2))
    if self.lit_id and not isinstance(self.lit_id, basestring):
        logger.error("Single_Lit_Reference - 'lit_id' type should be a string")
        error = error + 1
    if self.score:
        if not isinstance(self.score, evidence_association_score.Rank):
            logger.error("evidence_association_score.Rank class instance expected for attribute - 'score'")
            error = error + 1
        else:
            score_error = self.score.validate(logger)
            error = error + score_error
    if not self.mined_sentences == None and len(self.mined_sentences) > 0 and not all(isinstance(n, basestring) for n in self.mined_sentences):
        logger.error("Single_Lit_Reference - 'mined_sentences' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.lit_id is None: classDict['lit_id'] = self.lit_id
    if not self.score is None: classDict['score'] = self.score.serialize()
    if not self.mined_sentences is None: classDict['mined_sentences'] = self.mined_sentences
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(provenance_type)
"""
class BaseProvenance_Type(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param     literature = None
  :param     expert = None
  :param     database = None
  """
  def __init__(self,     literature = None,     expert = None,     database = None):
    """
    Name: literature
    """
    self.literature = literature
    """
    Name: expert
    """
    self.expert = expert
    """
    Name: database
    """
    self.database = database
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.literature:
        obj.literature = BaseLiterature.cloneObject(clone.literature)
    if clone.expert:
        obj.expert = BaseExpert.cloneObject(clone.expert)
    if clone.database:
        obj.database = BaseDatabase.cloneObject(clone.database)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['literature','expert','database']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Base - DictType expected - {0} found\n".format(type(map)))
      return
    if  'literature' in map:
        obj.literature = BaseLiterature.fromMap(map['literature'])
    if  'expert' in map:
        obj.expert = BaseExpert.fromMap(map['expert'])
    if  'database' in map:
        obj.database = BaseDatabase.fromMap(map['database'])
    for key in map:
      if not key in cls_keys:
        logger.error("Base - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseProvenance_Type
    :returns: number of errors found during validation
    """
    error = 0
    if self.literature:
        if not isinstance(self.literature, BaseLiterature):
            logger.error("BaseLiterature class instance expected for attribute - 'literature'")
            error = error + 1
        else:
            literature_error = self.literature.validate(logger)
            error = error + literature_error
    if self.expert:
        if not isinstance(self.expert, BaseExpert):
            logger.error("BaseExpert class instance expected for attribute - 'expert'")
            error = error + 1
        else:
            expert_error = self.expert.validate(logger)
            error = error + expert_error
    if self.database:
        if not isinstance(self.database, BaseDatabase):
            logger.error("BaseDatabase class instance expected for attribute - 'database'")
            error = error + 1
        else:
            database_error = self.database.validate(logger)
            error = error + database_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.literature is None: classDict['literature'] = self.literature.serialize()
    if not self.expert is None: classDict['expert'] = self.expert.serialize()
    if not self.database is None: classDict['database'] = self.database.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(literature)
"""
class BaseLiterature(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param references = None
  """
  def __init__(self, references = None):
    
    """
    Name: references
    Type: array
    Required: {True}
    """
    if references is None:
        self.references = []
    else:
        self.references = references
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.references:
        obj.references = []; obj.references.extend(clone.references)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['references']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("BaseProvenance_Type - DictType expected - {0} found\n".format(type(map)))
      return
    if  'references' in map:
        obj.references = map['references']
    for key in map:
      if not key in cls_keys:
        logger.error("BaseProvenance_Type - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseLiterature
    :returns: number of errors found during validation
    """
    error = 0
    if not self.references or self.references == None :
        logger.error("BaseLiterature - 'references' is required")
        error = error + 1
    if not self.references == None and len(self.references) > 0 and not all(isinstance(n, Single_Lit_Reference) for n in self.references):
        logger.error("BaseLiterature - 'references' array should have elements of type 'Single_Lit_Reference'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.references is None: classDict['references'] = self.references
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(expert)
"""
class BaseExpert(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param status = False
  :param statement = None
  :param     author = None
  """
  def __init__(self, status = False, statement = None,     author = None):
    
    """
    Name: status
    Type: boolean
    Required: {True}
    """
    self.status = status
    
    """
    Name: statement
    Type: string
    """
    self.statement = statement
    """
    Name: author
    """
    self.author = author
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.status:
        obj.status = clone.status
    if clone.statement:
        obj.statement = clone.statement
    if clone.author:
        obj.author = BaseAuthor.cloneObject(clone.author)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['status','statement','author']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("BaseProvenance_Type - DictType expected - {0} found\n".format(type(map)))
      return
    if  'status' in map:
        obj.status = map['status']
    if  'statement' in map:
        obj.statement = map['statement']
    if  'author' in map:
        obj.author = BaseAuthor.fromMap(map['author'])
    for key in map:
      if not key in cls_keys:
        logger.error("BaseProvenance_Type - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseExpert
    :returns: number of errors found during validation
    """
    error = 0
    if not self.status or self.status == None :
        logger.error("BaseExpert - 'status' is required")
        error = error + 1
    if self.status and not type(self.status) is bool:
        logger.error("BaseExpert - 'status' type should be a boolean")
        error = error + 1
    if self.statement and not isinstance(self.statement, basestring):
        logger.error("BaseExpert - 'statement' type should be a string")
        error = error + 1
    if self.author:
        if not isinstance(self.author, BaseAuthor):
            logger.error("BaseAuthor class instance expected for attribute - 'author'")
            error = error + 1
        else:
            author_error = self.author.validate(logger)
            error = error + author_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.status is None: classDict['status'] = self.status
    if not self.statement is None: classDict['statement'] = self.statement
    if not self.author is None: classDict['author'] = self.author.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(author)
"""
class BaseAuthor(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param organization = None
  :param email = None
  :param name = None
  """
  def __init__(self, organization = None, email = None, name = None):
    
    """
    Name: organization
    Type: string
    """
    self.organization = organization
    
    """
    Name: email
    Type: string
    String format: email
    """
    self.email = email
    
    """
    Name: name
    Type: string
    """
    self.name = name
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.organization:
        obj.organization = clone.organization
    if clone.email:
        obj.email = clone.email
    if clone.name:
        obj.name = clone.name
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['organization','email','name']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("BaseExpert - DictType expected - {0} found\n".format(type(map)))
      return
    if  'organization' in map:
        obj.organization = map['organization']
    if  'email' in map:
        obj.email = map['email']
    if  'name' in map:
        obj.name = map['name']
    for key in map:
      if not key in cls_keys:
        logger.error("BaseExpert - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseAuthor
    :returns: number of errors found during validation
    """
    error = 0
    if self.organization and not isinstance(self.organization, basestring):
        logger.error("BaseAuthor - 'organization' type should be a string")
        error = error + 1
    if self.email and not self.email == None and not re.match('[\w.-]+@[\w.-]+.\w+', self.email):
        logger.error("BaseAuthor - email '{0}' is not a valid email address".format(self.email))
        logger.error(self.to_JSON)
        error = error + 1
    if self.email and not isinstance(self.email, basestring):
        logger.error("BaseAuthor - 'email' type should be a string")
        error = error + 1
    if self.name and not isinstance(self.name, basestring):
        logger.error("BaseAuthor - 'name' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.organization is None: classDict['organization'] = self.organization
    if not self.email is None: classDict['email'] = self.email
    if not self.name is None: classDict['name'] = self.name
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(database)
"""
class BaseDatabase(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param     dbxref = None
  :param id = None
  :param version = None
  """
  def __init__(self,     dbxref = None, id = None, version = None):
    """
    Name: dbxref
    """
    self.dbxref = dbxref
    
    """
    Name: id
    Type: string
    Required: {True}
    """
    self.id = id
    
    """
    Name: version
    Type: string
    Required: {True}
    """
    self.version = version
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.dbxref:
        obj.dbxref = BaseDbxref.cloneObject(clone.dbxref)
    if clone.id:
        obj.id = clone.id
    if clone.version:
        obj.version = clone.version
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['dbxref','id','version']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("BaseProvenance_Type - DictType expected - {0} found\n".format(type(map)))
      return
    if  'dbxref' in map:
        obj.dbxref = BaseDbxref.fromMap(map['dbxref'])
    if  'id' in map:
        obj.id = map['id']
    if  'version' in map:
        obj.version = map['version']
    for key in map:
      if not key in cls_keys:
        logger.error("BaseProvenance_Type - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseDatabase
    :returns: number of errors found during validation
    """
    error = 0
    if self.dbxref:
        if not isinstance(self.dbxref, BaseDbxref):
            logger.error("BaseDbxref class instance expected for attribute - 'dbxref'")
            error = error + 1
        else:
            dbxref_error = self.dbxref.validate(logger)
            error = error + dbxref_error
    if not self.id or self.id == None :
        logger.error("BaseDatabase - 'id' is required")
        error = error + 1
    if self.id and not isinstance(self.id, basestring):
        logger.error("BaseDatabase - 'id' type should be a string")
        error = error + 1
    if not self.version or self.version == None :
        logger.error("BaseDatabase - 'version' is required")
        error = error + 1
    if self.version and not isinstance(self.version, basestring):
        logger.error("BaseDatabase - 'version' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.dbxref is None: classDict['dbxref'] = self.dbxref.serialize()
    if not self.id is None: classDict['id'] = self.id
    if not self.version is None: classDict['version'] = self.version
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/base.json inner class:(dbxref)
"""
class BaseDbxref(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param url = None
  :param version = None
  :param id = None
  """
  def __init__(self, url = None, version = None, id = None):
    
    """
    Name: url
    Type: string
    Description: Please provide a pointer to the original resource: e.g. http://identifiers.org/orphanet/93298
    String format: uri
    """
    self.url = url
    
    """
    Name: version
    Type: string
    Required: {True}
    """
    self.version = version
    
    """
    Name: id
    Type: string
    Description: Please provide the original DB name
    Required: {True}
    """
    self.id = id
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.url:
        obj.url = clone.url
    if clone.version:
        obj.version = clone.version
    if clone.id:
        obj.id = clone.id
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['url','version','id']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("BaseDatabase - DictType expected - {0} found\n".format(type(map)))
      return
    if  'url' in map:
        obj.url = map['url']
    if  'version' in map:
        obj.version = map['version']
    if  'id' in map:
        obj.id = map['id']
    for key in map:
      if not key in cls_keys:
        logger.error("BaseDatabase - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class BaseDbxref
    :returns: number of errors found during validation
    """
    error = 0
    if self.url and not isinstance(self.url, basestring):
        logger.error("BaseDbxref - 'url' type should be a string")
        error = error + 1
    if not self.version or self.version == None :
        logger.error("BaseDbxref - 'version' is required")
        error = error + 1
    if self.version and not isinstance(self.version, basestring):
        logger.error("BaseDbxref - 'version' type should be a string")
        error = error + 1
    if not self.id or self.id == None :
        logger.error("BaseDbxref - 'id' is required")
        error = error + 1
    if self.id and not isinstance(self.id, basestring):
        logger.error("BaseDbxref - 'id' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.url is None: classDict['url'] = self.url
    if not self.version is None: classDict['version'] = self.version
    if not self.id is None: classDict['id'] = self.id
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/expression.json
"""
class Expression(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param log2_fold_change = None
  :param comparison_name = None
  :param experiment_overview = None
  :param test_sample = None
  :param urls = None
  :param reference_sample = None
  :param evidence_codes = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, log2_fold_change = None, comparison_name = None, experiment_overview = None, test_sample = None, urls = None, reference_sample = None, evidence_codes = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Expression, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    """
    Name: log2_fold_change
    """
    self.log2_fold_change = log2_fold_change
    
    """
    Name: comparison_name
    Type: string
    Required: {True}
    """
    self.comparison_name = comparison_name
    
    """
    Name: experiment_overview
    Type: string
    Required: {True}
    """
    self.experiment_overview = experiment_overview
    
    """
    Name: test_sample
    Type: string
    Description: Free text - test sample
    Required: {True}
    """
    self.test_sample = test_sample
    
    """
    Name: urls
    Type: array
    """
    if urls is None:
        self.urls = []
    else:
        self.urls = urls
    
    """
    Name: reference_sample
    Type: string
    Description: Free text - reference sample
    Required: {True}
    """
    self.reference_sample = reference_sample
    
    """
    Name: evidence_codes
    Type: array
    Description: An array of evidence codes
    Required: {True}
    """
    if evidence_codes is None:
        self.evidence_codes = []
    else:
        self.evidence_codes = evidence_codes
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Expression, cls).cloneObject(clone)
    obj.log2_fold_change = ExpressionLog2_Fold_Change.cloneObject(clone.log2_fold_change)
    if clone.comparison_name:
        obj.comparison_name = clone.comparison_name
    if clone.experiment_overview:
        obj.experiment_overview = clone.experiment_overview
    if clone.test_sample:
        obj.test_sample = clone.test_sample
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    if clone.reference_sample:
        obj.reference_sample = clone.reference_sample
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['log2_fold_change','comparison_name','experiment_overview','test_sample','urls','reference_sample','evidence_codes']
    obj = super(Expression, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'log2_fold_change' in map:
        obj.log2_fold_change = ExpressionLog2_Fold_Change.fromMap(map['log2_fold_change'])
    if  'comparison_name' in map:
        obj.comparison_name = map['comparison_name']
    if  'experiment_overview' in map:
        obj.experiment_overview = map['experiment_overview']
    if  'test_sample' in map:
        obj.test_sample = map['test_sample']
    if  'urls' in map:
        obj.urls = map['urls']
    if  'reference_sample' in map:
        obj.reference_sample = map['reference_sample']
    if  'evidence_codes' in map:
        obj.evidence_codes = map['evidence_codes']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Expression
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Expression, self).validate(logger)
    if self.unique_experiment_reference == None:
      logger.error("Expression - 'unique_experiment_reference' is required")
      error = error + 1
    if self.provenance_type == None:
      logger.error("Expression - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Expression - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Expression - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Expression - 'association_score' is required")
      error = error + 1
    if not self.log2_fold_change or self.log2_fold_change == None :
        logger.error("Expression - 'log2_fold_change' is required")
        error = error + 1
    elif not isinstance(self.log2_fold_change, ExpressionLog2_Fold_Change):
        logger.error("ExpressionLog2_Fold_Change class instance expected for attribute - 'log2_fold_change'")
        error = error + 1
    else:
        log2_fold_change_error = self.log2_fold_change.validate(logger)
        error = error + log2_fold_change_error
    if not self.comparison_name or self.comparison_name == None :
        logger.error("Expression - 'comparison_name' is required")
        error = error + 1
    if self.comparison_name and not isinstance(self.comparison_name, basestring):
        logger.error("Expression - 'comparison_name' type should be a string")
        error = error + 1
    if not self.experiment_overview or self.experiment_overview == None :
        logger.error("Expression - 'experiment_overview' is required")
        error = error + 1
    if self.experiment_overview and not isinstance(self.experiment_overview, basestring):
        logger.error("Expression - 'experiment_overview' type should be a string")
        error = error + 1
    if not self.test_sample or self.test_sample == None :
        logger.error("Expression - 'test_sample' is required")
        error = error + 1
    if self.test_sample and not isinstance(self.test_sample, basestring):
        logger.error("Expression - 'test_sample' type should be a string")
        error = error + 1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Expression - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    if not self.reference_sample or self.reference_sample == None :
        logger.error("Expression - 'reference_sample' is required")
        error = error + 1
    if self.reference_sample and not isinstance(self.reference_sample, basestring):
        logger.error("Expression - 'reference_sample' type should be a string")
        error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Expression - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Expression - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Expression, self).serialize()
    if not self.log2_fold_change is None: classDict['log2_fold_change'] = self.log2_fold_change.serialize()
    if not self.comparison_name is None: classDict['comparison_name'] = self.comparison_name
    if not self.experiment_overview is None: classDict['experiment_overview'] = self.experiment_overview
    if not self.test_sample is None: classDict['test_sample'] = self.test_sample
    if not self.urls is None: classDict['urls'] = self.urls
    if not self.reference_sample is None: classDict['reference_sample'] = self.reference_sample
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/expression.json inner class:(log2_fold_change)
"""
class ExpressionLog2_Fold_Change(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param percentile_rank = 0
  :param value = 0
  """
  def __init__(self, percentile_rank = 0, value = 0):
    
    """
    Name: percentile_rank
    Type: number
    Required: {True}
    """
    self.percentile_rank = percentile_rank
    
    """
    Name: value
    Type: number
    Required: {True}
    """
    self.value = value
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.percentile_rank:
        obj.percentile_rank = clone.percentile_rank
    if clone.value:
        obj.value = clone.value
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['percentile_rank','value']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Expression - DictType expected - {0} found\n".format(type(map)))
      return
    if  'percentile_rank' in map:
        obj.percentile_rank = map['percentile_rank']
    if  'value' in map:
        obj.value = map['value']
    for key in map:
      if not key in cls_keys:
        logger.error("Expression - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class ExpressionLog2_Fold_Change
    :returns: number of errors found during validation
    """
    error = 0
    if not self.percentile_rank or self.percentile_rank == None :
        logger.error("ExpressionLog2_Fold_Change - 'percentile_rank' is required")
        error = error + 1
    if not self.value or self.value == None :
        logger.error("ExpressionLog2_Fold_Change - 'value' is required")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.percentile_rank is None: classDict['percentile_rank'] = self.percentile_rank
    if not self.value is None: classDict['value'] = self.value
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/literature_curated.json
"""
class Literature_Curated(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param known_mutations = None
  :param evidence_codes = None
  :param urls = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, known_mutations = None, evidence_codes = None, urls = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Literature_Curated, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    
    """
    Name: known_mutations
    Type: string
    Description: A comma-separated list of mutations e.g. A613K,T50I etc.
    """
    self.known_mutations = known_mutations
    
    """
    Name: evidence_codes
    Type: array
    Description: An array of evidence codes
    Required: {True}
    """
    if evidence_codes is None:
        self.evidence_codes = []
    else:
        self.evidence_codes = evidence_codes
    
    """
    Name: urls
    Type: array
    """
    if urls is None:
        self.urls = []
    else:
        self.urls = urls
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Literature_Curated, cls).cloneObject(clone)
    if clone.known_mutations:
        obj.known_mutations = clone.known_mutations
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['known_mutations','evidence_codes','urls']
    obj = super(Literature_Curated, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'known_mutations' in map:
        obj.known_mutations = map['known_mutations']
    if  'evidence_codes' in map:
        obj.evidence_codes = map['evidence_codes']
    if  'urls' in map:
        obj.urls = map['urls']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Literature_Curated
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Literature_Curated, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Literature_Curated - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Literature_Curated - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Literature_Curated - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Literature_Curated - 'association_score' is required")
      error = error + 1
    if self.known_mutations and not isinstance(self.known_mutations, basestring):
        logger.error("Literature_Curated - 'known_mutations' type should be a string")
        error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Literature_Curated - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Literature_Curated - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Literature_Curated - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Literature_Curated, self).serialize()
    if not self.known_mutations is None: classDict['known_mutations'] = self.known_mutations
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/literature_mining.json
"""
class Literature_Mining(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param literature_ref = None
  :param evidence_codes = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, literature_ref = None, evidence_codes = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Literature_Mining, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    """
    Name: literature_ref
    """
    self.literature_ref = literature_ref
    
    """
    Name: evidence_codes
    Type: array
    Description: An array of evidence codes
    Required: {True}
    """
    if evidence_codes is None:
        self.evidence_codes = []
    else:
        self.evidence_codes = evidence_codes
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Literature_Mining, cls).cloneObject(clone)
    obj.literature_ref = Single_Lit_Reference.cloneObject(clone.literature_ref)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['literature_ref','evidence_codes']
    obj = super(Literature_Mining, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'literature_ref' in map:
        obj.literature_ref = Single_Lit_Reference.fromMap(map['literature_ref'])
    if  'evidence_codes' in map:
        obj.evidence_codes = map['evidence_codes']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Literature_Mining
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Literature_Mining, self).validate(logger)
    if self.unique_experiment_reference == None:
      logger.error("Literature_Mining - 'unique_experiment_reference' is required")
      error = error + 1
    if self.provenance_type == None:
      logger.error("Literature_Mining - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Literature_Mining - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Literature_Mining - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Literature_Mining - 'association_score' is required")
      error = error + 1
    if not self.literature_ref or self.literature_ref == None :
        logger.error("Literature_Mining - 'literature_ref' is required")
        error = error + 1
    elif not isinstance(self.literature_ref, Single_Lit_Reference):
        logger.error("Single_Lit_Reference class instance expected for attribute - 'literature_ref'")
        error = error + 1
    else:
        literature_ref_error = self.literature_ref.validate(logger)
        error = error + literature_ref_error
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Literature_Mining - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Literature_Mining - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Literature_Mining, self).serialize()
    if not self.literature_ref is None: classDict['literature_ref'] = self.literature_ref.serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
