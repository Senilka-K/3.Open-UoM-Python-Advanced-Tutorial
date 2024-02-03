# Exampel 1 for Dictionaries

scores = {"Saman" : 75, "Nimal" : 80, "Kamal" : 82 }

print(scores["Saman"])
print(scores.get("Kamal"))

scores["Nimal"] = 90
scores["Sunil"] = 78

print(scores)

all_keys = list(scores.keys())
print(all_keys)

all_values = list(scores.values())
print(all_values)

for keys in scores:
    print(keys, scores[keys])

# Exampel 2 for Dictionaries

names = [ "Nimal", "Amal", "Kamal", "Nimal", "Sunil", "Kamal", "Sunil", "Amal", "Sunil", "Ajith"]

counts = dict()

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)