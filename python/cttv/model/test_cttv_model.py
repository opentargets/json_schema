from __future__ import absolute_import, print_function
from nose.tools.nontrivial import with_setup
import sys
# the following dir contains the init file
sys.path.append('../../../../../../build')
import logging
logger = logging.getLogger(__name__)
from cttv.model.core import *
import cttv.model.bioentity as bioentity
import cttv.model.evidence.core as evidence
import cttv.model.evidence.genetics as evidence_genetics
import cttv.model.evidence.association_score as evidence_score
# import cttv.model.evidence.core as evidence_core

def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")
 
def teardown_module(module):
    print ("teardown_module after everything in this file")
 
def my_setup_function():
    print ("my_setup_function")
 
def my_teardown_function():
    print ("my_teardown_function")
 
@with_setup(my_setup_function, my_teardown_function)
def test_base_exists():
    obj = Base()
    assert not obj == None
    
@with_setup(my_setup_function, my_teardown_function)
def test_genetics_exists():
    obj = Genetics()
    assert not obj == None
    
@with_setup(my_setup_function, my_teardown_function)
def test_animal_models_exists():
    obj = Animal_Models()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_expression_exists():
    obj = Expression()
    assert not obj == None
    
@with_setup(my_setup_function, my_teardown_function)
def test_drug_exists():
    obj = Drug()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_literature_curated_exists():
    obj = Literature_Curated()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_literature_mining_exists():
    obj = Literature_Mining()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_base_create_and_clone():
    obj = Base()
    obj.access_level = "public"
    obj.sourceID = "CTTV"
    obj.validated_against_schema_version = "1.2"
    # create a target
    obj.target = bioentity.Target(id=["http://identifiers.org/ensembl/ENSG00000213724"], activity="http://identifiers.org/cttv.activity/predicted_damaging", target_type="http://identifiers.org/cttv.target/gene")
    obj.disease = bioentity.Disease(id=["http://www.ebi.ac.uk/efo/EFO_0003767"]) 
    errors = obj.validate(logger)
    assert not obj == None and errors == 0
    
@with_setup(my_setup_function, my_teardown_function)
def test_genetics_create_and_clone():
    obj = Genetics(type="genetics_evidence_string")
    obj.access_level = "public"
    obj.sourceID = "CTTV"
    obj.validated_against_schema_version = "1.2"
    obj.unique_association_fields = { "target": "http://identifiers.org/ensembl/ENSG00000213724", "object": "http://www.ebi.ac.uk/efo/EFO_0003767", "variant": "http://identifiers.org/dbsnp/rs11010067", "study_name": "cttv009_gwas_catalog", "pvalue": "2.000000039082963e-25", "pubmed_refs": "http://europepmc.org/abstract/MED/23128233" }

    # create target, disease and variant
    obj.target = bioentity.Target(id=["http://identifiers.org/ensembl/ENSG00000213724"], activity="http://identifiers.org/cttv.activity/predicted_damaging", target_type="http://identifiers.org/cttv.target/gene")
    obj.disease = bioentity.Disease(id=["http://www.ebi.ac.uk/efo/EFO_0003767"]) 
    obj.variant = bioentity.Variant(id=["http://identifiers.org/dbsnp/rs11010067"], type="snp single") 
    obj.evidence = GeneticsEvidence(
        variant2disease = evidence_genetics.Variant2Disease(  
            evidence_codes = ["http://purl.obolibrary.org/obo/ECO_0000205"], 
            unique_experiment_reference = "http://europepmc.org/abstract/MED/23128233", 
            provenance_type = evidence.BaseProvenance_Type(),
            date_asserted = "2015-05-11T11:46:09+00:00",
            association_score = evidence_score.Pvalue(pvalue = evidence_score.PvaluePvalue(value = 2.000000039082963e-25))
            ),
        gene2variant = evidence_genetics.Gene2Variant( 
            evidence_codes = [ "http://purl.obolibrary.org/obo/ECO_0000205", "http://identifiers.org/eco/cttv_mapping_pipeline" ],
            functional_consequence = "http://purl.obolibrary.org/obo/SO_0001631",
            provenance_type = evidence.BaseProvenance_Type(),
            date_asserted = "2015-05-11T11:46:09+00:00",
            association_score = evidence_score.Pvalue(pvalue = evidence_score.PvaluePvalue(value = 2.000000039082963e-25))
        )
        )
                                                                                        
    logger.info(obj.evidence.variant2disease.unique_experiment_reference)
    obj.evidence.association_score = evidence_score.Probability(probability = evidence_score.ProbabilityProbability(method=evidence_score.Method(url = "http://en.wikipedia.org/wiki/Genome-wide_association_study",
                        description = "The P value we get from the curated paper for the given variant to disease association."), value=2.000000039082963e-25))
    errors = obj.validate(logger)
    assert not obj == None and errors == 0
    
@with_setup(my_setup_function, my_teardown_function)
def test_animal_models_create_and_clone():
    obj = Animal_Models()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_expression_create_and_clone():
    obj = Expression()
    obj.access_level = "public"
    obj.sourceID = "CTTV"
    obj.validated_against_schema_version = "1.2"
    # create a target
    obj.target = bioentity.Target(id=["http://identifiers.org/ensembl/ENSG00000213724"], activity="http://identifiers.org/cttv.activity/predicted_damaging", target_type="http://identifiers.org/cttv.target/gene")
    obj.disease = bioentity.Disease(id=["http://www.ebi.ac.uk/efo/EFO_0003767"]) 
    
    assert not obj == None
    
@with_setup(my_setup_function, my_teardown_function)
def test_drug_create_and_clone():
    obj = Drug()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_literature_curated_create_and_clone():
    obj = Literature_Curated()
    assert not obj == None

@with_setup(my_setup_function, my_teardown_function)
def test_literature_mining_create_and_clone():
    obj = Literature_Mining()
    assert not obj == None

    