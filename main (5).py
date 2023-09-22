class student:
  
 def __init__(self,name,roll_number, cgpa):
   self.name = name 
   self.roll_number = roll_number 
   self.cgpa = cgpa


def sort_students(student_list):
  
  sorted_students = sorted(student_list,
    key=lambda student:student.cgpa,
                       reverse=True)
  return sorted_students



students = [
  student("anitha","A123",8.8),
  student("aathira","A124",7.9),
  student("mathu","A125", 9.8),
  student("swathi","A126",9.4),
]

sorted_student = sort_students(students)


for student in sorted_student:
  print("Name: {}, Roll number:{}, CGPA: {}".format(student.name,
student.roll_number,
student.cgpa))