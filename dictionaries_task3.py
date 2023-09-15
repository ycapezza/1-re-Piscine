student = {"name" : "Yohan", "academic_year" : 2023}
student["units"] = {"name" : "Java", "credits" : 20, "grade" : "A"}

grade_weight_mapping = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "E" : 0} 

student["total_credits"] = student.get("units").get("credits")
student["GPA"] = grade_weight_mapping.get(student.get("units").get("grade"))

print(student)