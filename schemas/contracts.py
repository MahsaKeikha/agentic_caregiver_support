from dataclasses import dataclass,field
@dataclass
class CaregiverContext:
    routine:dict=field(default_factory=dict)
    observations:list=field(default_factory=list)
    communication:dict=field(default_factory=dict)
