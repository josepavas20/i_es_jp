# Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)

class Student:
    name = input("ingrese su nombre: ")
    age = int(input("ingrese su edad"))
    grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Crear un constructor que inicialice los atributos
    def __int__(self, name: str, age: int, grades):
        self.name: str = name
        self.age: int = age
        self.grades = grades

    # Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades
    def add_grade(self):
        grado=int(input("ingrese el grado"))
        self.grades.append=grado
        

