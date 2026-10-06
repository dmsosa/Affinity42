from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class ProjectCompletion:
    project_name: str
    completed_at: date


@dataclass
class Student:
    login: str
    completions: list[ProjectCompletion] = field(default_factory=list)
