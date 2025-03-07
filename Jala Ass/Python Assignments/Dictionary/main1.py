students = {101: "Chakri", 102: "Prasad", 103: "Charlie", 104: "David", 105: "Mahesh"}

# 1.1
students[106] = "Vijay"

# 1.2
students[103] = "Madhav"

# 1.3
print(students[102])

# 1.4
nested_students = {
    "Class A": {201: "eshwar", 202: "raju"},
    "Class B": {203: "mikey", 204: "ravi"}
}

# 1.5
print(nested_students["Class A"][201])

# 1.6
print(students.keys())

# 1.7
del students[104]
