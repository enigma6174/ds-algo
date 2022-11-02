// Define the class Student
class Student {
  // This is the first method that gets called
  // Initializes the class Student with the properties (studentId, studentName, studentEmail)
  // The arguments to the constructor will be passed by the user
  // The this keyword refers to the object that is calling the class
  constructor(id, name, score) {
    this.studentId = id;
    this.studentName = name;
    this.studentScore = score;
  }

  // Method - function that belongs to the class (or object)
  // We need the this keyword to access the properties of the class
  getInfo() {
    console.log(`Student ${this.studentName} with ID ${this.studentId} scored ${this.studentScore}`);
  }
}

// Define a class ScienceStudent that inherits from Student
// Inheritance is achieved with extends keyword in JavaScript
class ScienceStudent extends Student {
  // Constructor for the child class
  // Need to initialize the constructor of the parent class
  // This class can have properties unique to itslef also
  constructor(id, name, score, subjects) {
    super(id, name, score);
    this.subjectList = subjects;
  }

  // Method unique to ScienceStudent class
  // Parent class properties are accessible in child class
  getSubjects() {
    console.log(`Student ${this.studentName} registered for ${this.subjectList}`);
  }

  // Child class can access parent class method
  getAllInfo() {
    this.getInfo();
    console.log("Subjects Registered:");
    console.log(this.subjectList);
  }
}

// Create object of Student class and ScienceStudent class
// Need to use new keyword when we create an object of a class (ie. instantiate the class)
const student = new Student("012A", "John Smith", 85);
const scienceStudent = new ScienceStudent("510B", "Harry Maguire", 55, ["biology", "computer science", "maths"]);

// Accessing the methods of the class
student.getInfo();
scienceStudent.getSubjects();

// Science ScienceStudent class inherits from Student class it can access parent class methods
scienceStudent.getInfo();

// This method calls the parent class method internally
scienceStudent.getAllInfo();
