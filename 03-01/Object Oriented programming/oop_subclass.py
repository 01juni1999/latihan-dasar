class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self. age=age
        print('(initialized SchoolMember: {})'.format(self.name))
    
    def tell(self):
        '''tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end="")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name,age)
        self.salary = salary
        print('(initialized Teacher:{})'.format(self.name))

    def tell (self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks =marks
        print('(Initialized Student :{})'.format(self.name))

    def tell (self):
        SchoolMember.tell (self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher ('Mr.Shrividya', 40,30000)
s = Student('Swaroop', 25,75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()


