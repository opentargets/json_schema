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
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/drug/target2drug.json
"""
class Target2Drug(evidence_core.Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param evidence_codes = None
  :param urls = None
  :param action_type = None
  :param mechanism_of_action = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, evidence_codes = None, urls = None, action_type = None, mechanism_of_action = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Target2Drug, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    
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
    
    """
    Name: action_type
    Type: string
    Required: {True}
    """
    self.action_type = action_type
    
    """
    Name: mechanism_of_action
    Type: string
    Required: {True}
    """
    self.mechanism_of_action = mechanism_of_action
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Target2Drug, cls).cloneObject(clone)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    if clone.action_type:
        obj.action_type = clone.action_type
    if clone.mechanism_of_action:
        obj.mechanism_of_action = clone.mechanism_of_action
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['evidence_codes','urls','action_type','mechanism_of_action']
    obj = super(Target2Drug, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'evidence_codes' in map:
        obj.evidence_codes = map['evidence_codes']
    if  'urls' in map:
        obj.urls = map['urls']
    if  'action_type' in map:
        obj.action_type = map['action_type']
    if  'mechanism_of_action' in map:
        obj.mechanism_of_action = map['mechanism_of_action']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Target2Drug
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Target2Drug, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Target2Drug - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Target2Drug - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Target2Drug - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Target2Drug - 'association_score' is required")
      error = error + 1
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Target2Drug - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Target2Drug - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Target2Drug - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    if not self.action_type or self.action_type == None :
        logger.error("Target2Drug - 'action_type' is required")
        error = error + 1
    if self.action_type and not isinstance(self.action_type, basestring):
        logger.error("Target2Drug - 'action_type' type should be a string")
        error = error + 1
    if not self.mechanism_of_action or self.mechanism_of_action == None :
        logger.error("Target2Drug - 'mechanism_of_action' is required")
        error = error + 1
    if self.mechanism_of_action and not isinstance(self.mechanism_of_action, basestring):
        logger.error("Target2Drug - 'mechanism_of_action' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = super(Target2Drug, self).serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    if not self.action_type is None: classDict['action_type'] = self.action_type
    if not self.mechanism_of_action is None: classDict['mechanism_of_action'] = self.mechanism_of_action
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
import cttv.model.evidence.core as evidence_core
"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/drug/drug2clinic.json
"""
class Drug2Clinic(evidence_core.Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param max_phase_for_disease = None
  :param evidence_codes = None
  :param urls = None
  :param unique_experiment_reference = None
  :param     provenance_type = None
  :param is_associated = False
  :param date_asserted = None
  :param association_score = None
  """
  def __init__(self, max_phase_for_disease = None, evidence_codes = None, urls = None, unique_experiment_reference = None,     provenance_type = None, is_associated = False, date_asserted = None, association_score = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Drug2Clinic, self).__init__(unique_experiment_reference = unique_experiment_reference,provenance_type = provenance_type,is_associated = is_associated,date_asserted = date_asserted,association_score = association_score)
    """
    Name: max_phase_for_disease
    """
    self.max_phase_for_disease = max_phase_for_disease
    
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
    obj = super(Drug2Clinic, cls).cloneObject(clone)
    obj.max_phase_for_disease = Diseasephase.cloneObject(clone.max_phase_for_disease)
    if clone.evidence_codes:
        obj.evidence_codes = []; obj.evidence_codes.extend(clone.evidence_codes)
    if clone.urls:
        obj.urls = []; obj.urls.extend(clone.urls)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['max_phase_for_disease','evidence_codes','urls']
    obj = super(Drug2Clinic, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'max_phase_for_disease' in map:
        obj.max_phase_for_disease = Diseasephase.fromMap(map['max_phase_for_disease'])
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
    Validate class Drug2Clinic
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Drug2Clinic, self).validate(logger)
    if self.provenance_type == None:
      logger.error("Drug2Clinic - 'provenance_type' is required")
      error = error + 1
    if self.is_associated == None:
      logger.error("Drug2Clinic - 'is_associated' is required")
      error = error + 1
    if self.date_asserted == None:
      logger.error("Drug2Clinic - 'date_asserted' is required")
      error = error + 1
    if self.association_score == None:
      logger.error("Drug2Clinic - 'association_score' is required")
      error = error + 1
    if not self.max_phase_for_disease or self.max_phase_for_disease == None :
        logger.error("Drug2Clinic - 'max_phase_for_disease' is required")
        error = error + 1
    elif not isinstance(self.max_phase_for_disease, Diseasephase):
        logger.error("Diseasephase class instance expected for attribute - 'max_phase_for_disease'")
        error = error + 1
    else:
        max_phase_for_disease_error = self.max_phase_for_disease.validate(logger)
        error = error + max_phase_for_disease_error
    if not self.evidence_codes or self.evidence_codes == None :
        logger.error("Drug2Clinic - 'evidence_codes' is required")
        error = error + 1
    if not self.evidence_codes == None and len(self.evidence_codes) > 0 and not all(isinstance(n, basestring) for n in self.evidence_codes):
        logger.error("Drug2Clinic - 'evidence_codes' array should have elements of type 'basestring'")
        error = error+1
    if not self.urls == None and len(self.urls) > 0 and not all(isinstance(n, Linkout) for n in self.urls):
        logger.error("Drug2Clinic - 'urls' array should have elements of type 'Linkout'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Drug2Clinic, self).serialize()
    if not self.max_phase_for_disease is None: classDict['max_phase_for_disease'] = self.max_phase_for_disease.serialize()
    if not self.evidence_codes is None: classDict['evidence_codes'] = self.evidence_codes
    if not self.urls is None: classDict['urls'] = self.urls
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/evidence/drug/diseasephase.json
"""
class Diseasephase(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param numeric_index = 0
  :param label = None
  """
  def __init__(self, numeric_index = 0, label = None):
    
    """
    Name: numeric_index
    Type: number
    Description: An integer indicating the position of this study phase. Higher the number = more advanced phase.
    Required: {True}
    """
    self.numeric_index = numeric_index
    
    """
    Name: label
    Type: string
    Required: {True}
    """
    self.label = label
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.numeric_index:
        obj.numeric_index = clone.numeric_index
    if clone.label:
        obj.label = clone.label
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['numeric_index','label']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'numeric_index' in map:
        obj.numeric_index = map['numeric_index']
    if  'label' in map:
        obj.label = map['label']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Diseasephase
    :returns: number of errors found during validation
    """
    error = 0
    if not self.numeric_index or self.numeric_index == None :
        logger.error("Diseasephase - 'numeric_index' is required")
        error = error + 1
    if not self.label or self.label == None :
        logger.error("Diseasephase - 'label' is required")
        error = error + 1
    if self.label and not isinstance(self.label, basestring):
        logger.error("Diseasephase - 'label' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.numeric_index is None: classDict['numeric_index'] = self.numeric_index
    if not self.label is None: classDict['label'] = self.label
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
