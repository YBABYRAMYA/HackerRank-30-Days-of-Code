class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    def __init__(self,firstName,lastName,idNumber,score):
        super().__init__(firstName,lastName,idNumber) 
        self.s=score
    def calculate(self):
        avg = sum(self.s) / len(self.s)
        if avg>=90 and avg<=100:
            grade = "O"
        elif avg>=80:
            grade = "E"
        elif avg>=70:
            grade = "A"
        elif avg>=55:
            grade = "P"
        elif avg>=40:
            grade = "D"
        else:
            grade = "T"
        return grade
        
      
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
