student = {
    "naam": "Timon",
    "leeftijd": 16,
    "school": "van Veldeke",
    "hobbys": "voetbal, gitaar"
}
print(student["naam"])
student["woonplaats"] = "Runkst"
student["leeftijd"] += 1
del student["school"]
print(student)
