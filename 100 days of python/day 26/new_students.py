names = ["Anne", "Jay", "Arnold", "fible", "Mary", "Beth"]
import random

student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(passed_students)
