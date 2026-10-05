"""Student-related domain models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class ProjectCompletion:
    """Represents a completed project for a student."""

    name: str
    finished_at: datetime


@dataclass
class StudentProfile:
    """Represents a student and all completed projects."""

    login: str
    projects: list[ProjectCompletion] = field(default_factory=list)

    def project_names(self) -> set[str]:
        return {project.name for project in self.projects}

    def projects_in_common(self, other: "StudentProfile") -> set[str]:
        return self.project_names().intersection(other.project_names())

    @classmethod
    def from_iterable(cls, login: str, projects: Iterable[ProjectCompletion]) -> "StudentProfile":
        return cls(login=login, projects=list(projects))
