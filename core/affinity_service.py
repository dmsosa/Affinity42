"""Affinity score calculation service."""

from __future__ import annotations

from datetime import timedelta

from model import StudentProfile


class AffinityService:
    """Calculates affinity score between two students."""

    def __init__(self, bonus_window_days: int = 30, bonus_per_project: float = 0.05) -> None:
        self._bonus_window = timedelta(days=bonus_window_days)
        self._bonus_per_project = bonus_per_project

    def calculate_affinity_percent(self, a: StudentProfile, b: StudentProfile) -> float:
        jaccard = self._jaccard(a, b)
        bonus = self._temporal_bonus(a, b)
        return min((jaccard + bonus) * 100, 100.0)

    def _jaccard(self, a: StudentProfile, b: StudentProfile) -> float:
        names_a = a.project_names()
        names_b = b.project_names()
        union = names_a.union(names_b)

        if not union:
            return 0.0

        intersection = names_a.intersection(names_b)
        return len(intersection) / len(union)

    def _temporal_bonus(self, a: StudentProfile, b: StudentProfile) -> float:
        common_projects = a.projects_in_common(b)
        if not common_projects:
            return 0.0

        projects_by_name_a = {project.name: project for project in a.projects}
        projects_by_name_b = {project.name: project for project in b.projects}

        bonus_count = 0
        for project_name in common_projects:
            delta = projects_by_name_a[project_name].finished_at - projects_by_name_b[project_name].finished_at
            if abs(delta) <= self._bonus_window:
                bonus_count += 1

        return bonus_count * self._bonus_per_project
