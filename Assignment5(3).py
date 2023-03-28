class student_class :
    def __init__(self,Name,Rollnumber):
        self.Name = Name
        self.Rollnumber = Rollnumber
    def setName(self,N):
        self.Name =N
    def getName(self):
        return self.Name
    def setRollnumber(self,R):
        self.Rollnumber = R
    def getRollnumber(self):
        return self.Rollnumber
    

B = student_class("Bharathi",30)

    
print(B.getName())
print(B.getRollnumber())
print(B.Name)
print(B.Rollnumber)
    

        