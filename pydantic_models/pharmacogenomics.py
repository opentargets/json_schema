#!/usr/bin/env python
"""Generating a JSON schema via Pydantic models."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class phenotypeCategory(str, Enum):
    """Accepted phenotype categories describing pharmacogenomic effect."""

    toxicity = "toxicity"
    efficacy = "efficacy"
    dosage = "dosage"
    metabolism = ("metabolism/pk",)
    pd = "pd"
    other = "other"


class EvidenceLevel(str, Enum):
    """Evidence levels class describing the confidence in the assocations."""

    _1a = "1A"
    _1b = "1B"
    _2a = "2A"
    _2b = "2B"
    _3 = "3"
    _4 = "4"


class Pharmacogenomics(BaseModel):
    """Pharmacogenomics schema object."""

    datasourceId: str = "pharmgkb"
    datasourceVersion: str = Field(
        description="Date of data dump generation.",
        regex=r"[12]\d{3}-[01][0-9]-[0123][0-9]",
        examples=["2023-08-05"],
    )
    datatypeId: str = "clinical_annotation"
    studyId: str = Field(
        description="Clinical Annotation ID in the PharmKGB dataset.",
        examples=["1449309937"],
    )
    evidenceLevel: EvidenceLevel = Field(
        description="Level of evidence. More info: https://www.pharmgkb.org/page/clinAnnLevels.",
        examples=["1A"],
    )
    literature: List[str] = Field(
        description="List of PMIDs of supporting publications.",
    )
    genotypeId: Optional[str] = Field(
        description="VCF-style (chr_pos_ref_allele1,allele2) identifier of genotype; computed as described here: https://github.com/apriltuesday/opentargets-pharmgkb/tree/issue-18#variant-coordinate-computation.",
        examples=[
            "19_38499645_GGAG_G,GGAG",
            "20_54156202_T_C,T",
            "X_12885540_A_A"
        ],
        regex=r"^[0-9YX]{1,2}_\d+_[GATC]+_([GATC]+,)?[GATC]+$",
    )
    variantRsId: str = Field(
        description="RS identifier of the variant.",
        examples=["rs12354"],
        regex=r"^rs\d+$",
    )
    variantFunctionalConsequenceId: Optional[str] = Field(
        description="Sequence Ontology term, from VEP.",
        examples=["SO_0001822"],
        regex=r"^SO_\d+$",
    )
    targetFromSourceId: Optional[str] = Field(
        description="Ensembl gene identifier.",
        examples=["ENSG00000196218"],
        regex=r"^ENSG\d+$",
    )
    genotype: str = Field(
        description="Genotype string.", examples=["(CA)16/(CA)17", "TA", "del/GAG"]
    )
    genotypeAnnotationText: str = Field(
        description="Full annotation string for genotype.",
        examples=[
            "Patients with the rs121918596 del/GAG genotype may develop malignant hyperthermia when treated with volatile anesthetics [...]"
        ],
    )
    drugFromSource: str = Field(description="Drug name.", examples=["succinylcholine"])
    drugId: Optional[str] = Field(
        description="CHEBI ID of drug, mapped through OLS.",
        examples=["CHEBI_45652"],
        regex=r"^CHEBI_\d+$",
    )
    # pgxCategory: phenotypeCategory = Field(
    pgxCategory: str = Field(
        description="Pharmacogenomics phenotype category.", examples=["toxicity"]
    )
    phenotypeText: Optional[str] = Field(
        description="Phenotype name.", examples=["Malignant Hyperthermia"]
    )
    phenotypeFromSourceId: Optional[str] = Field(
        description="EFO ID of phenotype, mapped through ZOOMA / OXO.",
        examples=["Orphanet_423"],
        regex=r"^NCIT_C\d+$|^Orphanet_\d+$|^GO_\d+$|^HP_\d+$|^EFO_\d+$|^MONDO_\d+$|^DOID_\d+$|^MP_\d+$|^OTAR_\d+$|^PATO_\d+$|^CHEBI_\d+$|^OBI_\d+$|^OGMS_\d+$",
    )

    class Config:
        title = "OpenTargets-Pharmacogenomics"
        extra = Extra.forbid
        anystr_strip_whitespace = True


def main() -> None:
    with open("pharmacogenomics.json", "wt") as f:
        f.write(Pharmacogenomics.schema_json(indent=2))
        f.write('\n')


if __name__ == "__main__":
    main()
