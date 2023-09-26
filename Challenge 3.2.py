class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(students_list):
  sorted_students = sorted(students_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("Ranjini", "c24", 7.8),
    Student("Malar", "c17", 8.9),
    Student("Pooja", "c07", 9.1),
    Student("Rubini", "c26", 9.9)
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))
