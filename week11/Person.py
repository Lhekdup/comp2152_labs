class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_group = "I'm Public"

        print(self.public_group)

    # def get_name(self):
    #     return self.__name

    # def set_name(self, new_name):
    #     self.__name = new_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")


person1 = Person("Mark", 20, 6)

# print("The name of the person is " + str(person1.get_name()))
# person1.set_name("Anna")
# print("The name of the person is " + str(person1.get_name()))

print("The name of the person is " + str(person1.name))
person1.name = "Anna"
print("The name of the person is " + str(person1.name))