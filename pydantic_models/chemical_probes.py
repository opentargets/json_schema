import json
from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class Url(BaseModel):
    niceName: str
    url: Optional[str]

    class Config:
        extra = Extra.forbid
        anystr_strip_whitespace = True

class ChemicalProbes(BaseModel):
    """
    OpenTargets Chemical Probes model.
    """

    targetFromSourceId: str = Field(description='Gene symbol in resource of origin.', examples='ESR1')
    id: str = Field(description='Probe ID as reported in Probes&Drugs.', examples='IOX1')
    control: Optional[str] = Field(description='Inactive analogue of the probe.', examples='PF-04875474')
    drugId: Optional[str] = Field(description='Drug molecule ID.', examples='CHEMBL1651534')
    inchiKey: str = Field(description='ID that identifies the probe.', examples='JGRPKOGHYBAVMW-UHFFFAOYSA-N')
    urls: List[Url]
    probesDrugsScore: Optional[int] = Field(description='P&D probe-likeness score.', gt=0, le=100)
    probeMinerScore: Optional[int] = Field(description='Probe Miner probe-likeness score.', gt=0, le=100)
    scoreInCells: Optional[int] = Field(description='ChemicalProbes.org score for probe-likeness to be used in model cells.', gt=0, le=100)
    scoreInOrganisms: Optional[int] = Field(description='ChemicalProbes.org score for probe-likeness to be used in model organisms.', gt=0, le=100)
    mechanismOfAction: Optional[List[str]] = Field(description='Mechanism of action of the probe.', examples=['blocker'])
    isHighQuality: bool = Field(description='True if selected as high quality by P&D.')
    origin: List[str] = Field(description='Origin of the probe.')

    class Config:
        title = 'OpenTargets-chemical-probes'
        extra = Extra.forbid
        anystr_strip_whitespace = True

### Example validation

ex = '{"targetFromSourceId":"O00519","id":"PF-04457845","drugId":"CHEMBL1651534","inchiKey":"BATCTBJIJJEPHM-UHFFFAOYSA-N","urls":[{"niceName":"Chemical Probes.org (legacy)","url":"https://new.chemicalprobes.org/?q=PF-04457845"},{"niceName":"Open Science Probes","url":"http://www.sgc-ffm.uni-frankfurt.de/#!specificprobeoverview/PF-04457845"}],"control":"PF-04875474","probesDrugsScore":70.0,"probeMinerScore":41.0,"scoreInCells":50.0,"scoreInOrganisms":100.0,"mechanismOfAction":["inhibitor"],"isHighQuality":true,"origin":["experimental"]}'

def validator(item):
    try:
        ChemicalProbes(**json.loads(item))

    except pydantic.ValidationError as exc:
        print(f"ERROR: Invalid schema: {exc}")
        return False

    return True

print(validator(ex))
print(ChemicalProbes.schema_json(indent=2))
