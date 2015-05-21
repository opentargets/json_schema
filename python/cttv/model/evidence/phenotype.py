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
import cttv.model.evidence.core

__author__ = "Gautier Koscielny"
__copyright__ = "Copyright 2014-2015, The Centre for Therapeutic Target Validation (CTTV)"
__credits__ = ["Gautier Koscielny", "Samiul Hasan"]
__license__ = "Apache 2.0"
__version__ = "1.2"
__maintainer__ = "Gautier Koscielny"
__email__ = "gautierk@targetvalidation.org"
__status__ = "Production"

logger = logging.getLogger(__name__)
import cttv.model.evidence.core as evidence_core
"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/phenotype/pheno2disease.json
"""
class Pheno2Disease(evidence_core.Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param evidence_codes = None
  :param urls = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, evidence_codes = None, urls = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Pheno2Disease, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    
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
    obj = super(Pheno2Disease, cls).cloneObject(clone)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['evidence_codes','urls']
    obj = super(Pheno2Disease, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
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
    Validate class Pheno2Disease
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Pheno2Disease, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Pheno2Disease - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Pheno2Disease - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Pheno2Disease - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Pheno2Disease - 'association_score' is required")
      error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Pheno2Disease - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Pheno2Disease - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Pheno2Disease - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Pheno2Disease, self).serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
import cttv.model.evidence.core as evidence_core
"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/phenotype/pheno2pheno.json
"""
class Pheno2Pheno(evidence_core.Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param evidence_codes = None
  :param urls = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, evidence_codes = None, urls = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Pheno2Pheno, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    
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
    obj = super(Pheno2Pheno, cls).cloneObject(clone)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['evidence_codes','urls']
    obj = super(Pheno2Pheno, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
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
    Validate class Pheno2Pheno
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Pheno2Pheno, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Pheno2Pheno - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Pheno2Pheno - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Pheno2Pheno - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Pheno2Pheno - 'association_score' is required")
      error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Pheno2Pheno - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Pheno2Pheno - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Pheno2Pheno - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Pheno2Pheno, self).serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
import cttv.model.evidence.core as evidence_core
"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/phenotype/target2pheno.json
"""
class Target2Pheno(evidence_core.Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param evidence_codes = None
  :param urls = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, evidence_codes = None, urls = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Target2Pheno, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    
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
    obj = super(Target2Pheno, cls).cloneObject(clone)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['evidence_codes','urls']
    obj = super(Target2Pheno, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
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
    Validate class Target2Pheno
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Target2Pheno, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Target2Pheno - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Target2Pheno - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Target2Pheno - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Target2Pheno - 'association_score' is required")
      error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Target2Pheno - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Target2Pheno - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Target2Pheno - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Target2Pheno, self).serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
