class Student():
    def __init__( self ):
        self.vardas = "Vardas"
        self.pavarde = "Pavarde"

    def sakyk_labas(self):
        print(f"Labas as esu {self.vardas} {self.pavarde}")


studentas = Student()

studentas2 = Student()
studentas2.vardas = "Petras"

studentas.sakyk_labas()
studentas2.sakyk_labas()
print(studentas.vardas)
print(studentas2.vardas)

import datetime
class User():
    def __init__(self, email, name, password):
        self.email = email
        self.password = password
        self.name = name
        self.birth_date = datetime.datetime.now()

    def check_password(self,slaptazodis):
        if slaptazodis == self.password:
            print("teisingas")
        else:
            print("neteisingai")


    def __str__(self):
        return f"User: {self.name}, {self.email}"
