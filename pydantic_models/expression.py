#!/usr/bin/env python
"""Generating JSON schema for expression data via Pydantic models (v2-style)."""

from typing import Optional, Literal
from pydantic import BaseModel, Field, model_validator, ConfigDict
import json


# --- Shared types -------------------------------------------------------------

DatatypeId = Literal["rna-seq", "scrna-seq", "mass-spectrometry proteomics"]
Unit = Literal["TPM", "logCP10K", "PPB (iBAQ)"]
Sex = Literal["M", "F", "NB", "U"]


# --- Base model with common fields, validator, and config ---------------------

class ExpressionBase(BaseModel):
    """Common fields for expression records (aggregated or unaggregated)."""

    # Target & provenance
    targetId: str = Field(
        ...,
        title="targetId",
        description="Ensembl gene ID for the gene product.",
        example="ENSG00000157764",
    )
    datasourceId: str = Field(
        ...,
        title="datasourceId",
        description="Identifier of the data source providing the expression data.",
        example="tabula_sapiens",
    )
    datatypeId: DatatypeId = Field(
        ...,
        title="datatypeId",
        description="Identifier of the data type technology, e.g. RNA-seq, microarray.",
        example="scrna-seq",
    )
    unit: Unit = Field(
        ...,
        title="unit",
        description="Unit of the expression value.",
        example="TPM",
    )

    # Biosample ontology IDs
    tissueBiosampleId: Optional[str] = Field(
        None,
        title="tissueBiosampleId",
        description="UBERON ID for the tissue or biosample.",
        example="UBERON:0002048",
    )
    celltypeBiosampleId: Optional[str] = Field(
        None,
        title="celltypeBiosampleId",
        description="CL ID for the cell type.",
        example="CL:0000540",
    )

    # Source-defined names (free text or comma-separated)
    tissueBiosampleFromSource: Optional[str] = Field(
        None,
        title="tissueBiosampleFromSource",
        description=(
            "Name(s) of the tissue or biosample as defined by the source. "
            "Comma-separated if multiple."
        ),
        example="aorta,vena cava",
    )
    celltypeBiosampleFromSource: Optional[str] = Field(
        None,
        title="celltypeBiosampleFromSource",
        description=(
            "Name(s) of the cell type as defined by the source. "
            "Comma-separated if multiple."
        ),
        example="neuron",
    )

    targetFromSource: Optional[str] = Field(
        None,
        title="targetFromSource",
        description=(
            "Gene symbol, UniProt ID, or other identifier for the target "
            "as provided by the data source."
        ),
        example="TP53",
    )

    # Shared config (v2-style)
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    @model_validator(mode="after")
    def check_tissue_or_celltype(cls, model):
        """Ensure either tissue OR celltype info is fully provided."""
        if not (
            (model.tissueBiosampleId and model.tissueBiosampleFromSource)
            or (model.celltypeBiosampleId and model.celltypeBiosampleFromSource)
        ):
            raise ValueError(
                "Either (tissueBiosampleId & tissueBiosampleFromSource) "
                "or (celltypeBiosampleId & celltypeBiosampleFromSource) must be set."
            )
        return model


# --- Aggregated schema --------------------------------------------------------

class ExpressionAggregatedSchema(ExpressionBase):
    """Expression object for aggregated data."""

    min: float = Field(description="Minimum value in the assay group.")
    q1: float = Field(description="First quantile of values in the assay group.")
    q2: float = Field(description="Median of values in the assay group.")
    q3: float = Field(description="Third quantile of values in the assay group.")
    max: float = Field(description="Maximum expression value in the assay group.")

    model_config = ConfigDict(title="OpenTargets-gene-expression-aggregated")


# --- Unaggregated schema ------------------------------------------------------

class ExpressionUnaggregatedSchema(ExpressionBase):
    """Schema for unaggregated (per-sample) expression data."""

    expression: float = Field(
        ...,
        title="expression",
        description="Expression value for this single sample.",
        example=12.34,
    )
    donorId: str = Field(
        ...,
        title="donorId",
        description="Identifier for the individual sample or bulk assay.",
        example="SAMPLE123",
    )
    cellCount: Optional[int] = Field(
        None,
        title="cellCount",
        description=(
            "Number of cells that contributed to the pseudobulk expression value "
            "(required if datatypeId is scrna-seq)."
        ),
        example=1000,
    )
    sex: Optional[Sex] = Field(
        None,
        title="sex",
        description="Sex of the sample donor.",
        example="M",
    )
    age: Optional[str] = Field(
        None,
        title="age",
        description="Age of the sample donor.",
        example="20-29",
    )
    ethnicity: Optional[str] = Field(
        None,
        title="ethnicity",
        description="Reported ethnicity of the sample donor.",
        example="Hispanic",
    )

    model_config = ConfigDict(title="OpenTargets-gene-expression-unaggregated")

    @model_validator(mode="after")
    def check_cell_count_for_scrna(cls, model):
        """Require cellCount on every record when datatypeId is scrna-seq."""
        if model.datatypeId == "scrna-seq" and model.cellCount is None:
            raise ValueError(
                "`cellCount` is required when `datatypeId` is 'scrna-seq'."
            )
        return model


# --- Schema emission ----------------------------------------------------------

def main():
    """Generate and write the JSON schemas to files."""
    with open("expression_unaggregated.json", "wt") as f:
        json.dump(ExpressionUnaggregatedSchema.model_json_schema(), f, indent=2)
    with open("expression_aggregated.json", "wt") as f:
        json.dump(ExpressionAggregatedSchema.model_json_schema(), f, indent=2)


if __name__ == "__main__":
    main()
