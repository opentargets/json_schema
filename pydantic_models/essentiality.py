#!/usr/bin/env python
"""Generating json schema via pydantic models."""

from enum import Enum
import json
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

class MutationType(str, Enum):
    """Mutation class of a target in the essentiality object."""
    damaging = 'damaging'
    hotspot = 'hotspot'

class Screen(BaseModel):
    depmapId: str = Field(description="Screen identifier on DepMap.", examples=['ACH-001029'])
    cellLineName: str = Field(description="Screened cell-line name.", examples=['CHLA-10'])
    diseaseFromSource: Optional[str] = Field(description="Disease represented by the applied cell-line.", examples=['Ewing Sarcoma'])
    diseaseCellLineId: Optional[str] = Field(description="Sanger cell passport identifier.", examples=['SIDM01125'], regex=r'SIDM\d+')
    mutation: Optional[MutationType] = Field(description='Type of the mutation class of the target.', examples=['hotspot'])
    geneEffect: float = Field(description='Calculated DEMETER2 essentiality effect.')
    expression: Optional[float] = Field(description='Expression level of this gene in the screened cell line (log2(TPM+1)).')

    class Config:
        extra = Extra.forbid

class Screens(BaseModel):
    __root__: List[Screen] = Field(unique=True)

class DepMapEssentiality(BaseModel):
    tissueId: Optional[str] = Field(description="Tissue identifier.", examples=['UBERON_0004535', 'CL_0000057'], regex=r'(^UBERON_\\d+$|^CL_\\d+$)')
    tissueName: str = Field(description='Tissue name', examples=['liver'])
    screens: Screens

    class Config:
        extra = Extra.forbid

class DepMapEssentialities(BaseModel):
    __root__: List[DepMapEssentiality] = Field(unique=True)

class Essentiality(BaseModel):
    """Gene essentiality object."""
    targetSymbol: str = Field(description="Gene symbol.")
    isEssential: bool = Field(description="Boolean flag indicating if the target is considered essential or not by DepMap analysis.")
    depMapEssentiality: DepMapEssentialities

    class Config:
        title = 'OpenTargets-gene-essentiality'
        extra = Extra.forbid
        anystr_strip_whitespace = True

def main():
    with open('gene-essentiality.json', 'wt') as f:
        f.write(Essentiality.schema_json(indent=2))

if __name__ == '__main__':
    main()
