class Student():
  def __init__(self, id, name, course, age):
      self.id, self.name, self.course, self.age = id, name, course, age
  def show(self):
      print(f"id: {self.id}\nname: {self.name}\ncourse: {self.course}\nage: {self.age}\n")

Maiwaa = Student(6901012610137, "Wutthikorn Phumsiri", "CprE.", 18)
Maiwaa.show()

with open("save.txt", "r") as file:
  students = [[] for _ in file]
  line = file.readlines()
  for iFile in range(10):
      parts = line[iFile].strip().split(",")
      id_, name, course, age = parts
      students[iFile] = [int(id_), name, course, int(age)]

students_obj = [Student(s[0], s[1], s[2], s[3]) for s in students]

for iClass in range(len(students)):
  students_obj.append(Student(students[iClass][0], students[iClass][1], students[iClass][2], students[iClass][3]))

for iShow in students_obj:
  iShow.show()

Youngest = Student(s[0], s[1], s[2], s[3])youngest = min(students_obj, key=lambda s: s.age)

print("Youngest student:")
youngest.show()

#6901012610137
#lab08-1,2