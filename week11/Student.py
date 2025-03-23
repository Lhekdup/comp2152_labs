from week11.Person import Person


class Student(Person):
    def __init__(self, p_name, p_age, p_height, major):

        Person.__init__(self, p_name, p_age, p_height)
        self.__major = major
        print("This time it's a Student object")

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value


student1 = Student("Maria", 22, 6, "Computer Science")
print("Maria's major is " + str(student1.major) + ".")
