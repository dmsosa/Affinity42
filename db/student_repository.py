"""Student repository abstractions."""

from __future__ import annotations

from typing import Protocol

from model import StudentProfile


class StudentRepository(Protocol):
    """Contract for retrieving student profiles."""

    def get_by_login(self, login: str) -> StudentProfile | None:
        ...

    def list_all(self) -> list[StudentProfile]:
        ...


class InMemoryStudentRepository:
    """Simple in-memory repository implementation."""

    def __init__(self, students: list[StudentProfile] | None = None) -> None:
        self._students = {student.login: student for student in students or []}

    def add(self, student: StudentProfile) -> None:
        self._students[student.login] = student

    def get_by_login(self, login: str) -> StudentProfile | None:
        return self._students.get(login)

    def list_all(self) -> list[StudentProfile]:
        return list(self._students.values())
