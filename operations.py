def add_student(students, name, score):
    students[name] = score
    return students


def update_student(students, name, new_score):
    if name in students:
        students[name] = new_score
        return True
    return False


def delete_student(students, name):
    if name in students:
        del students[name]
        return True
    return False


def top_student(students):
    if not students:
        return None
    return max(students, key=students.get)


def average_score(students):
    if not students:
        return 0
    return sum(students.values()) / len(students)