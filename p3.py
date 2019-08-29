#Create a class Student with appropriate data members (rno, name, c_marks, cpp_marks, python_marks, total_marks, percentage, grade)
#and relevant member functions (input(), show(), calc_total(), calc_percentage() and calc_grade()). Also keep record of total count of Student objects. 
#Demonstrate creation and usage of Lambda functions

class Student:

    def input(self,rno,name,c_marks,cpp_marks,java_marks,python_marks):
        self.rno = rno
        self.name = name
        self.c_marks = c_marks
        self.cpp_marks = cpp_marks
        self.java_marks = java_marks
        self.python_marks = python_marks

    def show(self):
        print("Roll Number : ",self.rno)
        print("Name : ",self.name)
        print("C-Marks : ",self.c_marks)
        print("CMarks : ",self.cpp_marks)
        print("Java Marks : ",self.java_marks)
        print("Python Marks : ",self.python_marks)

    def calc_total(self):
        total = self.c_marks + self.cpp_marks+self.java_marks + self.python_marks
        return total

    def calc_percentage(self):
        self.m_total = self.calc_total()
        percentage =self.calc_total // 4
        return percentage

    def Grade(self):
        self.calc_percentage = self.calc_percentage()
        if self.calc_percentage  > 75:
            return 'A'
        elif self.calc_percentage > 60:
            return 'B'
        elif self.calc_percentage > 50:
            return 'C'
        elif self.calc_percentage > 33:
            return 'Pass'
        



#driver
a = Student();
a.input(9,"Atreya",77,69,80,82);
a.show();
print("Total = ",a.calc_total());
print("Percentage = ",float(a.calc_percentage()));
print("Grade = ",a.Grade())

