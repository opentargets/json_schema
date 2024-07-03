#!/usr/bin/env python
"""Generating json schema for expression data via pydantic models."""

from __future__ import annotations

from enum import Enum
import json
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

class ExpressionAggregated(BaseModel):
    """Expression object for aggregated data."""
    assayGroupId: str = Field(
        description="Identifier for the assay group.",
    )
    min: float = Field(
        description='Minimum value in the assay group.',
    )
    q1: float = Field(
        description='First quantile of values in the assay group.',
    )
    q2: float = Field(
        description='Median of values in the assay group.',
    )
    q3: float = Field(
        description='third quantile of values in the assay group.',
    )
    max: float = Field(
        description='Maximum expression value in the assay group.',
    )

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class ExpressionAggregatedSchema(BaseModel):
    """Schema for aggregated expression data."""
    geneProductId: str = Field(
        description="Identifier of measured gene product, protein or transcript.",
        examples=['ENSG00000157764', 'Q9HC10'],
    )
    unit: str = Field(
        description='Unit of the expression value.',
        examples=['tpms'],
    )
    expression: List[ExpressionAggregated]

    class Config:
        title = 'OpenTargets-gene-expression-aggregated'
        extra = Extra.forbid
        anystr_strip_whitespace = True

class ExperimentalDesign(BaseModel):
    """Experimental design object."""
    assayGroupId: str = Field(
        description="Identifier for the assay group.",
    )
    assayId: str = Field(
        description="Identifier for the assay.",
    )
    assayGroup: str = Field(
        description='Group of the assay.',
    )
    age: str = Field(
        description='Age of the organism.',
    )
    cultivar: str = Field(
        description='Cultivar name.',
    )
    genotype: str = Field(
        description='Genotype of the organism.',
    )
    organismPart: str = Field(
        description='Part of the organism.',
    )

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class ExpressionUnAggregated(BaseModel):
    """Expression object for unaggregated data."""
    assayId: str = Field(
        description="Identifier for the assay.",
    )
    value: float = Field(
        description='Expression value in the assay.',
    )

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class ExpressionUnaggregatedSchema(BaseModel):
    """Schema for unaggregated expression data."""
    geneProductId: str = Field(
        description="Identifier of measured gene product, protein or transcript.",
        examples=['ENSG00000157764', 'Q9HC10'],
    )
    unit: str = Field(
        description='Unit of the expression value.',
        examples=['tpms'],
    )
    expression: List[ExpressionUnAggregated]

    class Config:
        title = 'OpenTargets-gene-expression-unaggregated'
        extra = Extra.forbid
        anystr_strip_whitespace = True


class StudyMetadataSchema(BaseModel):
    """Schema for expression metadata."""
    experimentId: str = Field(
        description="Identifier for the experiment.",
    )
    experimentType: str = Field(
        description='Type of the experiment.',
    )
    species: str = Field(
        description='Species name.',
        examples=['Sorghum bicolor'],
    )
    speciesOntURI: str = Field(
        description='Species ontology URI.',
        examples=['http://purl.obolibrary.org/obo/NCBITaxon_4558'],
    )
    pubmedIds: List[str] = Field(
        description='List of pubmed identifiers.',
        examples=['28186631'],
    )
    provider: str = Field(
        description='Provider of the data.',
    )
    experimentalDesigns: List[ExperimentalDesign]

def main():
    with open('expression_aggregated.json', 'wt') as f:
        f.write(ExpressionAggregatedSchema.schema_json(indent=2))

    with open('expression_unaggregated.json', 'wt') as f:
        f.write(ExpressionUnaggregatedSchema.schema_json(indent=2))

    with open('expression_study_metadata.json', 'wt') as f:
        f.write(StudyMetadataSchema.schema_json(indent=2))

    

if __name__ == '__main__':
    main()
