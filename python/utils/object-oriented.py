# Define the class student
class Student:
    # Constructor method for every class
    # Initializes the class with the properties (student_id, student_name, student_grade)
    # Arguments to the constructor will be passed by the user at the time of creation
    # The self keyword refers to the class that is calling the method
    def __init__(self, sid, name, grade):
        self.student_id = sid
        self.student_name = name
        self.student_grade = grade

    # Method - function that belongs to the class
    # Need self keyword to access the properties of the class
    # This keyword has to be passed as argument when defining a method to be accessible inside
    def get_info(self):
        print(f"{self.student_name} with id {self.student_id} grade {self.student_grade}")


# Define the class SpecializedStudent that inherits from Student
# Inheritance in Python is achieved by passing the parent class to child class
class SpecializedStudent(Student):
    # Constructor for child class
    # Need to initialize the constructor of parent class also
    # Child class can have properties and methods unique to itself
    def __init__(self, sid, sname, grade, domain, subjects):
        super().__init__(sid, sname, grade)
        self.specialization = domain
        self.subject_list = subjects

    # Method unique to SpecializedStudent class
    # Child class can access properties of parent class
    def get_special_info(self):
        print(f"STUDENT {self.student_name} SPECIALIZATION {self.specialization}")
        print(f"SUBJECTS_REGISTERED {self.subject_list}")

    # Child class can access the method of the parent class
    def get_all_info(self):
        self.get_info()
        self.get_special_info()


# Instantiate the classes
student = Student("01A344", "Jane Doe", "A")
specialized_student = SpecializedStudent("BA001", "Lucy Liu", "A", "Science", ["physics", "maths", "chemistry"])

# Accessing the methods of the class
student.get_info()
specialized_student.get_special_info()

# Accessing the method of child class which calls parent class method internally
specialized_student.get_all_info()