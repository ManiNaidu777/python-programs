student = {
    "Name":"Mani",
    "Age":21,
    "Course":"MCA"
    }

print(student["Name"])
print(student.get("Age"))
print(student.get("Course"))
print(student)
student["city"]="Ravulapalem"
print(student["city"])
student.update({"Age":22})
print(student.get("Age"))
student.pop("Age")
print(student.get("Age"))
print(student)
student["Roll Num"]=10
student["section"]="mca-1"
print(student)
student.update({"Name":["mani","vignesh"]})
print()
