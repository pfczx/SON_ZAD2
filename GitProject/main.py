from importStudents import ImportStudents
from addStudent import ModifyStudents

lista = ImportStudents.csv("lists/student_list.csv")
'''
for student in lista:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))

'''
lista2 = ImportStudents.txt("lists/student_list.txt")
'''
for student in lista2:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))
'''

ModifyStudents.add_student(lista)

for student in lista:
    print(student.get("Name"), student.get("Surname"), student.get("ID"))
