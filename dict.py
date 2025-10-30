student = {
    "name": "arshpreet",
    "age": 18,
    "sub": ["mth", "Science", "english"],
    "marks": {"mth": 90, "science": 85, "english": 88}
}
print(student)


print(student.get("name"))
print(student["subjects"])
student["city"] = "Delhi"
student["age"] = 19
student.pop("city")

keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)
for sub, mark in student["marks"].items():
    print("{subject}: {mark}")
print("age" in student)
