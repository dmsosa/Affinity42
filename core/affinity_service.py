from model.student import Student

RECENT_BONUS_DAYS = 30
PROJECT_BONUS = 0.05


def calculate_affinity(student_a: Student, student_b: Student) -> float:
    projects_a = {completion.project_name: completion for completion in student_a.completions}
    projects_b = {completion.project_name: completion for completion in student_b.completions}

    union = set(projects_a) | set(projects_b)
    if not union:
        return 0.0

    intersection = set(projects_a) & set(projects_b)
    jaccard = len(intersection) / len(union)

    bonus = 0.0
    for project_name in intersection:
        date_a = projects_a[project_name].completed_at
        date_b = projects_b[project_name].completed_at
        if abs((date_a - date_b).days) <= RECENT_BONUS_DAYS:
            bonus += PROJECT_BONUS

    return min((jaccard + bonus) * 100, 100.0)
