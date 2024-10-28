from exportStudents import ExportStudents


class ModifyStudents:
    # method to add student to list and export it to csv and txt files, files are deleted after operation and new list overwrite file
    @staticmethod
    def add_student_and_export(path, path2, students):
        name = input("Enter student's name: ")
        surname = input("Enter student's surname: ")
        student_id = input("Enter student's ID: ")
        students.append({"Name": name, "Surname": surname, "ID": student_id})
        ExportStudents.csv(path, students)
        ExportStudents.txt(path2, students)

    # method to add student to file, if file doesn't exist, it will create it
    @staticmethod
    def add_student_by_overwriting(path, path2):
        file = open(path, "a")
        file2 = open(path2, "a")
        student = [input("Enter student's name: "), input("Enter student's surname: "), input("Enter student's ID: ")]
        file.write("\n" + ";".join(student))
        file2.write("\n" + student[0] + " " + student[1] + " - " + student[2])

    

