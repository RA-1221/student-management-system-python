class Student :
    def __init__(self , name , Sid , major):
        self.name = name
        self.Sid = Sid
        self.major = major
        
    def displayInfo(self):
            print(self.name)
            print(self.Sid)
            print(self.major)


   
s1 = Student ( " Ranoo" , 432, " CS")
s2 = Student ( " Amal" , 433, " CS")



class Database :
    def __init__(self):
        self.students =[ ]

    def Add(self ,Student ):
     self.students.append(s1)
     self.students.append(s2)

    def View( self ):
     for Student in self.students:
          Student.displayInfo()

    def Search (self , Sid):
     for Student in self.students:
          if Student.Sid == Sid:
               return Student

    def Delete (self , Sid):
     for Student in self.students:
          if Student.Sid == Sid:
               self.students.remove(Student)


db = Database()
while True :
     print( " Student Management System")
     print("1. Add Student ")
     print("2. View Students ")
     print("3. Search Student ")
     print("4. Delete Student ")
     print("5. Exit " )

     choice = input (" choose an input ")

     if choice == "1" :
          name= input(" enter name ")
          Sid = int(input(" enter ID "))
          major = input( " enter major ")

          s = Student(name , Sid , major)
          db.Add(s)

          print ( " Studente added ")




     elif choice == "2":
          db.View()

     elif choice == "3":
          Sid = int(input( "Enter Id "))
          S=db.Search(Sid)

          if S :
               S.displayInfo()
          else:
               print(" not found ")



     elif choice == "3":
          Sid = int(input( "Enter Id "))
          db.Delete(Sid)

          print (" Student deleted ")

     elif choice == "5":
          print (" GoodBye")

     else:
          print( " Eroor !")


