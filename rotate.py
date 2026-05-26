import json

with open("data/projects.json", "r") as f:
    data = json.load(f)

people = data["people"]
projects = data["projects"]

projects = projects[1:] + projects[:1]

assignments = {}
for i, person in enumerate(people):
    assignments[person] = projects[i]

data["projects"] = projects
data["assignments"] = assignments

with open("data/projects.json", "w") as f:
    json.dump(data, f, indent=2)