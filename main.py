from fastapi import FastAPI
from models import Student, ClassInfo

app = FastAPI()
students_db = {}
classes_db = {}
registrations = {}

@app.post("/student/")
def create_student(student: Student):
    id = len(students_db) + 1
    students_db[id] = student
    return {"id": id, "student": student}

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    students_db[student_id] = student
    return {"message": "Updated"}

@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    students_db.pop(student_id, None)
    return {"message": "Deleted"}

@app.post("/class/")
def create_class(classinfo: ClassInfo):
    id = len(classes_db) + 1
    classes_db[id] = classinfo
    return {"id": id, "class": classinfo}

@app.put("/class/{class_id}")
def update_class(class_id: int, classinfo: ClassInfo):
    classes_db[class_id] = classinfo
    return {"message": "Updated"}

@app.delete("/class/{class_id}")
def delete_class(class_id: int):
    classes_db.pop(class_id, None)
    return {"message": "Deleted"}

@app.post("/register/{student_id}/{class_id}")
def register_student(student_id: int, class_id: int):
    registrations.setdefault(class_id, []).append(student_id)
    return {"message": "Student registered"}

@app.get("/class/{class_id}/students")
def get_registered_students(class_id: int):
    ids = registrations.get(class_id, [])
    return [students_db[i] for i in ids]
