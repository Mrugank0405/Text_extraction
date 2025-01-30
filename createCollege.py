import csv



college_names = [
    "AISSMS College of Engineering",
    "AISSMS Institute of Information Technology",
    "Army Institute of Technology",
    "Bharati Vidyapeeth Deemed University College of Engineering, Pune",
    "College of Agriculture, Pune",
    "College of Engineering, Pune",
    "College of Military Engineering, Pune",
    "Cusrow Wadia Institute of Technology",
    "Dhole Patil College of Engineering",
    "Dr. D.Y. Patil College of Engineering, Pune",
    "G. H. Raisoni College of Engineering and Management",
    "Indian Institute of Aeronautical Engineering & Information Technology",
    "International Institute of Information Technology, Pune",
    "Jayawantrao Sawant College of Engineering",
    "Jayawantrao Sawant Polytechnic",
    "MIT World Peace University",
    "MIT-WPU Faculty of Engineering",
    "MKSSS's Cummins College of Engineering for Women",
    "PES Modern College of Engineering, Pune",
    "Pune Institute of Computer Technology",
    "Pune Vidhyarthi Griha's College of Engineering and Technology",
    "Suman Ramesh Tulsiani Technical Campus - Faculty of Engineering",
    "Supinfocom",
    "Supinfogame",
    "Trinity Academy of Engineering",
    "Vishwakarma Institute of Information Technology",
    "Vishwakarma Institute of Technology",
    "Vishwakarma University"
]

file_name = "college_names.csv"

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["College Name"])
    for name in college_names:
        writer.writerow([name])

print(f"Data has been saved to {file_name}")
