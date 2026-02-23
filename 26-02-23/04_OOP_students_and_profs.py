#26-02-23_04_OOP_students_and_profs
class Dozent:
    def __init__(self, name, subject, semester):
            self.name = name
            self.subject = subject
            self.semester = semester
    def lehren(self):
          print (f"My name is {self.name} and I am teaching {self.subject} in Semester {self.semester}")

D1=Dozent("Simur Skinner", "Networktechnology", 1)
D2=Dozent("Prof. Frink", "Programming", 2)
D3=Dozent("Sideshow Bob", "Databases", 3)

class Student:
    def __init__(self, name, note, dozent):
            self.name=name
            self.note=note
            self.dozent=dozent
    def Ergebnisse(self):
        if self.note > 91:
            print(f"the Student {self.name} in Semester {self.dozent.semester} with {self.dozent.name} passed with: A")
        elif self.note > 81:
            print (f"the Student {self.name} in Semester {self.dozent.semester} with {self.dozent.name} passed with: B")
        elif self.note > 67:
            print(f"the Student {self.name} in Semester {self.dozent.semester} with {self.dozent.name} passed with: C")
        elif self.note > 50:
             print(f"the Student {self.name} in Semester {self.dozent.semester} with {self.dozent.name} passed with: D")    
        else:
            print (f"the Student {self.name} in Semester {self.dozent.semester} with {self.dozent.name} DID NOT PASS!!!")     

T1 = Student("Lisa Simpson", 97, D1)
T2 = Student ("Ralf Wiggum", 45, D2)
T3 = Student ("Montgomery Burns", 67, D3)

T1.Ergebnisse()
T2.Ergebnisse()
T3.Ergebnisse()

