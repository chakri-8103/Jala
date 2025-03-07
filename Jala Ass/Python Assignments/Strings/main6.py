import re
pattern = r"\bWorld\b"
match = re.match(pattern, "World")
print(bool(match))
