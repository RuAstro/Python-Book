# class Dog:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name)
    
#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
        
# dog1_name = "Tim"
# dog1_age = 32

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
        
        def add_student(self, student):
            if len(self.students) < self.max_students:
                self.students.append(student)
                return True
            return False
        
        def get_average_grade(self):
            pass
        
    s1 = Student("RJ", 19, 95)
    s2 = Student("Bill", 20, 75)
    s3 = Student("Piet", 19, 65)
    
    course = Course("Science", 2)
    course = add.student(s1)
    course = add.student(s2)
    print(course.students[0].name)
        