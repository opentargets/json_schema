#!/usr/bin/env python
"""Generating json schema for expression data via pydantic models."""
from typing import Optional, Literal, List
from pydantic import BaseModel, Field, model_validator, Extra, constr


class UnaggregatedExpression(BaseModel):
    """Expression object for unaggregated bulk data or pseudo-bulked single-cell data."""
    expression: float = Field(
        ...,
        title="expression",
        description="Expression value for this single sample.",
        example=12.34,
    )
    sampleId: str = Field(
        ...,
        title="sampleId",
        description="Identifier for the individual sample or bulk assay.",
        example="SAMPLE123",
    )
    cellCount: Optional[int] = Field(
        None,
        title="cellCount",
        description=(
            "Number of cells that contributed to the pseudobulk expression value"
            " (only required if datatypeId is scrna‑seq)."
        ),
        example=1000,
    )
    sex: Optional[Literal["M", "F", "NB", "U"]] = Field(
        None,
        title="sex",
        description="Sex of the sample donor.",
        example="M",
    )
    age: Optional[constr(pattern=r"^[0-9]+-[0-9]+$")] = Field(
        None,
        title="age",
        description="Age range of the sample donor.",
        example="20-30",
    )

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True


class ExpressionUnaggregatedSchema(BaseModel):
    """Schema for unaggregated expression data."""
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
    datatypeId: Literal["rna-seq", "scrna-seq", "mass-spectrometry-proteomics"] = Field(
        ...,
        title="datatypeId",
        description="Identifier of the data type technology, e.g. RNA‑seq, microarray.",
        example="scrna-seq",
    )
    unit: Literal["TPM", "logCP10K", "PPB (iBAQ)"] = Field(
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
    # Source‐defined names (free text or comma‑separated)
    tissueBiosampleFromSource: Optional[str] = Field(
        None,
        title="tissueBiosampleFromSource",
        description=(
            "Name(s) of the tissue or biosample as defined by the source. "
            "Comma‐separated if multiple."
        ),
        example="aorta,vena cava",
    )
    celltypeBiosampleFromSource: Optional[str] = Field(
        None,
        title="celltypeBiosampleFromSource",
        description=(
            "Name(s) of the cell type as defined by the source. "
            "Comma‐separated if multiple."
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
    expression: List[UnaggregatedExpression]

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

    @model_validator(mode="after")
    def check_cell_count_for_scrna(cls, model):
        """Require cellCount on every expression entry if datatypeId is scrna-seq."""
        if model.datatypeId == "scrna-seq":
            for expr in model.expression:
                if expr.cellCount is None:
                    raise ValueError(
                        "`cellCount` is required for all items when `datatypeId` is 'scrna-seq'."
                    )
        return model

    class Config:
        title = 'OpenTargets-gene-expression-unaggregated'
        extra = Extra.forbid
        anystr_strip_whitespace = True


def main():
    """Generate and write the JSON schema for unaggregated expression data to a file."""
    with open('expression_unaggregated.json', 'wt') as f:
        f.write(ExpressionUnaggregatedSchema.schema_json(indent=2))


if __name__ == '__main__':
    main()
