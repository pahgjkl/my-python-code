students = [
    {"name": "张三", "score": 95, "class": "一班"},
    {"name": "李四", "score": 58, "class": "二班"},
    {"name": "王五", "score": 72, "class": "一班"},
    {"name": "赵六", "score": 45, "class": "二班"}
]
def get_failed_students(selfs):
    failed_names = [self["name"] for self in selfs if self["score"] < 60]
    return failed_names
print(get_failed_students(students))
for student in students:
    if student["class"] == "一班":
        student["score"] = student["score"] + 5
    elif student["class"] == "二班":
        student["score"] = student["score"] - 2
print(students)
