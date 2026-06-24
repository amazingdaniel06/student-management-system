from utils import load_data, save_data
from operations import (
    add_student,
    update_student,
    delete_student,
    top_student,
    average_score
) 


def main():
    students = load_data()

    

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Top Student")
        print("6. Average Score")
        print("7. Exit" )


        choice = input("Choose an option: ")

        if choice == "1":
           name = input("Name: ")


           try:
               score = int(input("Score: "))
           except ValueError:
               print("Invalid score. Enter a number")
               continue
    
           students = add_student(students, name, score)
           save_data(students)
           print("Student added successfully.")


        elif choice == "2":
            if not students:
                print("No students found.")
            else:
                for name, score in students.items():      
                    print(f"{name}: {score}")

            

        elif choice == "3":
            name = input("Name to update: ")
            try:
                score = int(input("New score: "))
            except ValueError:
                print("Invalid score")
                continue    

            if  update_student(students, name, score):
                save_data(students)
                print("Updated successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Name to delete: ")
        
        
            if delete_student(students, name):
                save_data(students)
                print("Deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "5":
            if students:
               print("Top student:", top_student(students))
            else:
                print("No students available.")   

        elif choice == "6":
            if students:
               print("Average score:", average_score(students))
            else:
                print("No students available.")   


        elif choice == "7":
            print("Goodbye.")
            break  

        else:
            print("Invalid option. Try again.")          

            


if __name__ == "__main__":
    main()