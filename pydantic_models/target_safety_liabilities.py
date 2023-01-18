import json
from typing import List, Optional

from pydantic import BaseModel, Extra, Field
from pydantic.schema import schema


class Biosample(BaseModel):
    """
    Anatomical structures referenced in resource.
    """

    cellFormat: Optional[str] = Field(description='Cellular or subcellular format of the assay.', examples='cell line')
    cellLabel: Optional[str] = Field(description='Name of the cell line or primary cell in source.', examples='T47D')
    tissueId: Optional[str] = Field(description='Identifier of the tissue in the UBERON ontology.', examples='UBERON_0004535')
    tissueLabel: Optional[str] = Field(description='Anatomical entity at an organ-level of the protein or cell used in the assay.', examples='cardiovascular system')

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class Biosamples(BaseModel):
    __root__: List[Biosample] = Field(unique_items=True)

class Effect(BaseModel):
    """
    Effect on target modulation.
    """

    direction: str = Field(description='Direction of the effect.')
    dosing: str = Field(description='Required dose to achieve the response.')
    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class Effects(BaseModel):
    __root__: List[Effect] = Field(unique_items=True)

class Study(BaseModel):
    """
    Characteristics of the study.
    """

    description: Optional[str] = Field(description='Description of the study.')
    name: Optional[str] = Field(description='Name of the study.', examples='ACEA_ER_80hr')
    type: Optional[str] = Field(description='Conceptual biological and/or chemical features of the study.', examples='cell-based')        
    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class Studies(BaseModel):
    __root__: List[Study] = Field(unique_items=True)

class TargetSafety(BaseModel):
    """
    OpenTargets Target Safety Liabilities model.
    """

    id: Optional[str] = Field(description='Target ID (accepted sources include Ensembl gene ID, Uniprot ID).', examples='ENSG00000133019')
    targetFromSourceId: Optional[str] = Field(description='Gene symbol in resource of origin.', examples='ESR1')
    event: str = Field(description='Identifier of the biological process in the EFO ontology.', examples='arrhythmia')
    eventId: Optional[str] = Field(description='Identifier of the safety event in the EFO ontology.', examples='EFO_0004269')
    biosample: Optional[Biosamples]
    effects: Optional[Effects]
    datasource: str = Field(description='Source of safety event.')
    literature: Optional[str] = Field(description='PubMed reference identifier.', regex='\d+$')
    study: Optional[Studies]
    url: Optional[str]

    class Config:
        title = 'OpenTargets-target-safety'
        extra = Extra.forbid
        anystr_strip_whitespace = True

### Example validation

ex = '{"id":"ENSG00000082556","event":"interaction with dopaminergic transmission and hallucination","datasource":"Urban et al. (2012)","url":"https://doi.org/10.1002/9781118098141.ch2","biosample":[{"tissueLabel":"nervous system","tissueId":"UBERON_0001016"}],"effects":[{"direction":"activation","dosing":"general"}]}'

def validator(item):
    try:
        TargetSafety(**json.loads(item))

    except pydantic.ValidationError as exc:
        print(f"ERROR: Invalid schema: {exc}")
        return False

    return True
    
print(validator(ex))
#print(TargetSafety.schema_json(indent=2))