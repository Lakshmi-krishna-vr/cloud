from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data stores
students = {}
classes = {}
registrations = {}

# 1. Add Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student_id = str(uuid.uuid4())
    students[student_id] = data
    return jsonify({"id": student_id, "message": "Student added"}), 201

# 2. Update Student
@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id in students:
        students[student_id] = request.json
        return jsonify({"message": "Student updated"})
    return jsonify({"error": "Student not found"}), 404

# 3. Delete Student
@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        return jsonify({"message": "Student deleted"})
    return jsonify({"error": "Student not found"}), 404

# 4. Add Class
@app.route('/classes', methods=['POST'])
def add_class():
    data = request.json
    class_id = str(uuid.uuid4())
    classes[class_id] = data
    return jsonify({"id": class_id, "message": "Class added"}), 201

# 5. Update Class
@app.route('/classes/<class_id>', methods=['PUT'])
def update_class(class_id):
    if class_id in classes:
        classes[class_id] = request.json
        return jsonify({"message": "Class updated"})
    return jsonify({"error": "Class not found"}), 404

# 6. Delete Class
@app.route('/classes/<class_id>', methods=['DELETE'])
def delete_class(class_id):
    if class_id in classes:
        del classes[class_id]
        return jsonify({"message": "Class deleted"})
    return jsonify({"error": "Class not found"}), 404

# 7. Register Student to Class
@app.route('/register', methods=['POST'])
def register_student():
    data = request.json
    student_id = data.get("student_id")
    class_id = data.get("class_id")
    if student_id not in students or class_id not in classes:
        return jsonify({"error": "Invalid student or class ID"}), 404
    registrations.setdefault(class_id, []).append(student_id)
    return jsonify({"message": "Student registered to class"})

# 8. Get Students for Class
@app.route('/classes/<class_id>/students', methods=['GET'])
def get_students_in_class(class_id):
    student_ids = registrations.get(class_id, [])
    result = [students[sid] for sid in student_ids if sid in students]
    return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
