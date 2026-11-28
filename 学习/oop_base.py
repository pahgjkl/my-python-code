students = [
    {"name": "张三", "score": 95, "class": "一班"},
    {"name": "李四", "score": 58, "class": "二班"},
    {"name": "王五", "score": 72, "class": "一班"},
    {"name": "赵六", "score": 45, "class": "二班"}
]
class StudentManager:
    def __init__(self, students_list):
        self.students_list = students_list
    def __str__(self):
        return f"共有 {len(self.students_list)} students"
    def add_student(self, name, score, class_name):
        self.students_list.append({"name": name, "score": score, "class": class_name})
        return self.students_list
    def get_failed_student(self):
        failed_name =  [stu["name"] for stu in self.students_list if stu["score"] < 60]
        return failed_name
    def update_score(self, name, new_score):
        for sti in self.students_list:
            if sti["name"] == name:
                sti["score"] = new_score
        return self.students_list

manager = StudentManager(students)
print(manager)
hi = manager.add_student("刘磊", 50, "一班")
print(hi)
hi = manager.get_failed_student()
print(hi)
hi = manager.update_score("刘磊", 100)
print(hi)