# DICTIONARY: A mapping of unique keys to values (mutable and unordered by key)
info = {
    "name": "Brajesh Gowda",
    "state" : "basariya",
    "subject" : ["maths", "science", "history"],
    "marks" : 0
      }

# print(info)
# print(type(info))
# print(len(info))

# Updating an existing key replaces only that value; the rest stays intact.
info["marks"] = 10

# Direct key access is fine here because the keys are known to exist.
print(info["name"])
print(info["marks"])

