grades = {
    "Ali": 90,
    "Muhammad": 85,
    "Maryam Ceesay": 100
}

highest_student = max(grades, key=grades.get)

print("Top student:", highest_student)
print("Score:", grades[highest_student])