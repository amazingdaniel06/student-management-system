#Student Management System#

Overview
A Python-based Command Line Interface (CLI) application for managing student records. The system allows users to add, view, update, and delete student information while storing data persistently in a JSON file.
This project was built to practice backend development fundamentals such as data persistence, CRUD operations, modular programming, error handling, and version control with Git and GitHub.

 Features
* Add new students and scores
* View all student records
* Update existing student scores
* Delete student records
* Display the top-performing student
* Calculate the average student score
* Persistent data storage using JSON
* Input validation and error handling

Project Structure
```text
student_app/
│
├── main.py          # Application entry point
├── operations.py    # Business logic
├── utils.py         # File handling and JSON storage
├── students.json    # Student data storage
└── README.md
```

---

Technologies Used
* Python 3
* JSON
* Git
* GitHub

Installation
Clone the Repository

```bash
git clone https://github.com/amazingdaniel06/student-management-system.git
```

Navigate to the Project Folder
```bash
cd student-management-system
```

Run the Application
```bash
python main.py
```

Usage
When the application starts, you will see the following menu:
```text
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Top Student
6. Average Score
7. Exit
```

Select an option and follow the prompts.

---

## Example

```text
Choose an option: 1

Name: Daniel
Score: 85

Student added successfully.
```

```text
Choose an option: 2

Daniel: 85
Ama: 78
```
Skills Demonstrated
* Python programming
* Functions and modular design
* Dictionary data structures
* File handling
* JSON serialization
* Error handling
* CRUD operations
* Git and GitHub workflow

Future Improvements
* Search for a student by name
* Export records to CSV
* Student ranking system
* Graphical User Interface (GUI)
* REST API version using FastAPI
* Database integration with SQLite or PostgreSQL
* User authentication and authorization



Author
Daniel Arku
GitHub: https://github.com/amazingdaniel06
