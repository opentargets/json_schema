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
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/base.json
"""
class Base(object):
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
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
    return error
  
  def serialize(self):
    classDict = {}
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/method.json
"""
class Method(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param url = None
  :param description = None
  :param reference = None
  """
  def __init__(self, url = None, description = None, reference = None):
    
    """
    Name: url
    Type: string
    String format: uri
    """
    self.url = url
    
    """
    Name: description
    Type: string
    """
    self.description = description
    
    """
    Name: reference
    Type: string
    Description: Note for pubmed identifiers, use the URI http://europepmc.org/abstract/MED/[0-9]+
    """
    self.reference = reference
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.url:
        obj.url = clone.url
    if clone.description:
        obj.description = clone.description
    if clone.reference:
        obj.reference = clone.reference
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['url','description','reference']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'url' in map:
        obj.url = map['url']
    if  'description' in map:
        obj.description = map['description']
    if  'reference' in map:
        obj.reference = map['reference']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Method
    :returns: number of errors found during validation
    """
    error = 0
    if self.url and not isinstance(self.url, basestring):
        logger.error("Method - 'url' type should be a string")
        error = error + 1
    if self.description and not isinstance(self.description, basestring):
        logger.error("Method - 'description' type should be a string")
        error = error + 1
    """ Check regex: http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$ for validation"""
    if self.reference and not re.match('http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$', self.reference):
        logger.error("Method - reference '"+self.reference+"' does not match pattern 'http://europepmc.org/abstract/MED/[0-9]+|http://europepmc.org/articles/PMC[0-9]{4,}$'")
        logger.warn(json.dumps(self.reference, sort_keys=True, indent=2))
    if self.reference and not isinstance(self.reference, basestring):
        logger.error("Method - 'reference' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.url is None: classDict['url'] = self.url
    if not self.description is None: classDict['description'] = self.description
    if not self.reference is None: classDict['reference'] = self.reference
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/probability.json
"""
class Probability(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param probability = None
  """
  def __init__(self, probability = None):
    """
    Name: probability
    """
    self.probability = probability
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Probability, cls).cloneObject(clone)
    obj.probability = ProbabilityProbability.cloneObject(clone.probability)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['probability']
    obj = super(Probability, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'probability' in map:
        obj.probability = ProbabilityProbability.fromMap(map['probability'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Probability
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Probability, self).validate(logger)
    if not self.probability or self.probability == None :
        logger.error("Probability - 'probability' is required")
        error = error + 1
    elif not isinstance(self.probability, ProbabilityProbability):
        logger.error("ProbabilityProbability class instance expected for attribute - 'probability'")
        error = error + 1
    else:
        probability_error = self.probability.validate(logger)
        error = error + probability_error
    return error
  
  def serialize(self):
    classDict = super(Probability, self).serialize()
    if not self.probability is None: classDict['probability'] = self.probability.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/probability.json inner class:(probability)
"""
class ProbabilityProbability(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param method = None
  :param value = 0
  """
  def __init__(self, method = None, value = 0):
    """
    Name: method
    """
    self.method = method
    
    """
    Name: value
    Type: number
    Required: {True}
    """
    self.value = value
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.method = Method.cloneObject(clone.method)
    if clone.value:
        obj.value = clone.value
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['method','value']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Probability - DictType expected - {0} found\n".format(type(map)))
      return
    if  'method' in map:
        obj.method = Method.fromMap(map['method'])
    if  'value' in map:
        obj.value = map['value']
    for key in map:
      if not key in cls_keys:
        logger.error("Probability - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class ProbabilityProbability
    :returns: number of errors found during validation
    """
    error = 0
    if not self.method or self.method == None :
        logger.error("ProbabilityProbability - 'method' is required")
        error = error + 1
    elif not isinstance(self.method, Method):
        logger.error("Method class instance expected for attribute - 'method'")
        error = error + 1
    else:
        method_error = self.method.validate(logger)
        error = error + method_error
    if not self.value or self.value == None :
        logger.error("ProbabilityProbability - 'value' is required")
        error = error + 1
    if self.value < 0 or self.value > 1:
        logger.error("ProbabilityProbability - 'value': {0} should be greater than or equal to 0 and should be lower than or equal to 1".format(self.value))
        logger.error(self.to_JSON())
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.method is None: classDict['method'] = self.method.serialize()
    if not self.value is None: classDict['value'] = self.value
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/pvalue.json
"""
class Pvalue(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param pvalue = None
  """
  def __init__(self, pvalue = None):
    """
    Name: pvalue
    """
    self.pvalue = pvalue
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Pvalue, cls).cloneObject(clone)
    obj.pvalue = PvaluePvalue.cloneObject(clone.pvalue)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['pvalue']
    obj = super(Pvalue, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'pvalue' in map:
        obj.pvalue = PvaluePvalue.fromMap(map['pvalue'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Pvalue
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Pvalue, self).validate(logger)
    if not self.pvalue or self.pvalue == None :
        logger.error("Pvalue - 'pvalue' is required")
        error = error + 1
    elif not isinstance(self.pvalue, PvaluePvalue):
        logger.error("PvaluePvalue class instance expected for attribute - 'pvalue'")
        error = error + 1
    else:
        pvalue_error = self.pvalue.validate(logger)
        error = error + pvalue_error
    return error
  
  def serialize(self):
    classDict = super(Pvalue, self).serialize()
    if not self.pvalue is None: classDict['pvalue'] = self.pvalue.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/pvalue.json inner class:(pvalue)
"""
class PvaluePvalue(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param method = None
  :param value = 0
  """
  def __init__(self, method = None, value = 0):
    """
    Name: method
    """
    self.method = method
    
    """
    Name: value
    Type: number
    Required: {True}
    """
    self.value = value
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.method = Method.cloneObject(clone.method)
    if clone.value:
        obj.value = clone.value
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['method','value']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Pvalue - DictType expected - {0} found\n".format(type(map)))
      return
    if  'method' in map:
        obj.method = Method.fromMap(map['method'])
    if  'value' in map:
        obj.value = map['value']
    for key in map:
      if not key in cls_keys:
        logger.error("Pvalue - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class PvaluePvalue
    :returns: number of errors found during validation
    """
    error = 0
    if not self.method or self.method == None :
        logger.error("PvaluePvalue - 'method' is required")
        error = error + 1
    elif not isinstance(self.method, Method):
        logger.error("Method class instance expected for attribute - 'method'")
        error = error + 1
    else:
        method_error = self.method.validate(logger)
        error = error + method_error
    if not self.value or self.value == None :
        logger.error("PvaluePvalue - 'value' is required")
        error = error + 1
    if self.value < 0 or self.value > 1:
        logger.error("PvaluePvalue - 'value': {0} should be greater than or equal to 0 and should be lower than or equal to 1".format(self.value))
        logger.error(self.to_JSON())
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.method is None: classDict['method'] = self.method.serialize()
    if not self.value is None: classDict['value'] = self.value
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/rank.json
"""
class Rank(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param rank = None
  """
  def __init__(self, rank = None):
    """
    Name: rank
    """
    self.rank = rank
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.rank = RankRank.cloneObject(clone.rank)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['rank']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'rank' in map:
        obj.rank = RankRank.fromMap(map['rank'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Rank
    :returns: number of errors found during validation
    """
    error = 0
    if not self.rank or self.rank == None :
        logger.error("Rank - 'rank' is required")
        error = error + 1
    elif not isinstance(self.rank, RankRank):
        logger.error("RankRank class instance expected for attribute - 'rank'")
        error = error + 1
    else:
        rank_error = self.rank.validate(logger)
        error = error + rank_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.rank is None: classDict['rank'] = self.rank.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/rank.json inner class:(rank)
"""
class RankRank(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param position = 0
  :param     method = None
  :param sample_size = 0
  """
  def __init__(self, position = 0,     method = None, sample_size = 0):
    
    """
    Name: position
    Type: number
    Required: {True}
    """
    self.position = position
    """
    Name: method
    """
    self.method = method
    
    """
    Name: sample_size
    Type: number
    Required: {True}
    """
    self.sample_size = sample_size
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.position:
        obj.position = clone.position
    if clone.method:
        obj.method = Method.cloneObject(clone.method)
    if clone.sample_size:
        obj.sample_size = clone.sample_size
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['position','method','sample_size']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Rank - DictType expected - {0} found\n".format(type(map)))
      return
    if  'position' in map:
        obj.position = map['position']
    if  'method' in map:
        obj.method = Method.fromMap(map['method'])
    if  'sample_size' in map:
        obj.sample_size = map['sample_size']
    for key in map:
      if not key in cls_keys:
        logger.error("Rank - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class RankRank
    :returns: number of errors found during validation
    """
    error = 0
    if not self.position or self.position == None :
        logger.error("RankRank - 'position' is required")
        error = error + 1
    if self.position < 1:
        logger.error("RankRank - 'position': {0} should be greater than or equal to 1".format(self.position))
        logger.error(self.to_JSON())
        error = error+1
    if self.method:
        if not isinstance(self.method, Method):
            logger.error("Method class instance expected for attribute - 'method'")
            error = error + 1
        else:
            method_error = self.method.validate(logger)
            error = error + method_error
    if not self.sample_size or self.sample_size == None :
        logger.error("RankRank - 'sample_size' is required")
        error = error + 1
    if self.sample_size < 1:
        logger.error("RankRank - 'sample_size': {0} should be greater than or equal to 1".format(self.sample_size))
        logger.error(self.to_JSON())
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.position is None: classDict['position'] = self.position
    if not self.method is None: classDict['method'] = self.method.serialize()
    if not self.sample_size is None: classDict['sample_size'] = self.sample_size
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/summed_total.json
"""
class Summed_Total(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param summed_total = None
  """
  def __init__(self, summed_total = None):
    """
    Name: summed_total
    """
    self.summed_total = summed_total
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Summed_Total, cls).cloneObject(clone)
    obj.summed_total = Summed_TotalSummed_Total.cloneObject(clone.summed_total)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['summed_total']
    obj = super(Summed_Total, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'summed_total' in map:
        obj.summed_total = Summed_TotalSummed_Total.fromMap(map['summed_total'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Summed_Total
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Summed_Total, self).validate(logger)
    if not self.summed_total or self.summed_total == None :
        logger.error("Summed_Total - 'summed_total' is required")
        error = error + 1
    elif not isinstance(self.summed_total, Summed_TotalSummed_Total):
        logger.error("Summed_TotalSummed_Total class instance expected for attribute - 'summed_total'")
        error = error + 1
    else:
        summed_total_error = self.summed_total.validate(logger)
        error = error + summed_total_error
    return error
  
  def serialize(self):
    classDict = super(Summed_Total, self).serialize()
    if not self.summed_total is None: classDict['summed_total'] = self.summed_total.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/association_score/summed_total.json inner class:(summed_total)
"""
class Summed_TotalSummed_Total(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param method = None
  :param value = 0
  """
  def __init__(self, method = None, value = 0):
    """
    Name: method
    """
    self.method = method
    
    """
    Name: value
    Type: number
    Required: {True}
    """
    self.value = value
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.method = Method.cloneObject(clone.method)
    if clone.value:
        obj.value = clone.value
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['method','value']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Summed_Total - DictType expected - {0} found\n".format(type(map)))
      return
    if  'method' in map:
        obj.method = Method.fromMap(map['method'])
    if  'value' in map:
        obj.value = map['value']
    for key in map:
      if not key in cls_keys:
        logger.error("Summed_Total - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Summed_TotalSummed_Total
    :returns: number of errors found during validation
    """
    error = 0
    if not self.method or self.method == None :
        logger.error("Summed_TotalSummed_Total - 'method' is required")
        error = error + 1
    elif not isinstance(self.method, Method):
        logger.error("Method class instance expected for attribute - 'method'")
        error = error + 1
    else:
        method_error = self.method.validate(logger)
        error = error + method_error
    if not self.value or self.value == None :
        logger.error("Summed_TotalSummed_Total - 'value' is required")
        error = error + 1
    if self.value < 0:
        logger.error("Summed_TotalSummed_Total - 'value': {0} should be greater than or equal to 0".format(self.value))
        logger.error(self.to_JSON())
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.method is None: classDict['method'] = self.method.serialize()
    if not self.value is None: classDict['value'] = self.value
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
