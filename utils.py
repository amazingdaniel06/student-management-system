import json


FILE_NAME = "students.json"



def load_data():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
    

def save_data(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)