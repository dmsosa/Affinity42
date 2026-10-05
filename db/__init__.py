"""Database/repository layer abstractions for Affinity42."""

from .student_repository import InMemoryStudentRepository, StudentRepository

__all__ = ["InMemoryStudentRepository", "StudentRepository"]
