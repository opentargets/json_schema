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
import cttv.model.bioentity as bioentity
import cttv.model.evidence.phenotype as evidence_phenotype
import cttv.model.evidence.drug as evidence_drug
import cttv.model.evidence.association_score as evidence_association_score
import cttv.model.evidence.core as evidence_core
import cttv.model.evidence.genetics as evidence_genetics

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
https://raw.githubusercontent.com/CTTV/json_schema/master/src/base.json
"""
class Base(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Name: target
    """
    self.target = target
    
    """
    Name: access_level
    Type: string
    Description: Choose public as default; private is for internal datasets
    """
    self.access_level = access_level
    
    """
    Name: sourceID
    Type: string
    Description: A source ID (database or study ID) to help identify who this data is from.
    """
    self.sourceID = sourceID
    """
    Name: disease
    """
    self.disease = disease
    """
    Name: unique_association_fields
    """
    self.unique_association_fields = unique_association_fields
    
    """
    Name: validated_against_schema_version
    Type: string
    Description: The CTTV-JSON schema version number against which your data was validated
    """
    self.validated_against_schema_version = validated_against_schema_version
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    if clone.target:
        obj.target = bioentity.Target.cloneObject(clone.target)
    if clone.access_level:
        obj.access_level = clone.access_level
    if clone.sourceID:
        obj.sourceID = clone.sourceID
    if clone.disease:
        obj.disease = bioentity.Disease.cloneObject(clone.disease)
    if clone.unique_association_fields:
        obj.unique_association_fields = clone.unique_association_fields
    if clone.validated_against_schema_version:
        obj.validated_against_schema_version = clone.validated_against_schema_version
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['target','access_level','sourceID','disease','unique_association_fields','validated_against_schema_version']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'target' in map:
        obj.target = bioentity.Target.fromMap(map['target'])
    if  'access_level' in map:
        obj.access_level = map['access_level']
    if  'sourceID' in map:
        obj.sourceID = map['sourceID']
    if  'disease' in map:
        obj.disease = bioentity.Disease.fromMap(map['disease'])
    if  'unique_association_fields' in map:
        obj.unique_association_fields = map['unique_association_fields']
    if  'validated_against_schema_version' in map:
        obj.validated_against_schema_version = map['validated_against_schema_version']
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
    if self.target:
        if not isinstance(self.target, bioentity.Target):
            logger.error("bioentity.Target class instance expected for attribute - 'target'")
            error = error + 1
        else:
            target_error = self.target.validate(logger)
            error = error + target_error
    if self.access_level and not self.access_level == None and not self.access_level in ['public','private']:
        logger.error("Base - 'access_level' value is restricted to the fixed set of values 'public','private'")
        error = error + 1
    if self.access_level and not isinstance(self.access_level, basestring):
        logger.error("Base - 'access_level' type should be a string")
        error = error + 1
    if self.sourceID and not isinstance(self.sourceID, basestring):
        logger.error("Base - 'sourceID' type should be a string")
        error = error + 1
    if self.disease:
        if not isinstance(self.disease, bioentity.Disease):
            logger.error("bioentity.Disease class instance expected for attribute - 'disease'")
            error = error + 1
        else:
            disease_error = self.disease.validate(logger)
            error = error + disease_error
    if self.unique_association_fields and not isinstance(self.unique_association_fields, dict):
        logger.error("dictionary expected for attribute - 'unique_association_fields'")
        error = error + 1
    if self.validated_against_schema_version and not self.validated_against_schema_version == None and not self.validated_against_schema_version in ['1.1','1.2']:
        logger.error("Base - 'validated_against_schema_version' value is restricted to the fixed set of values '1.1','1.2'")
        error = error + 1
    if self.validated_against_schema_version and not isinstance(self.validated_against_schema_version, basestring):
        logger.error("Base - 'validated_against_schema_version' type should be a string")
        error = error + 1
    return error
  
  def serialize(self):
    classDict = {}
    if not self.target is None: classDict['target'] = self.target.serialize()
    if not self.access_level is None: classDict['access_level'] = self.access_level
    if not self.sourceID is None: classDict['sourceID'] = self.sourceID
    if not self.disease is None: classDict['disease'] = self.disease.serialize()
    if not self.unique_association_fields is None: classDict['unique_association_fields'] = self.unique_association_fields
    if not self.validated_against_schema_version is None: classDict['validated_against_schema_version'] = self.validated_against_schema_version
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/animal_models.json
"""
class Animal_Models(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param human_phenotype = None
  :param     modelorg_phenotype = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, human_phenotype = None,     modelorg_phenotype = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Animal_Models, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: human_phenotype
    """
    self.human_phenotype = human_phenotype
    """
    Name: modelorg_phenotype
    """
    self.modelorg_phenotype = modelorg_phenotype
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Animal_Models, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.human_phenotype = bioentity.Phenotype.cloneObject(clone.human_phenotype)
    if clone.modelorg_phenotype:
        obj.modelorg_phenotype = bioentity.Phenotype.cloneObject(clone.modelorg_phenotype)
    obj.evidence = Animal_ModelsEvidence.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','human_phenotype','modelorg_phenotype','evidence']
    obj = super(Animal_Models, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'human_phenotype' in map:
        obj.human_phenotype = bioentity.Phenotype.fromMap(map['human_phenotype'])
    if  'modelorg_phenotype' in map:
        obj.modelorg_phenotype = bioentity.Phenotype.fromMap(map['modelorg_phenotype'])
    if  'evidence' in map:
        obj.evidence = Animal_ModelsEvidence.fromMap(map['evidence'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Animal_Models
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Animal_Models, self).validate(logger)
    if self.target == None:
      logger.error("Animal_Models - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Animal_Models - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Animal_Models - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Animal_Models - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Animal_Models - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Animal_Models - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Animal_Models - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['animal_models_evidence_string']:
        logger.error("Animal_Models - 'type' value is restricted to the fixed set of values 'animal_models_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Animal_Models - 'type' type should be a string")
        error = error + 1
    if not self.human_phenotype or self.human_phenotype == None :
        logger.error("Animal_Models - 'human_phenotype' is required")
        error = error + 1
    elif not isinstance(self.human_phenotype, bioentity.Phenotype):
        logger.error("bioentity.Phenotype class instance expected for attribute - 'human_phenotype'")
        error = error + 1
    else:
        human_phenotype_error = self.human_phenotype.validate(logger)
        error = error + human_phenotype_error
    if self.modelorg_phenotype:
        if not isinstance(self.modelorg_phenotype, bioentity.Phenotype):
            logger.error("bioentity.Phenotype class instance expected for attribute - 'modelorg_phenotype'")
            error = error + 1
        else:
            modelorg_phenotype_error = self.modelorg_phenotype.validate(logger)
            error = error + modelorg_phenotype_error
    if not self.evidence or self.evidence == None :
        logger.error("Animal_Models - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, Animal_ModelsEvidence):
        logger.error("Animal_ModelsEvidence class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Animal_Models, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.human_phenotype is None: classDict['human_phenotype'] = self.human_phenotype.serialize()
    if not self.modelorg_phenotype is None: classDict['modelorg_phenotype'] = self.modelorg_phenotype.serialize()
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/animal_models.json inner class:(evidence)
"""
class Animal_ModelsEvidence(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param pheno2disease = None
  :param pheno2pheno = None
  :param target2pheno = None
  """
  def __init__(self, pheno2disease = None, pheno2pheno = None, target2pheno = None):
    """
    Name: pheno2disease
    """
    self.pheno2disease = pheno2disease
    """
    Name: pheno2pheno
    """
    self.pheno2pheno = pheno2pheno
    """
    Name: target2pheno
    """
    self.target2pheno = target2pheno
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.pheno2disease = evidence_phenotype.Pheno2Disease.cloneObject(clone.pheno2disease)
    obj.pheno2pheno = evidence_phenotype.Pheno2Pheno.cloneObject(clone.pheno2pheno)
    obj.target2pheno = evidence_phenotype.Target2Pheno.cloneObject(clone.target2pheno)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['pheno2disease','pheno2pheno','target2pheno']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Animal_Models - DictType expected - {0} found\n".format(type(map)))
      return
    if  'pheno2disease' in map:
        obj.pheno2disease = evidence_phenotype.Pheno2Disease.fromMap(map['pheno2disease'])
    if  'pheno2pheno' in map:
        obj.pheno2pheno = evidence_phenotype.Pheno2Pheno.fromMap(map['pheno2pheno'])
    if  'target2pheno' in map:
        obj.target2pheno = evidence_phenotype.Target2Pheno.fromMap(map['target2pheno'])
    for key in map:
      if not key in cls_keys:
        logger.error("Animal_Models - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Animal_ModelsEvidence
    :returns: number of errors found during validation
    """
    error = 0
    if not self.pheno2disease or self.pheno2disease == None :
        logger.error("Animal_ModelsEvidence - 'pheno2disease' is required")
        error = error + 1
    elif not isinstance(self.pheno2disease, evidence_phenotype.Pheno2Disease):
        logger.error("evidence_phenotype.Pheno2Disease class instance expected for attribute - 'pheno2disease'")
        error = error + 1
    else:
        pheno2disease_error = self.pheno2disease.validate(logger)
        error = error + pheno2disease_error
    if not self.pheno2pheno or self.pheno2pheno == None :
        logger.error("Animal_ModelsEvidence - 'pheno2pheno' is required")
        error = error + 1
    elif not isinstance(self.pheno2pheno, evidence_phenotype.Pheno2Pheno):
        logger.error("evidence_phenotype.Pheno2Pheno class instance expected for attribute - 'pheno2pheno'")
        error = error + 1
    else:
        pheno2pheno_error = self.pheno2pheno.validate(logger)
        error = error + pheno2pheno_error
    if not self.target2pheno or self.target2pheno == None :
        logger.error("Animal_ModelsEvidence - 'target2pheno' is required")
        error = error + 1
    elif not isinstance(self.target2pheno, evidence_phenotype.Target2Pheno):
        logger.error("evidence_phenotype.Target2Pheno class instance expected for attribute - 'target2pheno'")
        error = error + 1
    else:
        target2pheno_error = self.target2pheno.validate(logger)
        error = error + target2pheno_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.pheno2disease is None: classDict['pheno2disease'] = self.pheno2disease.serialize()
    if not self.pheno2pheno is None: classDict['pheno2pheno'] = self.pheno2pheno.serialize()
    if not self.target2pheno is None: classDict['target2pheno'] = self.target2pheno.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/drug.json
"""
class Drug(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param drug = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, drug = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Drug, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: drug
    """
    self.drug = drug
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Drug, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.drug = bioentity.Drug.cloneObject(clone.drug)
    obj.evidence = DrugEvidence.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','drug','evidence']
    obj = super(Drug, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'drug' in map:
        obj.drug = bioentity.Drug.fromMap(map['drug'])
    if  'evidence' in map:
        obj.evidence = DrugEvidence.fromMap(map['evidence'])
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
    if self.target == None:
      logger.error("Drug - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Drug - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Drug - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Drug - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Drug - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Drug - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Drug - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['drug_evidence_string']:
        logger.error("Drug - 'type' value is restricted to the fixed set of values 'drug_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Drug - 'type' type should be a string")
        error = error + 1
    if not self.drug or self.drug == None :
        logger.error("Drug - 'drug' is required")
        error = error + 1
    elif not isinstance(self.drug, bioentity.Drug):
        logger.error("bioentity.Drug class instance expected for attribute - 'drug'")
        error = error + 1
    else:
        drug_error = self.drug.validate(logger)
        error = error + drug_error
    if not self.evidence or self.evidence == None :
        logger.error("Drug - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, DrugEvidence):
        logger.error("DrugEvidence class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Drug, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.drug is None: classDict['drug'] = self.drug.serialize()
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/drug.json inner class:(evidence)
"""
class DrugEvidence(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param target2drug = None
  :param drug2clinic = None
  :param association_score = None
  """
  def __init__(self, target2drug = None, drug2clinic = None, association_score = None):
    """
    Name: target2drug
    """
    self.target2drug = target2drug
    """
    Name: drug2clinic
    """
    self.drug2clinic = drug2clinic
    """
    Name: association_score
    """
    self.association_score = association_score
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.target2drug = evidence_drug.Target2Drug.cloneObject(clone.target2drug)
    obj.drug2clinic = evidence_drug.Drug2Clinic.cloneObject(clone.drug2clinic)
    obj.association_score = clone.association_score
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['target2drug','drug2clinic','association_score']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Drug - DictType expected - {0} found\n".format(type(map)))
      return
    if  'target2drug' in map:
        obj.target2drug = evidence_drug.Target2Drug.fromMap(map['target2drug'])
    if  'drug2clinic' in map:
        obj.drug2clinic = evidence_drug.Drug2Clinic.fromMap(map['drug2clinic'])
    obj.association_score = map['association_score']
    for key in map:
      if not key in cls_keys:
        logger.error("Drug - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class DrugEvidence
    :returns: number of errors found during validation
    """
    error = 0
    if not self.target2drug or self.target2drug == None :
        logger.error("DrugEvidence - 'target2drug' is required")
        error = error + 1
    elif not isinstance(self.target2drug, evidence_drug.Target2Drug):
        logger.error("evidence_drug.Target2Drug class instance expected for attribute - 'target2drug'")
        error = error + 1
    else:
        target2drug_error = self.target2drug.validate(logger)
        error = error + target2drug_error
    if not self.drug2clinic or self.drug2clinic == None :
        logger.error("DrugEvidence - 'drug2clinic' is required")
        error = error + 1
    elif not isinstance(self.drug2clinic, evidence_drug.Drug2Clinic):
        logger.error("evidence_drug.Drug2Clinic class instance expected for attribute - 'drug2clinic'")
        error = error + 1
    else:
        drug2clinic_error = self.drug2clinic.validate(logger)
        error = error + drug2clinic_error
    if not self.association_score or self.association_score == None:
        logger.error("DrugEvidence - 'association_score' is required")
        error = error + 1
    elif not( isinstance(self.association_score, evidence_association_score.Pvalue) or isinstance(self.association_score, evidence_association_score.Probability) or isinstance(self.association_score, evidence_association_score.Rank) or isinstance(self.association_score, evidence_association_score.Summed_Total)):
        logger.error("DrugEvidence - 'association_score' incorrect type")
        error = error + 1
    else:
        association_score_error = self.association_score.validate(logger)
        error = error + association_score_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.target2drug is None: classDict['target2drug'] = self.target2drug.serialize()
    if not self.drug2clinic is None: classDict['drug2clinic'] = self.drug2clinic.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/expression.json
"""
class Expression(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Expression, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Expression, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.evidence = evidence_core.Expression.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','evidence']
    obj = super(Expression, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'evidence' in map:
        obj.evidence = evidence_core.Expression.fromMap(map['evidence'])
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
    if self.target == None:
      logger.error("Expression - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Expression - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Expression - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Expression - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Expression - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Expression - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Expression - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['expression_evidence_string']:
        logger.error("Expression - 'type' value is restricted to the fixed set of values 'expression_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Expression - 'type' type should be a string")
        error = error + 1
    if not self.evidence or self.evidence == None :
        logger.error("Expression - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, evidence_core.Expression):
        logger.error("evidence_core.Expression class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Expression, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/genetics.json
"""
class Genetics(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param variant = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, variant = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Genetics, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: variant
    """
    self.variant = variant
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Genetics, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.variant = bioentity.Variant.cloneObject(clone.variant)
    obj.evidence = GeneticsEvidence.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','variant','evidence']
    obj = super(Genetics, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'variant' in map:
        obj.variant = bioentity.Variant.fromMap(map['variant'])
    if  'evidence' in map:
        obj.evidence = GeneticsEvidence.fromMap(map['evidence'])
    for key in map:
      if not key in cls_keys:
        logger.error("None - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class Genetics
    :returns: number of errors found during validation
    """
    error = 0
    # cumulate errors from super class
    error = error + super(Genetics, self).validate(logger)
    if self.target == None:
      logger.error("Genetics - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Genetics - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Genetics - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Genetics - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Genetics - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Genetics - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Genetics - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['genetics_evidence_string']:
        logger.error("Genetics - 'type' value is restricted to the fixed set of values 'genetics_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Genetics - 'type' type should be a string")
        error = error + 1
    if not self.variant or self.variant == None :
        logger.error("Genetics - 'variant' is required")
        error = error + 1
    elif not isinstance(self.variant, bioentity.Variant):
        logger.error("bioentity.Variant class instance expected for attribute - 'variant'")
        error = error + 1
    else:
        variant_error = self.variant.validate(logger)
        error = error + variant_error
    if not self.evidence or self.evidence == None :
        logger.error("Genetics - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, GeneticsEvidence):
        logger.error("GeneticsEvidence class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Genetics, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.variant is None: classDict['variant'] = self.variant.serialize()
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/genetics.json inner class:(evidence)
"""
class GeneticsEvidence(object):
  """
  Constructor using all fields with default values
  Arguments:
  :param variant2disease = None
  :param gene2variant = None
  :param association_score = None
  """
  def __init__(self, variant2disease = None, gene2variant = None, association_score = None):
    """
    Name: variant2disease
    """
    self.variant2disease = variant2disease
    """
    Name: gene2variant
    """
    self.gene2variant = gene2variant
    """
    Name: association_score
    """
    self.association_score = association_score
  
  @classmethod
  def cloneObject(cls, clone):
    obj = cls()
    obj.variant2disease = evidence_genetics.Variant2Disease.cloneObject(clone.variant2disease)
    obj.gene2variant = evidence_genetics.Gene2Variant.cloneObject(clone.gene2variant)
    obj.association_score = clone.association_score
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['variant2disease','gene2variant','association_score']
    obj = cls()
    if not isinstance(map, types.DictType):
      logger.error("Genetics - DictType expected - {0} found\n".format(type(map)))
      return
    if  'variant2disease' in map:
        obj.variant2disease = evidence_genetics.Variant2Disease.fromMap(map['variant2disease'])
    if  'gene2variant' in map:
        obj.gene2variant = evidence_genetics.Gene2Variant.fromMap(map['gene2variant'])
    obj.association_score = map['association_score']
    for key in map:
      if not key in cls_keys:
        logger.error("Genetics - invalid field - {0} found".format(key))
    return obj
  
  def validate(self, logger):
    """
    Validate class GeneticsEvidence
    :returns: number of errors found during validation
    """
    error = 0
    if not self.variant2disease or self.variant2disease == None :
        logger.error("GeneticsEvidence - 'variant2disease' is required")
        error = error + 1
    elif not isinstance(self.variant2disease, evidence_genetics.Variant2Disease):
        logger.error("evidence_genetics.Variant2Disease class instance expected for attribute - 'variant2disease'")
        error = error + 1
    else:
        variant2disease_error = self.variant2disease.validate(logger)
        error = error + variant2disease_error
    if not self.gene2variant or self.gene2variant == None :
        logger.error("GeneticsEvidence - 'gene2variant' is required")
        error = error + 1
    elif not isinstance(self.gene2variant, evidence_genetics.Gene2Variant):
        logger.error("evidence_genetics.Gene2Variant class instance expected for attribute - 'gene2variant'")
        error = error + 1
    else:
        gene2variant_error = self.gene2variant.validate(logger)
        error = error + gene2variant_error
    if not self.association_score or self.association_score == None:
        logger.error("GeneticsEvidence - 'association_score' is required")
        error = error + 1
    elif not( isinstance(self.association_score, evidence_association_score.Pvalue) or isinstance(self.association_score, evidence_association_score.Probability) or isinstance(self.association_score, evidence_association_score.Rank) or isinstance(self.association_score, evidence_association_score.Summed_Total)):
        logger.error("GeneticsEvidence - 'association_score' incorrect type")
        error = error + 1
    else:
        association_score_error = self.association_score.validate(logger)
        error = error + association_score_error
    return error
  
  def serialize(self):
    classDict = {}
    if not self.variant2disease is None: classDict['variant2disease'] = self.variant2disease.serialize()
    if not self.gene2variant is None: classDict['gene2variant'] = self.gene2variant.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/literature_curated.json
"""
class Literature_Curated(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Literature_Curated, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Literature_Curated, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.evidence = evidence_core.Literature_Curated.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','evidence']
    obj = super(Literature_Curated, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'evidence' in map:
        obj.evidence = evidence_core.Literature_Curated.fromMap(map['evidence'])
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
    if self.target == None:
      logger.error("Literature_Curated - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Literature_Curated - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Literature_Curated - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Literature_Curated - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Literature_Curated - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Literature_Curated - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Literature_Curated - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['genetics_curated_literature_evidence_string','affected_pathways_curated_literature_evidence_string','somatic_mutations_curated_literature_evidence_string']:
        logger.error("Literature_Curated - 'type' value is restricted to the fixed set of values 'genetics_curated_literature_evidence_string','affected_pathways_curated_literature_evidence_string','somatic_mutations_curated_literature_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Literature_Curated - 'type' type should be a string")
        error = error + 1
    if not self.evidence or self.evidence == None :
        logger.error("Literature_Curated - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, evidence_core.Literature_Curated):
        logger.error("evidence_core.Literature_Curated class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Literature_Curated, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)

"""
https://raw.githubusercontent.com/CTTV/json_schema/master/src/literature_mining.json
"""
class Literature_Mining(Base):
  """
  Constructor using all fields with default values
  Arguments:
  :param type = None
  :param evidence = None
  :param     target = None
  :param access_level = None
  :param sourceID = None
  :param     disease = None
  :param unique_association_fields = None
  :param validated_against_schema_version = None
  """
  def __init__(self, type = None, evidence = None,     target = None, access_level = None, sourceID = None,     disease = None, unique_association_fields = None, validated_against_schema_version = None):
    """
    Call super constructor
    BaseClassName.__init__(self, args)
    """
    super(Literature_Mining, self).__init__(target = target,access_level = access_level,sourceID = sourceID,disease = disease,unique_association_fields = unique_association_fields,validated_against_schema_version = validated_against_schema_version)
    
    """
    Name: type
    Type: string
    Required: {True}
    """
    self.type = type
    """
    Name: evidence
    """
    self.evidence = evidence
  
  @classmethod
  def cloneObject(cls, clone):
    # super will return an instance of the subtype
    obj = super(Literature_Mining, cls).cloneObject(clone)
    if clone.type:
        obj.type = clone.type
    obj.evidence = evidence_core.Literature_Mining.cloneObject(clone.evidence)
    return obj
  
  @classmethod
  def fromMap(cls, map):
    cls_keys = ['type','evidence']
    obj = super(Literature_Mining, cls).fromMap(map)
    if not isinstance(map, types.DictType):
      logger.error("None - DictType expected - {0} found\n".format(type(map)))
      return
    if  'type' in map:
        obj.type = map['type']
    if  'evidence' in map:
        obj.evidence = evidence_core.Literature_Mining.fromMap(map['evidence'])
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
    if self.target == None:
      logger.error("Literature_Mining - 'target' is required")
      error = error + 1
    if self.access_level == None:
      logger.error("Literature_Mining - 'access_level' is required")
      error = error + 1
    if self.sourceID == None:
      logger.error("Literature_Mining - 'sourceID' is required")
      error = error + 1
    if self.disease == None:
      logger.error("Literature_Mining - 'disease' is required")
      error = error + 1
    if self.unique_association_fields == None:
      logger.error("Literature_Mining - 'unique_association_fields' is required")
      error = error + 1
    if self.validated_against_schema_version == None:
      logger.error("Literature_Mining - 'validated_against_schema_version' is required")
      error = error + 1
    if not self.type or self.type == None :
        logger.error("Literature_Mining - 'type' is required")
        error = error + 1
    if self.type and not self.type == None and not self.type in ['literature_mining_evidence_string']:
        logger.error("Literature_Mining - 'type' value is restricted to the fixed set of values 'literature_mining_evidence_string'")
        error = error + 1
    if self.type and not isinstance(self.type, basestring):
        logger.error("Literature_Mining - 'type' type should be a string")
        error = error + 1
    if not self.evidence or self.evidence == None :
        logger.error("Literature_Mining - 'evidence' is required")
        error = error + 1
    elif not isinstance(self.evidence, evidence_core.Literature_Mining):
        logger.error("evidence_core.Literature_Mining class instance expected for attribute - 'evidence'")
        error = error + 1
    else:
        evidence_error = self.evidence.validate(logger)
        error = error + evidence_error
    return error
  
  def serialize(self):
    classDict = super(Literature_Mining, self).serialize()
    if not self.type is None: classDict['type'] = self.type
    if not self.evidence is None: classDict['evidence'] = self.evidence.serialize()
    return classDict
  
  def to_JSON(self, indentation=4):
    return json.dumps(self, default=lambda o: o.serialize(), sort_keys=True, check_circular=False, indent=indentation)
