from person import Person


class Student(Person): #繼承Person程式碼(重複的部分可以不寫)
    def __init__ (self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    
    # def printname(self):          /
    #     print (self.name)        /
    #                             <==   重複的部分
    # def printage(self):          \
    #     print (self.age)          \
    
    def printschool(self):
        print (self.school)
