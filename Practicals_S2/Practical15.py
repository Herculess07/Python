# Print the students name and Python marks from the below dict

sampleDict = {
	"class": {
		"student": {
			"name": "Yash",
			"marks": {
				"Python": 70,
				"SEO/DMM": 80
			}
		}
	}
}

python_marks = sampleDict["class"]["student"]["marks"]["Python"]
name = sampleDict["class"]["student"]["name"]
print(f"Student name : {name}")
print(f"Python Marks : {python_marks}")
# print(sampleDict["class"]["student"]["marks"]["Python"])
