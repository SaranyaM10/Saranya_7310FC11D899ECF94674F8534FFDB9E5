class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):
  sorted_students=sorted(student_list, key=lambda student:student.cgpa,
                                     reverse=True)
  return sorted_students
students=[Student("Saranya","a133","9.1"),Student("Mubeena","a234","9.7"),Student("Thanuja","a344","9.9"),Student("Neha", "a567","9.8")]
sorted_students=sort_students(students)

for student in sorted_students:
  print("Name:{}, Roll number:{}, CGPA:{}".format(student.name,student.roll_number,student.cgpa))

