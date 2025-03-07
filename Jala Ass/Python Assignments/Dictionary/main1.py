students = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "David", 105: "Eve"}

# 1.1
students[106] = "Frank"

# 1.2
students[103] = "Chris"

# 1.3
print(students[102])

# 1.4
nested_students = {
    "Class A": {201: "John", 202: "Mike"},
    "Class B": {203: "Sarah", 204: "Anna"}
}

# 1.5
print(nested_students["Class A"][201])

# 1.6
print(students.keys())

# 1.7
del students[104]
