import streamlit as st

from core.affinity_service import calculate_affinity
from db.student_repository import StudentRepository


def main() -> None:
    st.set_page_config(page_title="Affinity42", layout="wide")
    st.title("Affinity42")
    st.caption("Boilerplate app ready to connect with 42 API data.")

    students = StudentRepository().list_students()
    st.write(f"Loaded students: {len(students)}")

    if len(students) >= 2:
        score = calculate_affinity(students[0], students[1])
        st.metric("Sample affinity score", f"{score:.2f}%")
    else:
        st.info("Add student data in StudentRepository to start calculating affinity.")


if __name__ == "__main__":
    main()
