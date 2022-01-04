class student:
    def __init__(self,name,school,mark):
        self.name=name
        self.school=school
        self.marks=mark
    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(student):
    def __init__(self,name,school,mark,salary):
        super().__init__(name,school,mark)
        self.salary=salary
    
    def func2(self):
        #avg=super().average()
        total=sum(self.marks)
        print(total)

    def weeklysalary(self):
        return self.salary*7

rolf=WorkingStudent("yash","Mit",[67,89,90,80,78],100)
rolf.func2()
print(rolf.average())
print(rolf.weeklysalary(),rolf.salary,rolf.school)

anna=student("vivek","Oxford",[76,89,94,39,98])
print(anna.average())
print(anna.school)


