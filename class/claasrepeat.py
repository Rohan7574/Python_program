class one():
    def first(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    def second(self):
        self.a=9
        return self.a-self.b
        
    def third(self):
        self.a=2
        return self.a*self.b

obj=one()
print(obj.first(6,7))
print(obj.second())
print(obj.third())