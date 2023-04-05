import json
from json import JSONEncoder

class Employee:
    def __init__(self, name, DOB, Height,City, State):
        self.name = name
        self.DOB = DOB
        self.Height = Height
        self. City = City
        self. State = State
class EmployeeEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__
employee = Employee( "Bharathi", 2014, 3.4, "Vizag", "Andhrapradesh" )
print ("Encode Employee object into JSON")

EmployeeJSON = json.dumps(employee,indent = 4, cls = EmployeeEncoder)
print(EmployeeJSON)
