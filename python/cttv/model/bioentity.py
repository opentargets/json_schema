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
import cttv.model.evidence.drug as evidence_drug

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
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/base.json
"""
class Base(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param id = None
  """
  def __init__(self, id = None):
    
    """
    Name: id
    Type: array
    """
    if id is None:
        self.id = []
    else:
        self.id = id
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['id']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'id' in map:
        obj.id = map['id']
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
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Base - 'id' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.id is None: classDict['id'] = self.id
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/disease.json
"""
class Disease(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param     biosample = None
  :param name = None
  :param id = None
  """
  def __init__(self,     biosample = None, name = None, id = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Disease, self).__init__(id = id)
    """
    Name: biosample
    """
    self.biosample = biosample
    
    """
    Name: name
    Type: array
    """
    if name is None:
        self.name = []
    else:
        self.name = name
    
    """
    Name: id
    Type: array
    Required: {True}
    """
    if id is None:
        self.id = []
    else:
        self.id = id
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Disease, cls).cloneObject(clone)
    if clone.biosample:
        obj.biosample = DiseaseBiosample.cloneObject(clone.biosample)
    if clone.name:
        obj.name = []; obj.name.extend(clone.name)
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['biosample','name','id']
    obj = super(Disease, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'biosample' in map:
        obj.biosample = DiseaseBiosample.fromMap(map['biosample'])
    if  'name' in map:
        obj.name = map['name']
    if  'id' in map:
        obj.id = map['id']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Disease
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Disease, self).validate(logger)
    if self.id == None:
      logger.error("Disease - 'id' is required")
      error = error + 1
    if self.biosample:
        if not isinstance(self.biosample, DiseaseBiosample):
            logger.error("DiseaseBiosample class instance expected for attribute - 'biosample'")
            error = error + 1
        else:
            biosample_error = self.biosample.validate(logger)
            error = error + biosample_error
    if not self.name == None and len(self.name) > 0 and not all(isinstance(n, basestring) for n in self.name):
        logger.error("Disease - 'name' array should have elements of type 'basestring'")
        error = error+1
    if not self.id or self.id == None :
        logger.error("Disease - 'id' is required")
        error = error + 1
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Disease - 'id' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Disease, self).serialize()
    if not self.biosample is None: classDict['biosample'] = self.biosample.serialize()
    if not self.name is None: classDict['name'] = self.name
    if not self.id is None: classDict['id'] = self.id
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/disease.json inner class:(biosample)
"""
class DiseaseBiosample(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param name = None
  :param id = None
  """
  def __init__(self, name = None, id = None):
    
    """
    Name: name
    Type: string
    Description: free text of the tissue / cell name
    Required: {True}
    """
    self.name = name
    
    """
    Name: id
    Type: string
    Description: EFO ID of the tissue - optional
    String format: uri
    """
    self.id = id
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.name:
        obj.name = clone.name
    if clone.id:
        obj.id = clone.id
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['name','id']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Disease - DictType expected - {0} found\n".format(type(map)))
      return
    if  'name' in map:
        obj.name = map['name']
    if  'id' in map:
        obj.id = map['id']
    for key in map:
      if not key in cls_keys:
        logger.error("Disease - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class DiseaseBiosample
    :returns: number of errors found during validation
    """
    error = 0
    if not self.name or self.name == None :
        logger.error("DiseaseBiosample - 'name' is required")
        error = error + 1
    if self.name and not isinstance(self.name, basestring):
        logger.error("DiseaseBiosample - 'name' type should be a string")
        error = error + 1
    if self.id and not isinstance(self.id, basestring):
        logger.error("DiseaseBiosample - 'id' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.name is None: classDict['name'] = self.name
    if not self.id is None: classDict['id'] = self.id
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/target.json
"""
class Target(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param target_name = None
  :param target_type = None
  :param target_class = None
  :param activity = None
  :param id = None
  """
  def __init__(self, target_name = None, target_type = None, target_class = None, activity = None, id = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Target, self).__init__(id = id)
    
    """
    Name: target_name
    Type: string
    Description: used by ChEMBL initially if they have a more canonical target name, optional
    """
    self.target_name = target_name
    
    """
    Name: target_type
    Type: string
    Description: Type of target
    Required: {True}
    """
    self.target_type = target_type
    
    """
    Name: target_class
    Type: array
    """
    if target_class is None:
        self.target_class = []
    else:
        self.target_class = target_class
    
    """
    Name: id
    Type: array
    Required: {True}
    """
    if id is None:
        self.id = []
    else:
        self.id = id
    
    """
    Name: activity
    Type: string
    Description: Activity of target in disease context
    Required: {True}
    """
    self.activity = activity
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Target, cls).cloneObject(clone)
    if clone.target_name:
        obj.target_name = clone.target_name
    if clone.target_type:
        obj.target_type = clone.target_type
    if clone.target_class:
        obj.target_class = []; obj.target_class.extend(clone.target_class)
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    if clone.activity:
        obj.activity = clone.activity
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['target_name','target_type','target_class','id','activity']
    obj = super(Target, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'target_name' in map:
        obj.target_name = map['target_name']
    if  'target_type' in map:
        obj.target_type = map['target_type']
    if  'target_class' in map:
        obj.target_class = map['target_class']
    if  'id' in map:
        obj.id = map['id']
    if  'activity' in map:
        obj.activity = map['activity']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Target
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Target, self).validate(logger)
    if self.id == None:
      logger.error("Target - 'id' is required")
      error = error + 1
    if self.target_name and not isinstance(self.target_name, basestring):
        logger.error("Target - 'target_name' type should be a string")
        error = error + 1
    if not self.target_type or self.target_type == None :
        logger.error("Target - 'target_type' is required")
        error = error + 1
    if self.target_type and not self.target_type == None and not self.target_type in ['http://identifiers.org/cttv.target/chimeric_protein','http://identifiers.org/cttv.target/gene','http://identifiers.org/cttv.target/gene_allele','http://identifiers.org/cttv.target/gene_evidence','http://identifiers.org/cttv.target/gene_in_LD_region','http://identifiers.org/cttv.target/gene_in_epigenetic_regulation_complex','http://identifiers.org/cttv.target/gene_variant','http://identifiers.org/cttv.target/pro_protein','http://identifiers.org/cttv.target/protein','http://identifiers.org/cttv.target/protein_complex','http://identifiers.org/cttv.target/protein_complex_group','http://identifiers.org/cttv.target/protein_complex_heteropolymer','http://identifiers.org/cttv.target/protein_complex_homopolymer','http://identifiers.org/cttv.target/protein_evidence','http://identifiers.org/cttv.target/protein_family','http://identifiers.org/cttv.target/protein_nucleic_acid_complex','http://identifiers.org/cttv.target/selectivity_group','http://identifiers.org/cttv.target/transcript','http://identifiers.org/cttv.target/transcript_evidence','http://identifiers.org/cttv.target/transcript_isoform','http://identifiers.org/cttv.target/protein_isoform']:
        logger.error("Target - 'target_type' value is restricted to the fixed set of values 'http://identifiers.org/cttv.target/chimeric_protein','http://identifiers.org/cttv.target/gene','http://identifiers.org/cttv.target/gene_allele','http://identifiers.org/cttv.target/gene_evidence','http://identifiers.org/cttv.target/gene_in_LD_region','http://identifiers.org/cttv.target/gene_in_epigenetic_regulation_complex','http://identifiers.org/cttv.target/gene_variant','http://identifiers.org/cttv.target/pro_protein','http://identifiers.org/cttv.target/protein','http://identifiers.org/cttv.target/protein_complex','http://identifiers.org/cttv.target/protein_complex_group','http://identifiers.org/cttv.target/protein_complex_heteropolymer','http://identifiers.org/cttv.target/protein_complex_homopolymer','http://identifiers.org/cttv.target/protein_evidence','http://identifiers.org/cttv.target/protein_family','http://identifiers.org/cttv.target/protein_nucleic_acid_complex','http://identifiers.org/cttv.target/selectivity_group','http://identifiers.org/cttv.target/transcript','http://identifiers.org/cttv.target/transcript_evidence','http://identifiers.org/cttv.target/transcript_isoform','http://identifiers.org/cttv.target/protein_isoform'")
        error = error + 1
    if self.target_type and not isinstance(self.target_type, basestring):
        logger.error("Target - 'target_type' type should be a string")
        error = error + 1
    if not self.target_class == None and len(self.target_class) > 0 and not all(isinstance(n, basestring) for n in self.target_class):
        logger.error("Target - 'target_class' array should have elements of type 'basestring'")
        error = error+1
    if not self.id or self.id == None :
        logger.error("Target - 'id' is required")
        error = error + 1
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Target - 'id' array should have elements of type 'basestring'")
        error = error+1
    if not self.activity or self.activity == None :
        logger.error("Target - 'activity' is required")
        error = error + 1
    if self.activity and not self.activity == None and not self.activity in ['http://identifiers.org/cttv.activity/decreased_transcript_level','http://identifiers.org/cttv.activity/decreased_translational_product_level','http://identifiers.org/cttv.activity/drug_negative_modulator','http://identifiers.org/cttv.activity/drug_positive_modulator','http://identifiers.org/cttv.activity/gain_of_function','http://identifiers.org/cttv.activity/increased_transcript_level','http://identifiers.org/cttv.activity/increased_translational_product_level','http://identifiers.org/cttv.activity/loss_of_function','http://identifiers.org/cttv.activity/partial_loss_of_function','http://identifiers.org/cttv.activity/up_or_down','http://identifiers.org/cttv.activity/up','http://identifiers.org/cttv.activity/down','http://identifiers.org/cttv.activity/tolerated','http://identifiers.org/cttv.activity/predicted','http://identifiers.org/cttv.activity/damaging','http://identifiers.org/cttv.activity/damaging_to_target','http://identifiers.org/cttv.activity/predicted_tolerated','http://identifiers.org/cttv.activity/predicted_damaging','http://identifiers.org/cttv.activity/tolerated_by_target']:
        logger.error("Target - 'activity' value is restricted to the fixed set of values 'http://identifiers.org/cttv.activity/decreased_transcript_level','http://identifiers.org/cttv.activity/decreased_translational_product_level','http://identifiers.org/cttv.activity/drug_negative_modulator','http://identifiers.org/cttv.activity/drug_positive_modulator','http://identifiers.org/cttv.activity/gain_of_function','http://identifiers.org/cttv.activity/increased_transcript_level','http://identifiers.org/cttv.activity/increased_translational_product_level','http://identifiers.org/cttv.activity/loss_of_function','http://identifiers.org/cttv.activity/partial_loss_of_function','http://identifiers.org/cttv.activity/up_or_down','http://identifiers.org/cttv.activity/up','http://identifiers.org/cttv.activity/down','http://identifiers.org/cttv.activity/tolerated','http://identifiers.org/cttv.activity/predicted','http://identifiers.org/cttv.activity/damaging','http://identifiers.org/cttv.activity/damaging_to_target','http://identifiers.org/cttv.activity/predicted_tolerated','http://identifiers.org/cttv.activity/predicted_damaging','http://identifiers.org/cttv.activity/tolerated_by_target'")
        error = error + 1
    if self.activity and not isinstance(self.activity, basestring):
        logger.error("Target - 'activity' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = super(Target, self).serialize()
    if not self.target_name is None: classDict['target_name'] = self.target_name
    if not self.target_type is None: classDict['target_type'] = self.target_type
    if not self.target_class is None: classDict['target_class'] = self.target_class
    if not self.id is None: classDict['id'] = self.id
    if not self.activity is None: classDict['activity'] = self.activity
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/phenotype.json
"""
class Phenotype(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param species = None
  :param id = None
  """
  def __init__(self, species = None, id = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Phenotype, self).__init__(id = id)
    
    """
    Name: id
    Type: array
    Required: {True}
    """
    if id is None:
        self.id = []
    else:
        self.id = id
    
    """
    Name: species
    Type: string
    Required: {True}
    """
    self.species = species
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Phenotype, cls).cloneObject(clone)
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    if clone.species:
        obj.species = clone.species
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['id','species']
    obj = super(Phenotype, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'id' in map:
        obj.id = map['id']
    if  'species' in map:
        obj.species = map['species']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Phenotype
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Phenotype, self).validate(logger)
    if self.id == None:
      logger.error("Phenotype - 'id' is required")
      error = error + 1
    if not self.id or self.id == None :
        logger.error("Phenotype - 'id' is required")
        error = error + 1
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Phenotype - 'id' array should have elements of type 'basestring'")
        error = error+1
    if not self.species or self.species == None :
        logger.error("Phenotype - 'species' is required")
        error = error + 1
    if self.species and not self.species == None and not self.species in ['mouse','human','rat','zebrafish','dog']:
        logger.error("Phenotype - 'species' value is restricted to the fixed set of values 'mouse','human','rat','zebrafish','dog'")
        error = error + 1
    if self.species and not isinstance(self.species, basestring):
        logger.error("Phenotype - 'species' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = super(Phenotype, self).serialize()
    if not self.id is None: classDict['id'] = self.id
    if not self.species is None: classDict['species'] = self.species
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/drug.json
"""
class Drug(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param molecule_type = None
  :param molecule_name = None
  :param     max_phase_for_all_diseases = None
  :param id = None
  """
  def __init__(self, molecule_type = None, molecule_name = None,     max_phase_for_all_diseases = None, id = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Drug, self).__init__(id = id)
    
    """
    Name: molecule_type
    Type: string
    Required: {True}
    """
    self.molecule_type = molecule_type
    
    """
    Name: molecule_name
    Type: string
    Required: {True}
    """
    self.molecule_name = molecule_name
    
    """
    Name: id
    Type: array
    Required: {True}
    """
    if id is None:
        self.id = []
    else:
        self.id = id
    """
    Name: max_phase_for_all_diseases
    """
    self.max_phase_for_all_diseases = max_phase_for_all_diseases
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Drug, cls).cloneObject(clone)
    if clone.molecule_type:
        obj.molecule_type = clone.molecule_type
    if clone.molecule_name:
        obj.molecule_name = clone.molecule_name
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    if clone.max_phase_for_all_diseases:
        obj.max_phase_for_all_diseases = evidence_drug.Diseasephase.cloneObject(clone.max_phase_for_all_diseases)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['molecule_type','molecule_name','id','max_phase_for_all_diseases']
    obj = super(Drug, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'molecule_type' in map:
        obj.molecule_type = map['molecule_type']
    if  'molecule_name' in map:
        obj.molecule_name = map['molecule_name']
    if  'id' in map:
        obj.id = map['id']
    if  'max_phase_for_all_diseases' in map:
        obj.max_phase_for_all_diseases = evidence_drug.Diseasephase.fromMap(map['max_phase_for_all_diseases'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Drug
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Drug, self).validate(logger)
    if self.id == None:
      logger.error("Drug - 'id' is required")
      error = error + 1
    if not self.molecule_type or self.molecule_type == None :
        logger.error("Drug - 'molecule_type' is required")
        error = error + 1
    if self.molecule_type and not isinstance(self.molecule_type, basestring):
        logger.error("Drug - 'molecule_type' type should be a string")
        error = error + 1
    if not self.molecule_name or self.molecule_name == None :
        logger.error("Drug - 'molecule_name' is required")
        error = error + 1
    if self.molecule_name and not isinstance(self.molecule_name, basestring):
        logger.error("Drug - 'molecule_name' type should be a string")
        error = error + 1
    if not self.id or self.id == None :
        logger.error("Drug - 'id' is required")
        error = error + 1
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Drug - 'id' array should have elements of type 'basestring'")
        error = error+1
    if self.max_phase_for_all_diseases:
        if not isinstance(self.max_phase_for_all_diseases, evidence_drug.Diseasephase):
            logger.error("evidence_drug.Diseasephase class instance expected for attribute - 'max_phase_for_all_diseases'")
            error = error + 1
        else:
            max_phase_for_all_diseases_error = self.max_phase_for_all_diseases.validate(logger)
            error = error + max_phase_for_all_diseases_error
    return error
  
  def serialize(self):
    classDict = super(Drug, self).serialize()
    if not self.molecule_type is None: classDict['molecule_type'] = self.molecule_type
    if not self.molecule_name is None: classDict['molecule_name'] = self.molecule_name
    if not self.id is None: classDict['id'] = self.id
    if not self.max_phase_for_all_diseases is None: classDict['max_phase_for_all_diseases'] = self.max_phase_for_all_diseases.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/bioentity/variant.json
"""
class Variant(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param id = None
  """
  def __init__(self, type = None, id = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Variant, self).__init__(id = id)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    
    """
    Name: id
    Type: array
    Required: {True}
    """
    if id is None:
        self.id = []
    else:
        self.id = id
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Variant, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    if clone.id:
        obj.id = []; obj.id.extend(clone.id)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','id']
    obj = super(Variant, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'id' in map:
        obj.id = map['id']
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Variant
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Variant, self).validate(logger)
    if self.id == None:
      logger.error("Variant - 'id' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Variant - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['snp single','snp multiple','structural variant']:
        logger.error("Variant - 'type' value is restricted to the fixed set of values 'snp single','snp multiple','structural variant'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Variant - 'type' type should be a string")
        error = error + 1
    if not self.id or self.id == None :
        logger.error("Variant - 'id' is required")
        error = error + 1
    if not self.id == None and len(self.id) > 0 and not all(isinstance(n, basestring) for n in self.id):
        logger.error("Variant - 'id' array should have elements of type 'basestring'")
        error = error+1
    return error
  
  def serialize(self):
    classDict = super(Variant, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.id is None: classDict['id'] = self.id
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
